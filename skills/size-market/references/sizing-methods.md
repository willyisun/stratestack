# Sizing methods

## Selection tree

1. Decide whether demand is incremental, replacement, or hybrid.
2. Decide whether the measurable unit is people, businesses, devices, transactions, content/work units, sites, seats, or spend.
3. Decide which revenue boundary matters: category vendor revenue, customer spend, GMV, or value-chain revenue.
4. Choose methods with different error sources. Two versions of the same analyst report are not independent.

## Method A: demand or user bottom-up

Use distinct demand segments with different usage and willingness to pay.

`Market revenue = addressable units × active rate × paid rate × annual ARPPU`

For usage-priced products:

`Market revenue = addressable units × usage frequency × units per event × unit price`

Useful segments often include mass creators/consumers, professional creators or operators, commercial users tied to transactions, and specialist/professional users. Anchor each segment to relevant macro drivers such as population, business counts, device penetration, connectivity, platform activity, transaction volume, or professional employment.

Avoid counting the same person in multiple segments unless the model measures separate paid seats or separate jobs.

## Method B: replacement pool

Use when the technology primarily replaces an existing workflow or spend pool.

`Replaceable pool = current work units or spend × technically addressable share`

`New market = replaceable pool × adoption rate × new price per unit`

Separate:

- Theoretical replaceability.
- Economic willingness to switch.
- Actual adoption within the forecast period.
- Price decline or usage expansion caused by the new technology.

For hybrid demand, calculate replacement and incremental use cases separately, then deduct overlap.

## Method C: revenue aggregation

Add relevant category revenue across all important channels:

- Public-company reported segment revenue.
- Private companies and AI-native products.
- Mobile subscriptions and in-app purchases.
- Web subscriptions and usage-based revenue.
- Desktop/perpetual licenses.
- Services or offline revenue only if inside the market boundary.

Normalize company revenue for category mix, geography, fiscal period, gross/net presentation, and acquired businesses. Use third-party app and traffic data to estimate uncovered products, but avoid adding web traffic itself as revenue.

Show these fields for every company or component: source-period revenue, relevant-category share, overlap/geography adjustment, base-year conversion factor, Point revenue, Low coefficient, High coefficient, Low revenue, High revenue, source ID, conversion rationale, and range rationale.

Define the base-year conversion factor explicitly. A factor of `1.00` means the source is already a current-year guide, ARR, or run-rate. A factor above or below `1.00` bridges an older period, partial period, growth assumption, or normalization to the common model year.

Break material private-company, bundled-platform, and long-tail estimates into named components with separate editable values and rationales. A single unexplained residual is not acceptable.

## Method D: leader-share reverse check

`Implied market = leader relevant revenue ÷ leader category share`

Use multiple share definitions or a range. The leader's company-wide revenue is rarely the correct numerator. Share may refer to users, traffic, units, bookings, or revenue; match it to the numerator.

This method is a calibration check, not proof. A broad filing TAM claim and a narrow revenue share can create false precision.

## Method E: value-chain build

Map every monetized layer, for example creation/services, software, hosting/publishing, CDN/infrastructure, domain/identity, commerce management, payments, advertising, and ancillary services.

For each layer estimate:

`Layer pool = addressable units × penetration × spend per unit`

Then deduct pass-through, bundled revenue, and cross-layer overlap. Present both the full value-chain pool and the narrower category pool when useful; do not mix them in one headline.

Public companies spanning several layers can provide two checks: reported revenue and management's market estimate. Compare their implied share with observed market structure.

## Method F: stock-flow and macro envelope

Use population, businesses, devices, connected users, installed bases, time spent, transactions, sites, or professional employment to establish a physical ceiling.

Stocks constrain active installed bases; flows measure annual creation, replacement, or transactions. Do not multiply a stock by a monthly flow without an explicit frequency conversion.

Macro envelopes are best for sanity checks and for allocating demand by geography.

## Method G: external-report range

Collect multiple estimates and normalize definitions. Record publication date, base year, forecast period, included categories, and whether the number is revenue, spend, GMV, or economic value.

Use report ranges as orientation or calibration. Do not average incompatible reports.

## Bounds and uncertainty

Point is the most likely current estimate. Low and High are conservative and optimistic model boundaries, not statistical confidence intervals. Build Low/High from model drivers, not a blanket percentage when possible:

- Addressable units.
- Penetration or paid conversion.
- Usage/frequency.
- Price/ARPPU.
- Relevant-revenue allocation.
- Leader share.
- Overlap deduction.

Flag correlated inputs. If multiple methods reuse the same population, price, or company revenue, reduce their combined reconciliation weight.

When driver-level bounds are unavailable, show the Low/High coefficient beside the row and explain whether it reflects source reliability, age, definition mismatch, coverage gaps, target-versus-actual risk, or private-company opacity.

## Reconciliation score

Score each method from 1 to 5 on:

- Definition match.
- Coverage.
- Source quality and recency.
- Independence.
- Assumption intensity, reverse scored.

Use the score to inform—not mechanically dictate—weights. Weights must total 100%. Explain any method below 10% or above 40%.

Investigate any estimate outside half to twice the weighted midpoint before finalizing.
