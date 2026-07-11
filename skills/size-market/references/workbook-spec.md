# Workbook specification

## Required tabs

Use the included template or recreate these tabs in this order:

1. `00_说明`: purpose, as-of date, conventions, color legend, model limitations, and navigation. Name the first section `模型信息`.
2. `01_结论`: market definition, TAM/SAM/SOM, user revenue and user-count share, method range, scenario outlook, and key takeaways. Define Point, Low, and High directly beside the method table.
3. `02_口径`: business description, customer, monetization, geography, currency, base year, inclusions/exclusions, incremental/replacement classification, user-provided metrics, and common assumptions. Use clear labels such as `用户输入链接`, `分析假设`, `反推公式`, and `跨表公式`; do not use unexplained `Analyst` or `Analyst bridge` labels.
4. `03_来源`: title the sheet `数据来源`. Store one atomic source fact per row with a typed value, full URL, and source ID. Do not store assumptions in this sheet.
5. `04_结构`: demand segments, geography, channel/form factor, market-module boundaries, and overlap logic. Give every table an explicit header and use `模块`, not `经济池`.
6. `05_驱动`: current macro and operating drivers, historical observations, forecast relevance, and source IDs.
7. `06_用户法`: segment-level addressable units, active rate, paid rate, ARPPU or usage, Point/Low/High market calculations. Put units in every numeric header.
8. `07_收入法`: public, private, mobile, web, desktop, service, and channel revenue aggregation with coverage and normalization. Show the base-year conversion factor and the rationale for each Low/High coefficient. Decompose material private and long-tail estimates into visible components.
9. `08_公司价值链`: title the sheet `公司倒推与模块拆分`; include public-company/leader-share reverse checks and non-overlapping market-module estimates.
10. `09_勾稽`: method point/low/high, score, weight, weighted result, divergence checks, TAM-to-SAM bridge.
11. `10_情景`: conservative, base, and aggressive Year 0–3 driver builds and CAGRs. Define demand-volume growth, price/mix change, structural adoption uplift, and constraint factor in the sheet and explain each scenario's values.
12. `11_竞争KSF`: competitor map including the modeled company, formula-linked relevant revenue and TAM revenue share, value accrual, moat/commoditization, KSFs, and falsification indicators.
13. `12_检查`: source completeness, weight, units, formula errors, component tie-outs, data-lineage status, share bounds, scenario ordering, and overall status.

## Formula and input rules

- Put each assumption in one labeled cell.
- Keep source facts, assumptions, and calculations in distinct areas. Never place an assumption in `03_来源`.
- Store one source metric and one typed value per source row. Split multiple metrics from one document into separate IDs or suffixed IDs.
- Use formulas for all derived values; do not hardcode calculated totals.
- Quote every cross-sheet worksheet name in formulas.
- Use bounded ranges, not entire-column references.
- Use blue font for editable inputs, green for cross-sheet formulas, black for same-sheet formulas, and yellow fill for unresolved inputs.
- Use real numeric/date values and explicit formats.
- Keep currency and unit scale visible in headers.
- Add source IDs beside model inputs; full URLs belong in `03_来源`.
- Make every headline result traceable to an atomic source row or editable assumption.
- Add comments to complex or judgment-heavy assumptions when supported.
- Separate actual/base-year data from forecast periods visually.

## Core equations

User method:

`Segment market = addressable units × active rate × paid rate × annual ARPPU`

Usage-based alternative:

`Segment market = units × events per year × output per event × price per output`

Revenue method:

`Point normalized revenue = source-period revenue × relevant-category share × overlap/geography adjustment × base-year conversion factor`

`Low revenue = Point normalized revenue × Low coefficient`

`High revenue = Point normalized revenue × High coefficient`

Define Point as the most likely current estimate. Define Low/High as conservative/optimistic model boundaries, not statistical confidence intervals. State the reason for every material coefficient.

Leader-share method:

`Implied market = relevant revenue ÷ category revenue share`

Market-module method:

`Net module revenue = gross module revenue × inclusion rate × (1 − overlap/pass-through rate)`

Reconciliation:

`Reconciled TAM = SUM(method point estimate × method weight)`

`SAM = TAM × serviceable geography × serviceable category × reachable channel/customer factor`

`Comparable user revenue = provided annualized revenue, otherwise active users × estimated paid rate × annual ARPPU`

`Current revenue share = comparable user revenue ÷ SAM`

## Summary requirements

Show point estimate and range together. Display the market definition and as-of date adjacent to the headline number. Include both market revenue and user-denominator views when possible.

Create after data is populated:

- Bar chart: point/low/high estimate by method.
- Line chart: conservative/base/aggressive market through Year 3.
- Bar or compact table: demand segment or value-chain composition.

Each chart must be formula-backed, have explicit units, and avoid decorative effects.

## Checks

At minimum test:

- Reconciliation weights equal 100%.
- Low ≤ point ≤ high for each method.
- TAM ≥ SAM ≥ SOM revenue.
- User and revenue shares are between 0% and 100%, or exceptions are explained.
- Scenario Year 0 equals reconciled TAM or the explicitly selected market base.
- Conservative ≤ base ≤ aggressive by Year 3, unless the model explains a crossing.
- Component totals equal displayed totals.
- Private-company and long-tail component tables equal the main revenue-method rows.
- No required source ID is blank.
- Source IDs use source rows only; assumptions are labeled separately.
- At least one headline TAM formula is traced to sources and assumptions.
- A temporary source-value change updates at least two downstream sheets, and the source is restored before export.
- No `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, or unexplained `#N/A` errors.

## Visual quality

Hide gridlines when explicit styling provides structure. Freeze useful header rows and label columns. Use dark section headers, restrained color, readable source columns, and no merged cells in calculation blocks. Keep summary tabs compact and all text visible at normal zoom.
