# Fixed-Rate Protocols

> **Ten ways to lock a borrowing rate on-chain – and the honest accounting of how little money is actually behind them.**

[![Live](https://img.shields.io/badge/live-fixedrateprotocol.com-C44A36.svg)](https://fixedrateprotocol.com/)
[![Pages](https://img.shields.io/badge/brief-13%20pages-1A1816.svg)](https://fixedrateprotocol.com/)
[![Data](https://img.shields.io/badge/data-verified%20Jun%202026-7A6E4F.svg)](#data--methodology)
[![Build](https://img.shields.io/badge/build-none%20·%20single%20file-blue.svg)](#how-its-built)

Almost every corner of DeFi lets the borrowing rate float. **Fixed-Rate Protocols** – published at [fixedrateprotocol.com](https://fixedrateprotocol.com/) under the *Rate.Lock* motif – is a landscape brief on the small set of teams trying to nail the rate down for a fixed term: the niche living beneath variable-rate giants like Aave and Morpho Blue. It walks ten core protocols page by page, routes one worked example (borrow 10 ETH for three months) through nine different rate-discovery mechanisms, and then does the thing most landscape decks skip – nets the TVL out and admits how small the field really is.

The conclusion is deliberately unflattering to its own subject. By net TVL the DeFi-native field is Wildcat (~$150M) and Liquity V2 (~$74M) and not much else, while the institutional RWA tier next door – tokenized Treasuries, Maple, Centrifuge – is roughly 50× bigger. The mechanisms are inventive; the demand has not shown up yet.

Written as an R3 landscape brief; published in case it saves anyone else the fortnight of protocol-doc archaeology.

---

## What's in it

A single scrolling deck of 13 numbered pages plus a closing panel:

- **Cover** – the field at a glance: ten mechanisms all now live, ~$300M combined, and the caveat that the RWA tier next door dwarfs it.
- **02 · Why the niche exists** – what fixed-rate and fixed-term actually mean, why borrowers want them (cash-flow planning, institutional mandates, hedging, structured products), and the three structural reasons the slice stays small: liquidity fragmentation across maturities, rollover risk, and capital-efficiency drag.
- **03 · Worked example** – *borrow 10 ETH for three months*, routed through nine native mechanisms side by side. The clearest single page for seeing how differently each protocol discovers a rate.
- **04 · Cross-cutting** – the field sliced five ways: rate discovery, collateral model, capital efficiency and leverage, flexibility vs. predictability, and maturity/scale.
- **05 · The comparison matrix** – all ten protocols against mechanism, fixed term, rate-setter, collateral/risk, status and TVL, and chains.
- **06–10 · Protocol deep-dives** – Morpho Midnight; Term Finance; the tokenized-bond family (TermMax, Fira, Secured Finance); rate-as-a-token and per-maturity pools (Inverse FiRM, Exactly); and the overlay/borrower-led group (IPOR, Wildcat, Liquity V2).
- **11–12 · The institutional / RWA frontier** – the ~$15B tokenized-Treasury market that functions as the on-chain risk-free benchmark, then the credit tier where real balance sheets sit (Maple, Centrifuge, Clearpool).
- **13 · Adjacent and wound down** – the neighbours and the graveyard: Notional, Yield Protocol, Element/DELV, Goldfinch, TrueFi, plus an explicit note on what was cut from the list and why.
- **Closing** – the honest take, and the open question: what finally brings the volume – a better mechanism, clearer regulation, or institutional distribution?

## The ten protocols

| Protocol | Rate discovered by | Status · net TVL (Jun 2026) |
|---|---|---|
| [Wildcat](https://wildcat.finance/) | Borrower decree, permissioned lenders | Live · **~$150M outstanding** |
| [Liquity V2](https://www.liquity.org/) | The borrower (rate sets redemption order) | Live · **~$74M** |
| [TermMax](https://ts.finance/) | AMM curve on tokenized bonds (FT/XT/GT) | Live · ~$33–49M |
| [Inverse · FiRM](https://www.inverse.finance/firm) | Market price of DBR borrowing rights | Live · ~$20M |
| [Term Finance](https://www.term.finance/) | Weekly sealed-bid auction, single clearing price | Live · ~$13M |
| [Fira](https://www.fira.money/) | Supply/demand on fixed-maturity bonds | Live · ~$5M net (large gross book) |
| [Exactly](https://exact.ly/) | Per-maturity pool utilization | Live · ~$3.8M |
| [Secured Finance](https://secured.finance/) | On-chain order book + Itayose auction | Live · ~$0.6M |
| [IPOR](https://ipor.io/) | Interest-rate swap AMM (overlay on Aave/Compound) | Live · IRS now legacy |
| [Morpho Midnight](https://morpho.org/) | Two-sided offers, no interest-rate model | Live 21 Jul 2026 · ~$1.9M *(Aug 2026)* |

## The headline findings

- **The field is two names.** Wildcat and Liquity V2 are most of it. Everything else is under ~$75M.
- **Fira's headline was doing the marketing.** A ~$425M gross loan book nets to roughly $5M of real on-chain value once the collateral it loops through itself is stripped out. Net TVL is the only honest cross-protocol ruler, so the brief ranks on it throughout.
- **Scale was never the survival trait.** Notional once topped ~$843M and still wound down after the November 2025 Balancer hack. Goldfinch – a16z-backed, once the flagship of undercollateralized RWA credit – passed GIP-87 unanimously in June 2026 and went into maintenance mode with GFI down ~99.8% from its 2022 high.
- **The money already moved next door.** ~$15B of tokenized Treasuries at a blended ~3.3% yield, with Circle's USYC having overtaken BlackRock's BUIDL as the largest single product, plus Maple (~$2.1B) and Centrifuge (~$1.63B) in institutional credit.
- **Rate discovery is the real taxonomy.** Auction, bond price, order book, a two-sided offer, a token you hold, pool utilization, a swap overlay, or simple borrower decree – mechanism choice is what actually separates these protocols, not branding.
- **The best-funded attempt launched into silence.** Morpho shipped Midnight on 21 July 2026 and it drew ~$1.9M. The mechanism was built properly by the largest team in on-chain lending, and the volume still did not appear – which is the cleanest evidence the brief has for its own thesis.

## How it's built

One file. `index.html`, ~68KB, 1,264 lines, 14 `<section>` blocks. No build step, no bundler, no dependencies to install, no JavaScript.

- **Type** – [Fraunces](https://fonts.google.com/specimen/Fraunces) for display and [Inter](https://fonts.google.com/specimen/Inter) for body, loaded from Google Fonts. These are the only external network requests the page makes.
- **Palette** – defined as CSS custom properties in `:root`: paper `#F2EBDD`, ink `#1A1816`, accent `#C44A36`, plus muted/rule/highlight/olive supporting tones. Change a value there and it propagates through the whole deck.
- **Favicon** – an inline `data:` URI SVG padlock (the Rate.Lock motif), so there is no icon file to keep in sync.
- **Responsive** – a single `@media (max-width: 900px)` breakpoint collapses the multi-column layouts and lets the wide matrix scroll horizontally inside its own container.

The same design system backs the sister brief at [trancheprotocol.com](https://trancheprotocol.com/).

## Run it locally

Nothing to install:

```bash
git clone https://github.com/mishablank/fixedrateprotocol.git
cd fixedrateprotocol
open index.html          # macOS – or just drag the file into any browser
```

If you want it served over HTTP (closer to production, and required if you add relative assets such as the social image):

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Deploy

The site is hosted on **Cloudflare Workers** with the static-assets integration, wired to this repository. Push to `main` and the live site rebuilds within seconds – there is no manual deploy step and no CI workflow in the repo.

[`.assetsignore`](.assetsignore) keeps `.git`, `.gitignore`, `.wrangler`, `.claude`, `wrangler.jsonc` and itself out of the uploaded asset bundle. Anything added to the repo that should not be publicly fetchable needs a line there. Note that the Worker configuration itself lives in the Cloudflare dashboard rather than a committed `wrangler.jsonc`.

## Editing conventions

- **En dashes, never em dashes.** Use `–` (or `&ndash;`) throughout. Three separate commits in this repo exist purely to undo em-dash regressions, so it is worth getting right the first time.
- **Every number carries an as-of date.** Figures are stamped in the page footer and in the source note under each table rather than floated as timeless facts.
- **Net, not gross.** When a protocol's headline TVL includes collateral it recycles through itself, the brief quotes the net figure and says so inline. Fira is the worked case.
- **Scope discipline is explicit.** Page 13 lists what was deliberately excluded and why – Pendle fixes *yield* rather than borrowing, Contango pivoted to variable-rate looping, Royco is an incentivized action market. Keep that list current when the scope is challenged.
- **Page numbering** is hardcoded in each section's `data-slide` attribute and footer. Inserting a page means renumbering both, in every section.

## Data & methodology

- **Sources** – [DefiLlama](https://defillama.com/) for TVL, [rwa.xyz](https://app.rwa.xyz/) for the tokenized-Treasury tier, and individual protocol documentation for mechanism detail.
- **As-of** – protocol figures verified **21 June 2026**; the page carries a revision note of **August 2026**.
- **Scope** – fixed-rate, *fixed-term borrowing*. Yield-fixing protocols, tranching chassis, and variable-rate loopers are covered only as adjacent context.

Because the underlying figures move continuously, treat every number here as a dated snapshot rather than a live feed.

## Known gaps

One thing a next revision should address:

1. **Social previews are broken.** `og:image` and `twitter:image` point at the relative filename `Fixed-rate-v4-og.png`, which is not in the repo and [404s in production](https://fixedrateprotocol.com/Fixed-rate-v4-og.png). Link unfurls on X, LinkedIn, Slack and iMessage need an absolute `https://fixedrateprotocol.com/…` URL and the actual image committed. A leftover `https://your-domain.com/…` placeholder also sits in an HTML comment. There is no `og:url` or `<link rel="canonical">` either.

Closed since this README was first written:

- ~~**Morpho Midnight is no longer pre-mainnet.**~~ Fixed 1 Aug 2026. Midnight launched publicly on **21 July 2026** – offer-based fixed-rate, fixed-term credit, cbBTC/USDC on Base across a limited set of maturities, ~$1.9M TVL. The cover headline, subtitle, matrix row and takeaway, worked example, both cross-cutting bullets, the deep-dive on page 06, the closing stat block and the OG/Twitter meta were all reframed, and the mechanism was corrected from *intent-based* (the pre-launch whitepaper design) to *offer-based* (what actually shipped).
- ~~**A stale cross-reference.**~~ Fixed 1 Aug 2026. Page 13 pointed at "pages 10–11" for the institutional/RWA tier; it now reads pages 11–12.

## Credits

Written by [Mike Blank](https://www.linkedin.com/in/mishablank/). Companion brief: [trancheprotocol.com](https://trancheprotocol.com/) – yield tranching protocols, eight chassis compared.

## License

No license file is currently present, so default copyright applies and all rights are reserved. If you want this to be reusable – quotable charts, forkable layout – add a `LICENSE` (MIT for the markup, or CC BY 4.0 if the intent is to license the research and prose).
