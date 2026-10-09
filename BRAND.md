# Design Lab brand and design system

Version 0.1, October 2026. Living reference: `designlab_html/styleguide/` (not linked from the site, `noindex`).

## The one rule

Pages use the tokens in `designlab_html/css/site.css`. Never write raw hex values, font names or pixel spacing into a page. If a token is missing, add it to `site.css` and the style guide first.

`css/styles.css` is the old Bootstrap theme. Leave it alone; `site.css` loads after it and overrides what matters.

## Direction

A drawing set, not a creative agency. Warm paper, near-black ink, thin hairlines, a strict grid, small uppercase labels like a title block, tabular numbers. Calm and precise. No stock photos, gradients, drop shadows or pill buttons.

## Color

All contrast ratios are against Paper.

- `--paper #FAFAF7` page background
- `--surface #FFFFFF` cards and raised areas
- `--ink #17181C` body text and headings (17.0:1)
- `--graphite #4F5560` secondary text, labels, captions (7.2:1)
- `--rule #E4E4DE` hairlines, borders, dividers
- `--brand #1F0046` buttons, links, focus rings, active states (17.5:1)
- `--brand-tint #F1EEF6` selected and highlighted backgrounds
- `--over #B42318` over budget, errors (6.3:1)
- `--paid #15803D` paid, complete (4.8:1; icons and bold labels, not long text)

Brand is the only accent. Over and Paid carry meaning and are used only for that meaning.

Alternative being considered: swap `--brand` to blueprint blue `#1D4ED8` (6.4:1). It's a one-line change.

## Type

- IBM Plex Serif 500: H1 and H2 only
- IBM Plex Sans 400, 500, 600: everything else
- Scale: 14, 16, 18, 22, 28, 36, 48px (`--text-xs` to `--text-3xl`)
- Body 18px, line height 1.6. Headings line height 1.2.
- Use `.num` (tabular figures) wherever amounts stack in a column.
- Load both families from Google Fonts with exactly these weights on every page.

## Space and shape

- Spacing: 4px base. Steps 4, 8, 12, 16, 24, 32, 48, 64, 96 (`--space-1` to `--space-9`).
- Radius: 6px controls (`--radius-control`), 10px cards (`--radius-card`).
- Borders: 1px hairline in Rule. No shadows.
- Reading width: 40rem (`--measure`).

## Components

Defined in `site.css`, shown in the style guide: `.site-header`, `.wordmark`, `.eyebrow`, `.btn` (`.btn-primary`, `.btn-outline`, `.btn-sm`), `.card-dl`, `.pain-list`, `.check-list`, `.steps`, `.offer`, `.founder`, `.mock` (product mockup), `.tag`, `.site-footer`.

## Voice

- Plain, specific, short sentences.
- Use the buyer's words (fees, phases, billing day), not ours.
- Say what it does and what it costs. No hype words.
- No em dashes. No "it's X, not Y" constructions. No clever closing lines.
- Sentence case for headings and buttons.

## Identity

- Wordmark: lowercase "design lab" in Plex Sans 600, Ink. Placeholder until the product has its own name.
- Favicon: "dl" in Paper on a Brand rounded square (`assets/favicon.svg`, PNG and ICO fallbacks).
