#!/usr/bin/env python3
"""Validate a size-market research evidence JSON file.

Expected shape:
{
  "study": {"as_of_date": "YYYY-MM-DD", "base_year": 2025,
            "market_definition": "...", "geography": "..."},
  "sources": [{"source_id": "S001", "metric": "...", "value": 1,
               "unit": "USD", "period": "2025", "geography": "Global",
               "source_type": "filing", "publisher": "...",
               "document_title": "...", "url": "https://...",
               "retrieved_at": "YYYY-MM-DD", "confidence": "High",
               "used_in": "06_用户法!C8", "fact_type": "reported"}],
  "assumptions": [{"assumption_id": "A001", "metric": "Paid rate",
                   "value": 0.1, "unit": "%", "rationale": "...",
                   "owner_sheet": "06_用户法", "editable": true}],
  "methods": [{"name": "Demand bottom-up", "point": 1,
               "low": 0.8, "high": 1.2, "weight": 0.5}],
  "scenarios": [{"name": "Conservative"}, {"name": "Base"},
                {"name": "Aggressive"}]
}
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


REQUIRED_STUDY = ("as_of_date", "base_year", "market_definition", "geography")
REQUIRED_SOURCE = (
    "source_id", "metric", "value", "unit", "period", "geography",
    "source_type", "publisher", "document_title", "url", "retrieved_at",
    "confidence", "used_in", "fact_type",
)
REQUIRED_ASSUMPTION = (
    "assumption_id", "metric", "value", "unit", "rationale",
    "owner_sheet", "editable",
)
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SOURCE_ID_RE = re.compile(r"^S[0-9A-Z]+(?:-[0-9A-Z]+)*$")
ASSUMPTION_ID_RE = re.compile(r"^A[0-9A-Z]+(?:-[0-9A-Z]+)*$")


def valid_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def user_input_marker(value: object) -> bool:
    if not isinstance(value, str):
        return False
    return value.strip().lower() in {
        "n/a", "user-provided", "n/a — user-provided", "n/a - user-provided"
    }


def atomic_value(value: object) -> bool:
    return not isinstance(value, (list, dict))


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python validate_evidence.py evidence.json")
        return 2

    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read valid JSON: {exc}")
        return 2

    errors: list[str] = []
    warnings: list[str] = []
    study = data.get("study", {})
    for field in REQUIRED_STUDY:
        if study.get(field) in (None, ""):
            errors.append(f"study.{field} is required")
    if study.get("as_of_date") and not DATE_RE.match(str(study["as_of_date"])):
        errors.append("study.as_of_date must be YYYY-MM-DD")

    sources = data.get("sources", [])
    if not sources:
        errors.append("at least one source is required")
    ids: set[str] = set()
    for index, source in enumerate(sources, start=1):
        prefix = f"sources[{index}]"
        for field in REQUIRED_SOURCE:
            if source.get(field) in (None, ""):
                errors.append(f"{prefix}.{field} is required")
        sid = source.get("source_id")
        if sid in ids:
            errors.append(f"{prefix}.source_id duplicates {sid}")
        elif sid:
            ids.add(sid)
        if sid and not SOURCE_ID_RE.match(str(sid)):
            errors.append(f"{prefix}.source_id must start with S and use only uppercase letters, digits, or hyphens")
        fact_type = source.get("fact_type")
        source_type = str(source.get("source_type", "")).lower().replace("_", "-")
        is_user_input = fact_type == "user_input" or source_type in {"user-input", "user input"}
        if source.get("url") and not valid_url(source["url"]):
            if not (is_user_input and user_input_marker(source["url"])):
                errors.append(f"{prefix}.url must be a full http(s) URL or an explicit user-provided marker")
        if source.get("retrieved_at") and not DATE_RE.match(str(source["retrieved_at"])):
            errors.append(f"{prefix}.retrieved_at must be YYYY-MM-DD")
        if source.get("confidence") not in {"High", "Medium", "Low"}:
            errors.append(f"{prefix}.confidence must be High, Medium, or Low")
        if fact_type not in {"reported", "user_input"}:
            errors.append(f"{prefix}.fact_type must be reported or user_input; calculations and assumptions do not belong in sources")
        if not atomic_value(source.get("value")):
            errors.append(f"{prefix}.value must be one atomic value; split multiple metrics into separate source rows")

    assumptions = data.get("assumptions", [])
    assumption_ids: set[str] = set()
    for index, assumption in enumerate(assumptions, start=1):
        prefix = f"assumptions[{index}]"
        for field in REQUIRED_ASSUMPTION:
            if assumption.get(field) in (None, ""):
                errors.append(f"{prefix}.{field} is required")
        aid = assumption.get("assumption_id")
        if aid in assumption_ids:
            errors.append(f"{prefix}.assumption_id duplicates {aid}")
        elif aid:
            assumption_ids.add(aid)
        if aid and not ASSUMPTION_ID_RE.match(str(aid)):
            errors.append(f"{prefix}.assumption_id must start with A and use only uppercase letters, digits, or hyphens")
        if not atomic_value(assumption.get("value")):
            errors.append(f"{prefix}.value must be one atomic value")
        if assumption.get("editable") is not True:
            errors.append(f"{prefix}.editable must be true so the workbook can expose it as a blue input")

    methods = data.get("methods", [])
    if len(methods) < 2:
        errors.append("at least two independent sizing methods are required")
    total_weight = 0.0
    for index, method in enumerate(methods, start=1):
        prefix = f"methods[{index}]"
        for field in ("name", "point", "low", "high", "weight"):
            if method.get(field) in (None, ""):
                errors.append(f"{prefix}.{field} is required")
        try:
            low = float(method.get("low", 0))
            point = float(method.get("point", 0))
            high = float(method.get("high", 0))
            weight = float(method.get("weight", 0))
            if not low <= point <= high:
                errors.append(f"{prefix} must satisfy low <= point <= high")
            total_weight += weight
        except (TypeError, ValueError):
            errors.append(f"{prefix} numeric fields must be numbers")
    if methods and abs(total_weight - 1.0) > 0.001:
        errors.append(f"method weights sum to {total_weight:.4f}, not 1.0")

    scenario_names = {str(s.get("name", "")).lower() for s in data.get("scenarios", [])}
    for required in ("conservative", "base", "aggressive"):
        if required not in scenario_names:
            errors.append(f"scenario {required!r} is required")

    if len(sources) < 12:
        warnings.append("fewer than 12 evidence rows; confirm research breadth or document why the market is narrow")
    primary_count = sum(
        1 for s in sources
        if str(s.get("source_type", "")).lower() in {
            "government", "regulator", "filing", "prospectus", "company-ir"
        }
    )
    if sources and primary_count < 3:
        warnings.append("fewer than 3 clearly primary source rows found")
    filing_count = sum(
        1 for s in sources
        if str(s.get("source_type", "")).lower() in {"filing", "prospectus"}
    )
    if sources and filing_count == 0:
        warnings.append("no filing or prospectus found; confirm whether public comparables exist")
    if not assumptions:
        warnings.append("no assumptions supplied; confirm all model judgments will remain outside the source ledger")

    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARNING: {message}")
    if errors:
        print(f"FAIL: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"PASS: {len(sources)} source(s), {len(assumptions)} assumption(s), {len(methods)} method(s), {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
