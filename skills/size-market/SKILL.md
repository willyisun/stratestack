---
name: size-market
description: Research and calculate an auditable market size, TAM/SAM/SOM, current user or revenue share, market structure, competition, growth drivers, and conservative/base/aggressive three-year scenarios, then deliver an Excel workbook with atomic source facts, separate editable assumptions, full formula lineage, and explicit uncertainty logic. Use when a user describes a business and provides only current users or revenue; when asked for market sizing, market space, 市场规模, 市占率, 行业空间, TAM/SAM/SOM, top-down or bottom-up estimates, industry research, investment-style market analysis, or a source-backed Excel sizing model.
---

# Size Market

Turn a short business description plus current users and/or revenue into a source-backed market model. Optimize for understanding the business—structure, competition, growth, changing demand, and economics—not for producing a single impressive number.

## Non-negotiable output

Deliver one `.xlsx` workbook, not only a narrative. Make every headline result traceable through formulas to a visible source fact or editable assumption. Do not use a workbook that merely contains formulas between hardcoded output tables.

Use the included `assets/market-sizing-template.xlsx` when practical. Copy it before editing. If the host cannot edit the template, recreate the same tabs with its native spreadsheet tool using `references/workbook-spec.md`. Never return CSV files as a substitute for the requested workbook.

## Minimal-input contract

Accept these as sufficient:

1. What the business does.
2. Current active users and/or annualized revenue.

Do not require the user to supply industry, geography, customer type, monetization, or competitors when they can be researched or reasonably inferred. Infer them, label every inference, and show alternatives when an ambiguity materially changes the answer. Ask one concise question only when competing interpretations would change the market definition by more than roughly 2x and public evidence cannot resolve it.

Default to the current date as the research cut-off, the latest completed calendar year as the base year, both local currency and USD when conversion matters, and regional splits plus a global roll-up when geography is uncertain.

## Model-control contract

Use three distinct cell classes:

- Source facts: one atomic data point per row in `03_来源`; black text unless the user is expected to update the fact.
- Editable assumptions and user inputs: blue text with a visible rationale and unit.
- Calculations: black for same-sheet formulas and green for formulas linking another sheet.

Never place an analysis assumption in the source ledger. Keep source IDs and assumption IDs separate. Use `S...` for source facts and `A...` for assumptions when IDs are helpful.

Explain these terms inside the workbook:

- Point: the most likely current estimate under the stated assumptions.
- Low / High: conservative and optimistic model boundaries, not statistical confidence intervals.
- Base-year conversion factor: the explicit multiplier that moves a source period, ARR, run-rate, currency, or partial-period value to the common model year.

## Required references

Read each reference before the indicated phase:

- Before searching: `references/research-protocol.md`.
- Before selecting calculations: `references/sizing-methods.md`.
- Before forecasting: `references/scenarios.md`.
- Before building the workbook: `references/workbook-spec.md`.
- Before writing competition and KSF conclusions: `references/competition-ksf.md`.

## Workflow

### 1. Frame the market

Write a one-sentence market definition with product, customer, job-to-be-done, monetization, geography, and base year. Specify inclusions and exclusions.

Classify the business as:

- Incremental demand: creates a new job, usage occasion, or budget.
- Replacement: substitutes an existing workflow, labor pool, tool, or spend category.
- Hybrid: replaces part of an existing pool and creates measurable new consumption.

Do not start with a market-report number. First define the denominator.

### 2. Build a research plan

Create a search matrix covering:

- Geography: global, operating region, and major regional differences.
- Demand: population, businesses, devices, connectivity, time spent, transactions, content/work units, and relevant installed bases.
- Supply and revenue: public companies, private products, mobile, web, desktop, services, and indirect channels.
- Economics: price, ARPPU/ARPU, paid conversion, frequency, take rate, capacity, and replacement rate.
- Competition: category leaders, adjacent substitutes, open-source/free alternatives, and value-chain owners.
- Forecasting: demand growth, price/mix, adoption/substitution, constraints, regulation, and platform shifts.

Search broadly, but use facts only after opening the underlying source. Prefer current-year data; otherwise use the latest reported period and explicitly bridge it to the base year.

### 3. Collect an evidence ledger

Record each source fact in `03_来源` before using it. Store one metric and one typed value per row; split revenue, users, growth, price, and share from the same document into separate rows. Every row needs source ID, metric, value, unit, period, geography, publisher, document title, full URL or an explicit user-input marker, retrieval date, source type, and confidence.

Prefer primary sources: official statistics, regulator data, company filings, prospectuses, annual reports, earnings materials, and platform disclosures. Use third-party traffic, app, and market datasets to fill gaps and triangulate; disclose paywall, sample, coverage, or methodology limitations. Never invent a paywalled number.

Separate into different workbook areas:

- Reported or user-provided source fact in `03_来源`.
- Formula-derived calculation in a model sheet.
- Editable assumption in a labeled assumption cell or component table.

### 4. Map structure before sizing

Segment demand by distinct buyer/job/economic model rather than by arbitrary demographics. Cover all economically material channels and form factors.

Map market modules when participants monetize different layers. Use the word `module`, not an unexplained economic pool. Give every structure table an explicit header. Identify double-counting boundaries: pass-through revenue, payments, ad spend, cloud/hosting, services, and bundled products often overlap.

### 5. Calculate with independent methods

Use at least two genuinely independent methods and normally three or more. Choose from `references/sizing-methods.md`.

Required when data permits:

- Demand/user bottom-up: addressable units × usage/frequency × paid rate × price.
- Revenue aggregation: public-company relevant revenue plus private/mobile/web/desktop/channel estimates.
- Leader-share reverse check: leader relevant revenue ÷ defensible category share.
- Replacement pool: existing spend or work units × replaceable share × adoption × new price.
- Value-chain build: non-overlapping monetization pools across the chain.
- External-report range: use only as a benchmark, never the sole answer.

For each method calculate Point, Low, High, and confidence. Build Low/High from visible driver ranges where possible. When using a coefficient, explain the basis beside the row: source reliability, age, definition match, coverage, or private-company opacity.

In the revenue method, show reported revenue, relevant-category share, overlap/geography adjustment, base-year conversion factor, Point, Low coefficient, High coefficient, Low, High, source ID, conversion rationale, and range rationale. Decompose any material private-company, bundled-platform, or long-tail estimate into named editable components; do not use one unexplained residual.

### 6. Reconcile instead of averaging blindly

Normalize all estimates to the same geography, base year, currency, revenue concept, and value-chain boundary. Weight methods by coverage, independence, source quality, and assumption intensity.

Investigate divergences greater than 2x. Typical causes are mixed GMV/revenue, annual/monthly units, users/accounts/devices, cumulative/active users, value-chain double counting, geography mismatch, or a report using a different category definition.

Produce TAM, SAM, and SOM explicitly:

- TAM: the full defined economic pool under the stated boundary.
- SAM: the portion serviceable by current product, geography, channel, and customer constraints.
- SOM/current share: the user's annualized comparable revenue divided by SAM; also show user share when a comparable active-user denominator exists.

Never calculate share using incomparable numerator and denominator definitions.

### 7. Forecast three years

Build conservative, base, and aggressive cases from visible demand, penetration/adoption, price/mix, and constraint assumptions. Do not merely apply three arbitrary CAGR values.

Define the scenario drivers in the workbook:

- Demand-volume growth: growth in users, seats, jobs, content units, usage, or transactions, excluding price and structural uplift.
- Price/mix change: pricing, discounting, enterprise mix, credits, or product mix per unit.
- Structural adoption uplift: additional paid penetration, frequency, new use cases, or replacement unlocked by technology, excluding base demand growth.
- Constraint factor: a multiplier for regulation, distribution, capacity, compute, rights, or other bottlenecks; `1.00` means no incremental drag.

Start Year 0 from the reconciled current market. Use copy-across formulas. Show the definition, rationale, source anchors, driver bridge, and implied CAGR for each scenario. Read `references/scenarios.md` for guardrails.

### 8. Explain competition, change, and KSF

Answer:

- Where value accrues and why.
- Which layer is concentrated or commoditizing.
- How demand and structure are changing.
- What drives growth and what caps it.
- Which capabilities determine durable success.
- What evidence would falsify the thesis.

Distinguish table stakes from true key success factors. Tie each KSF to an economic driver or structural bottleneck.

Include the modeled company itself in the competition table. Show numeric relevant revenue and revenue share of TAM for every competitor that can be linked to the revenue model; leave unknowns blank rather than replacing them with qualitative labels.

### 9. Build and verify the workbook

Follow `references/workbook-spec.md`. Keep hardcoded inputs separate from formulas; use blue font for editable assumptions, green font for cross-sheet formulas, black for same-sheet formulas, and yellow fill for unresolved inputs.

Create native charts only after data is populated. Include a method-comparison chart, a three-scenario market trend, and a segment/value-chain view when they add insight.

Before delivery:

1. Scan for formula errors and circular references.
2. Check units, periods, currencies, and geography.
3. Confirm weights sum to 100% and all key outputs link to formulas.
4. Trace at least one headline TAM cell back to source facts and assumptions.
5. Perform a live-link test in memory: change one source value, confirm at least two downstream sheets update, then restore the value before export.
6. Confirm every external numeric input has a source ID and every assumption is visibly labeled and editable.
7. Reconcile component totals, segment totals, method estimates, TAM/SAM/SOM, revenue share, user share, and competitor shares.
8. Visually inspect every user-facing tab for missing headers, clipping, overlap, unreadable text, and blank/broken charts.
9. Ensure the cover states the as-of date, limitations, and exact color legend.

If a spreadsheet-capable tool is unavailable, report that blocker rather than pretending to have created an Excel file.

## Optional evidence validation

When research is first stored as JSON, run:

```bash
python scripts/validate_evidence.py evidence.json
```

Use the JSON shape documented at the top of the script. Fix errors before modeling; treat warnings as review items.
