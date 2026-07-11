# Three-year scenarios

## Model the drivers

Forecast each scenario from a small set of visible drivers:

`Market(t) = Market(t-1) × (1 + demand growth) × (1 + price/mix growth) × (1 + structural uplift) × constraint factor`

Use a more specific operating equation when available, such as users × paid rate × ARPPU, units × frequency × price, or installed base × attach rate × annual spend.

Use these exact driver meanings unless a more specific operating equation replaces them:

- Demand-volume growth: growth in users, seats, jobs, content units, usage, transactions, or installed base; exclude pricing and structural uplift.
- Price/mix change: change in revenue per unit from pricing, discounting, enterprise mix, credits, or product mix.
- Structural adoption uplift: additional paid penetration, usage frequency, replacement, new use cases, or module expansion not already captured in demand and price.
- Constraint factor: multiplicative impact from capacity, compute, supply, regulation, distribution, rights, or talent. `1.00` means no incremental drag; `0.99` means roughly 1% annual drag.

Avoid double counting structural adoption with demand growth, paid-rate growth, or price/mix.

Constraint factor is normally 100% and can fall below 100% for capacity, compute, supply, regulation, distribution, or talent bottlenecks. Do not use it as an unexplained plug.

## Scenario meanings

- Conservative: slower demand and adoption, weaker price/mix, stronger constraints, or faster commoditization. It should be plausible, not catastrophic unless evidence supports a downside case.
- Base: the most evidence-backed continuation plus explicit structural change.
- Aggressive: faster adoption and favorable price/mix or usage expansion, still bounded by physical, budget, distribution, or capacity ceilings.

Change multiple economically coherent drivers. Do not create scenarios by multiplying one base CAGR by arbitrary discounts or premiums.

## Required bridges

For every scenario show:

- Year 0 market tied to the reconciled current estimate.
- Year 1, Year 2, and Year 3 driver assumptions.
- Implied annual growth and three-year CAGR.
- Demand/volume contribution.
- Price/mix contribution.
- Adoption/structural contribution.
- Constraint or cannibalization impact.
- A plain-language definition and a visible rationale for every driver row.

For a replacement market, also show the remaining replaceable pool and prevent cumulative adoption from exceeding it. For an installed-base model, prevent penetration from exceeding 100% unless units per account can exceed one and that is explicitly modeled.

## Assumption anchors

Anchor forecasts to at least two of:

- Historical category or leader growth.
- Macro/user/device/transaction forecasts.
- Product adoption curves or disclosed guidance.
- Price trends and compute/unit economics.
- Platform or channel growth.
- Capacity and regulation.

Explain step changes. If the base case departs materially from history, show the new causal mechanism.

## Sensitivities

In addition to three scenarios, expose the two variables with the largest impact. A useful sensitivity changes the underlying driver logic, not the final market output directly.

Typical pairs include paid rate vs ARPPU, adoption vs price, addressable units vs frequency, or leader share vs relevant-revenue allocation.

## Falsification indicators

List leading indicators that would invalidate the forecast, including demand growth, price compression, retention, conversion, usage intensity, unit economics, channel concentration, regulation, or substitute adoption. State the threshold and direction that would trigger a model update.
