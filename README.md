# StrateStack

Reusable strategy skills for AI agents.

## Size Market

`size-market` researches and calculates an auditable market size from a short business description plus current users and/or annualized revenue.

It produces a formula-linked Excel workbook covering:

- TAM, SAM, SOM, and current revenue/user share
- market structure, demand modules, and competition
- multiple independent sizing methods and reconciliation
- source facts separated from editable assumptions
- conservative, base, and aggressive three-year scenarios
- growth drivers, structural change, key success factors, and model limitations

### Install

Download [size-market-v2.zip](https://github.com/willyisun/stratestack/releases/download/v2.0.0/size-market-v2.zip), unzip it, and install the resulting `size-market/` folder in the skills directory supported by your Agent product.

You can also install from source by copying [`skills/size-market/`](skills/size-market/) into the relevant skills directory.

### Example

> Use $size-market to estimate the market size for my business. We provide a cross-platform creative tool, currently with 10 million monthly active users and US$30 million in annualized revenue.

The business description and current user and/or revenue scale are sufficient. The skill researches geography, comparable companies, filings, macro drivers, pricing, adoption, and market structure.

### Requirements

The Agent should have:

- internet or browser access for current research
- spreadsheet/XLSX creation and editing capability
- enough execution time for source collection and model reconciliation

## Repository layout

```text
skills/
└── size-market/
    ├── SKILL.md
    ├── agents/
    ├── assets/
    ├── references/
    └── scripts/
```

## Version

Current release: `v2.0.0`
