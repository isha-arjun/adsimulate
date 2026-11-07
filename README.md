# AdSimulate

**Advertising Decision Intelligence** — understand the creative, simulate the economics, and make a more informed campaign decision.

## MVP (0.1)

This first API-key-free MVP includes:

- Campaign economics inputs: product price, unit cost, variable order costs, ad spend, CPM, CTR and click-to-purchase rate.
- Deterministic scenario calculations: impressions, clicks, estimated orders, revenue, contribution after variable costs and ad spend, break-even orders, CAC, ROAS and ROI.
- Transparent copy diagnostics: rule-based checks for benefit language, credibility cues, action clarity, audience relevance, scan length and sentence rhythm.
- Clear disclosure that modeled figures are assumption-driven, not measured outcomes or validated performance predictions.

## Run locally

```bash
npm install
npm run dev
```

Open http://localhost:3000.

## Important modelling notes

The financial simulator is deterministic arithmetic based on inputs supplied by the user. It does not forecast real campaign performance. Use historical account averages where possible and treat all unverified inputs as planning assumptions.

Creative diagnostics only inspect visible text patterns. They do not measure attention, emotion, persuasion, subconscious response or consumer behaviour.

Current exclusions: authentication, persistent database storage, team collaboration, AI API integration, platform ad-account integrations, and calibrated predictive modelling.

## Stack

- Next.js 14 / React / TypeScript
- Client-side deterministic calculations
- No AI API keys required
