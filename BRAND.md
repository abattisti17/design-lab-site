# Design Lab brand and design system

Version 0.2, "Drawing set", October 2026. Living reference: `designlab_html/styleguide/` (not linked from the site, `noindex`).

## The one rule

Pages use the tokens in `designlab_html/css/site.css`. Never write raw hex values, font names or pixel spacing into a page. If a token is missing, add it to `site.css` and the style guide first.

`css/styles.css` is the old Bootstrap theme. Leave it alone; `site.css` loads after it and overrides what matters.

## Direction

Borrowed from architects' own drawings: black linework on white, hatching for what's used, dimension strings for amounts, a redline revision cloud for what's wrong, trace paper for what's still being worked out, and a title block at the foot of every page. The audience reads drawings all day, so the page speaks their visual language.

Spend boldness in one place: the fee drawing at the top of the architecture page, set on its own drawing sheet (grid paper, double-line border, title block) so it reads as a separate object. Everything else stays quiet.

## Color

- `--paper #FFFFFF` page
- `--ink #000000` text, linework, buttons (21:1)
- `--pencil #5B6169` secondary text and captions (6.3:1)
- `--line-light #D4D4D4` minor rules
- `--trace #FFF6C2` the founding offer only
- `--redline #C8201A` over budget and markup only (5.7:1)

## Type

- Archivo variable, self-hosted in `assets/fonts/` (SIL OFL). No third-party font requests.
- Headlines: 118% width (`--wide`), weight 650 to 700, tight tracking.
- Body: normal width, weight 400, 18px, line height 1.55.
- Scale: 14, 16, 18, 22, 30, 40, 60px (`--text-xs` to `--text-3xl`).
- Sentence case everywhere, including buttons. Tabular figures by default.

## Shape and space

- Radius 2px on buttons and the trace sheet, nothing else.
- Lines are 1px black (`--line`). Hatching: `--hatch` (black) and `--hatch-red`.
- Spacing: 4px base. Steps 4, 8, 12, 16, 24, 32, 48, 72, 112.
- Reading width: 36rem (`--measure`).

## Components

In `site.css`, shown in the style guide: `.site-header`, `.wordmark`, `.btn` (`.btn-primary`, `.btn-outline`, `.btn-sm`), `.cta`, the fee drawing (`.drawing`, `.fee-run`, `.phase`, `.dim`, `.bar`, `.used`, `.over`, `.cloud`, `.markup`, `.legend`), `.problems`, `.steps`, `.trace`, `.terms`, `.founder`, `.prose`, `.title-block`.

## Voice

- Plain, specific, short sentences, in the buyer's words (fees, phases, billing day).
- Say what it does and what it costs. No hype.
- No em dashes. No "it's X, not Y" constructions. No clever closing lines.

## What we don't do

These are the defaults of generated sites:

- Cream backgrounds, serif display headlines, purple or clay accents
- All-caps labels above headings, monospace data labels, arrows on links, middle-dot meta strings
- Rounded cards with soft shadows, gradient washes, icon-in-a-circle bullets
- Fake browser chrome around product shots

## Identity

- Wordmark: "Design Lab" in Archivo at 125% width, weight 750. Placeholder until the product has its own name.
- Favicon: white "DL" on a black square (`assets/favicon.svg`, PNG and ICO fallbacks).
