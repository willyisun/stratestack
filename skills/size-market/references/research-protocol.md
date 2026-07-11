# Research protocol

## 1. Define the denominator

Before searching, write the market equation in words. Specify:

- Product or job being purchased.
- Buyer and end user.
- Revenue concept: vendor revenue, customer spend, GMV, take-rate revenue, or total value-chain revenue.
- Geography and base year.
- Active-period definition for users.
- Included and excluded categories.

Maintain separate denominators when the business spans multiple market modules. Do not add GMV to revenue or upstream revenue to downstream pass-through spend.

## 2. Search in waves

### Wave A: orientation

Identify category vocabulary, segments, public leaders, regulators, trade bodies, and candidate research firms. Treat search snippets as discovery only.

### Wave B: primary evidence

Search official statistics and company materials. For public companies inspect annual reports, 10-K/20-F, S-1/F-1 or local prospectuses, investor presentations, earnings materials, and disclosed KPIs. Search filings for `market`, `TAM`, `industry`, `users`, `customers`, `volume`, `pricing`, `revenue`, and segment definitions.

### Wave C: gap filling

Use reputable third-party datasets for app revenue/downloads, web traffic, device/usage, private-company estimates, and industry shares. Record coverage and methodology limitations.

### Wave D: contradiction search

Actively search for a different estimate, a narrower definition, a declining price, a substitute, or a regulatory/technical constraint. A model with only confirming evidence is incomplete.

## 3. Source hierarchy

Use this order unless a lower-tier source measures the specific metric better:

1. Government, regulator, official census/statistics, audited filing, prospectus.
2. Company investor relations, earnings releases, official platform disclosures.
3. Trade associations and methodology-disclosed research.
4. Recognized measurement providers such as app/traffic panels.
5. Credible media quoting a named source.
6. Aggregators, blogs, and anonymous estimates only as leads or low-confidence bounds.

Triangulate company-provided TAM claims; they may use broad boundaries. A filing is primary for the company's own revenue, but not automatically authoritative for industry size.

## 4. Freshness and time normalization

- Target current-year or latest-twelve-month data.
- Record the source period and retrieval date separately.
- Annualize interim values only when seasonality is understood; state the formula.
- Bridge an older industry datum with an explicit driver such as population, installed base, transactions, or category revenue growth.
- Use the exchange rate appropriate to the measurement: average-period for revenue flows, period-end for point-in-time stock. Record FX source and date.
- Do not silently combine fiscal years and calendar years.

## 5. Evidence ledger fields

Each source row should contain exactly one atomic metric and one typed value. Split multiple facts from one document into separate source IDs or suffixed IDs. Each source fact should have:

`source_id`, `metric`, `value`, `unit`, `period`, `geography`, `source_type`, `publisher`, `document_title`, `url`, `retrieved_at`, `primary_or_secondary`, `confidence`, `used_in`, and `notes`.

Do not store analysis assumptions or model calculations in the evidence ledger. Put assumptions in visible blue model cells with an assumption ID, unit, rationale, and owner sheet. Keep formula-derived calculations in calculation sheets. For user-provided facts, allow an explicit `user-provided` URL marker and make clear that the value was not independently verified.

Confidence guidance:

- High: direct, current, definition-matched primary evidence.
- Medium: reputable measurement or a transparent derivation with limited assumptions.
- Low: partial coverage, old data, weak definition match, or assumption-heavy inference.

## 6. Research completeness tests

Do not stop until all are true or explicitly marked unavailable:

- Target at least 12 substantive evidence rows, including at least three primary-source rows, two relevant public-company filings/prospectuses when public comparables exist, one macro/demand anchor, and one contradictory or constraining source. Treat these as breadth targets, not permission to add weak sources; document exceptions for narrow markets.

- Geography and base year are clear.
- At least one demand-side denominator exists.
- At least one supply/revenue-side estimate exists.
- Public-company revenue and leader-share evidence have been investigated.
- Private/mobile/web/desktop/offline gaps have been considered where relevant.
- Price, paid conversion, frequency, or take rate is sourced or visibly assumed.
- At least one contrary or constraining signal is documented.
- Every material workbook input has a source ID or assumption label.
- Each headline output can be traced through formulas to atomic source rows and labeled assumptions.

## 7. Citation discipline

Use full URLs in the source register. Cite the document page, table, section, or filing item in notes when possible. Paraphrase source claims; do not paste long copyrighted passages. Never cite a search-results page when the underlying source is accessible.
