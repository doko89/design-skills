# Cobalt Analytics Dashboard — Style Guide

> **Theme name:** Cobalt Analytics Dashboard  
> **Reference:** Dashboard UI shown inside the tablet mockup supplied by the user  
> **Format:** Desktop/tablet analytics dashboard  
> **Design direction:** Clean, modern, data-centric, bright, and blue-led

## 1. Design principles

- **Blue is the primary identity.** Use saturated cobalt blue for navigation, primary actions, selected states, and key data series.
- **Keep the workspace light.** Use a very pale blue-gray application canvas and white cards so charts and metrics remain easy to scan.
- **Use teal as a secondary data color.** Teal distinguishes a second series or a positive/secondary metric without competing with the primary blue.
- **Favor clear grouping.** Separate the persistent navigation, global header, and dashboard content into distinct regions.
- **Use restrained elevation.** Cards should feel lightly raised rather than heavily outlined or dramatically shadowed.

The tablet bezel and vivid blue background are part of the presentation mockup, not part of the dashboard UI theme. Do not apply those elements to the application itself.

## 2. Color palette

The values below are **visual estimates sampled from the supplied raster image**. Treat them as starting design tokens; refine them against the original design source if exact brand values become available.

| Token | Approx. HEX | Intended use |
|---|---:|---|
| `color.primary` | `#2872EF` | Primary buttons, active navigation accents, primary chart series |
| `color.primary-hover` | `#1F63D8` | Hover/pressed primary controls |
| `color.primary-dark` | `#174FAF` | Dark blue chart line, emphasis, selected icon details |
| `color.sidebar` | `#2D73E9` | Sidebar base; may use a subtle vertical blue gradient |
| `color.teal` | `#20BEC8` | Secondary chart series, secondary highlights |
| `color.canvas` | `#EDF1F9` | Main application background |
| `color.surface` | `#FFFFFF` | Cards, header, active navigation item |
| `color.surface-muted` | `#F5F7FB` | Search field and muted control surfaces |
| `color.text` | `#171B25` | Main headings and primary labels |
| `color.text-secondary` | `#6F7888` | Supporting labels, captions, metadata |
| `color.text-on-primary` | `#FFFFFF` | Text and icons on blue surfaces |
| `color.border` | `#DCE2EB` | Card outlines, input borders, separators |
| `color.gridline` | `#D9DEE8` | Chart gridlines and subtle dividers |
| `color.track` | `#E2E7EF` | Progress tracks and inactive chart segments |
| `color.success` | `#20B8A8` | Optional positive status; use sparingly |
| `color.warning` | `#E8AE3B` | Warning/status indicator; not a dominant theme color |

### Color usage rules

1. Reserve saturated blue for actions, active states, and the most important data series.
2. Use teal as a supporting accent, not as a second primary brand color.
3. Keep most surfaces white or pale blue-gray. Avoid large areas of dark backgrounds.
4. Use dark text on white surfaces and white text on saturated blue surfaces.
5. Do not use color alone to communicate status; pair it with a label, icon, or other visual cue.
6. Maintain sufficient text contrast, especially for small secondary labels.

## 3. Typography

The reference uses a modern sans-serif UI style. The exact font cannot be identified reliably from the image.

### Recommended font stack

```css
font-family:
  Inter,
  ui-sans-serif,
  system-ui,
  -apple-system,
  BlinkMacSystemFont,
  "Segoe UI",
  sans-serif;
```

### Type scale

| Role | Suggested size | Weight | Typical use |
|---|---:|---:|---|
| Page title | 20–22px | 600 | Main page heading |
| Card title | 17–19px | 600 | “Analytics”, “Summary”, “Details” |
| Metric value | 20–24px | 600 | Currency, percentages, KPI values |
| Body / navigation | 14–15px | 400–500 | Navigation labels and control text |
| Supporting label | 12–13px | 400 | Field names, chart labels, metadata |
| Micro label | 10–11px | 400 | Dense chart annotations only |

### Typography rules

- Use sentence case for headings and navigation.
- Keep headings compact; avoid oversized marketing-style typography.
- Use tabular numerals for financial values, metrics, and chart axes where supported.
- Use medium or semibold weights for titles and important values.
- Use muted gray for secondary text, but do not reduce small text to an unreadable contrast level.

## 4. Layout and composition

### Application shell

The screen is organized into three persistent regions:

1. **Left sidebar:** fixed-width navigation with a blue background.
2. **Top header:** white horizontal bar containing the menu toggle, search, notifications, and user profile.
3. **Main workspace:** pale blue-gray canvas containing a dashboard title and modular cards.

### Reference proportions

These are approximate proportions from the image, not mandatory pixel dimensions:

- Sidebar: about 19–20% of the application width.
- Header: about 60–64px high.
- Main content: remaining width, with approximately 24–28px of inner padding.
- Dashboard top row: a wide analytics card (roughly two-thirds) and a narrower donut-chart card (roughly one-third).
- Dashboard lower row: three cards arranged in columns, with consistent gaps.

### Spacing scale

Use a consistent 4px-based spacing system.

| Token | Value | Use |
|---|---:|---|
| `space.1` | 4px | Tight icon/label gap |
| `space.2` | 8px | Compact control spacing |
| `space.3` | 12px | Internal card spacing |
| `space.4` | 16px | Standard component spacing |
| `space.5` | 20px | Card content spacing |
| `space.6` | 24px | Main layout gap |
| `space.8` | 32px | Large section separation |
| `space.10` | 40px | Major layout separation |

### Layout rules

- Align card edges to a shared grid.
- Use consistent horizontal and vertical gaps between cards.
- Keep the analytics chart visually dominant.
- Allow cards to stack on narrow screens; do not compress chart labels until they become illegible.
- On smaller viewports, collapse the sidebar into a drawer or compact navigation rail.

## 5. Navigation and header

### Sidebar

- Use a saturated cobalt-blue background.
- Place the product mark and product name at the top.
- Use white or softly tinted icons and labels for inactive navigation.
- Highlight the active item with a white rounded rectangle, blue icon, and dark blue label.
- Indent nested navigation items beneath their parent section.
- Keep icon size consistent (approximately 18–20px).

### Header

- Use a white surface with a subtle bottom divider.
- Place the menu toggle at the left edge of the workspace.
- Use a centered or flexible search field with a pale neutral fill and rounded corners.
- Group notification icons and the user avatar/profile menu at the right.
- Keep header controls visually quiet; avoid competing with the dashboard content.

## 6. Cards and surfaces

| Property | Recommendation |
|---|---|
| Background | `#FFFFFF` |
| Border | `1px solid #E4E8EF` or a very subtle border |
| Corner radius | 10–12px |
| Shadow | Soft, low-opacity shadow |
| Internal padding | 20–24px |
| Card title spacing | 12–16px below title |
| Card-to-card gap | 16–20px |

Suggested shadow:

```css
box-shadow: 0 3px 14px rgba(24, 48, 86, 0.07);
```

Cards should have consistent radii and elevation. Avoid thick borders, strong gradients, and deep shadows.

## 7. Components

### Buttons

**Primary button**
- Background: `#2872EF`
- Text: white
- Radius: 6–8px
- Height: approximately 36–40px
- Weight: 500–600
- Hover: slightly darker blue
- Focus: visible blue focus ring

**Secondary button**
- White or muted surface
- Border: `#DCE2EB`
- Text: dark neutral
- Same height and radius as the primary button

### Inputs and selects

- White background, thin neutral border, 6–8px radius.
- Use 12–14px labels and 14–15px input text.
- Keep dropdown chevrons and search icons aligned consistently.
- Provide a visible focus state; do not rely only on a subtle color shift.
- Disabled controls should use a muted surface and readable disabled text.

### Metric fields

- Place the label above the value.
- Use a semibold, larger numeric value.
- Add a small progress indicator only when it conveys meaningful information.
- Keep units and supporting metadata visually secondary.

### Icons and avatars

- Use a consistent outline icon family.
- Prefer 18–20px icons for navigation and header actions.
- Use blue for active or emphasized icons; use muted gray for inactive utility icons.
- Keep avatar treatment circular and aligned with the header control baseline.

## 8. Data visualization

The dashboard uses line, donut, and vertical bar charts.

### Line chart

- Primary series: cobalt blue (`#1F63D8` or `#2872EF`).
- Secondary series: teal (`#20BEC8`).
- Use thin, low-contrast horizontal gridlines.
- Keep axis labels small and muted.
- Use smooth curves only if the underlying data presentation supports them.
- If using area fills, apply a very low-opacity tint beneath the line.
- Highlight a selected point with a clear marker and a compact tooltip.

### Donut chart

- Use blue as the dominant segment, teal as a secondary segment, and a pale neutral for the remaining segment.
- Keep the center open for a percentage or summary value.
- Make the center value the visual focus; supporting text should be smaller and muted.
- Provide a legend or accessible text equivalent when segment meaning is not obvious.

### Bar chart

- Use cobalt blue for the main bars.
- Use teal selectively to highlight a category or comparison.
- Keep bar widths and spacing consistent.
- Use a pale neutral gridline or baseline.
- Axis labels should remain legible and should not compete with the data.

### Chart accessibility

- Do not communicate series identity by color alone; add labels or legends.
- Provide accessible names or a data table for important chart information.
- Ensure tooltip text has sufficient contrast and can be accessed without hover where applicable.

## 9. Borders, radii, and elevation tokens

```css
:root {
  --radius-sm: 6px;
  --radius-md: 8px;
  --radius-card: 12px;
  --radius-pill: 999px;

  --border-width: 1px;
  --border-color: #DCE2EB;

  --shadow-card: 0 3px 14px rgba(24, 48, 86, 0.07);
  --shadow-popover: 0 8px 24px rgba(24, 48, 86, 0.14);
}
```

Use pill radii only for compact badges or progress indicators. Buttons and cards should retain modest rounded corners.

## 10. Design tokens — CSS starter

```css
:root {
  /* Brand */
  --color-primary: #2872EF;
  --color-primary-hover: #1F63D8;
  --color-primary-dark: #174FAF;
  --color-sidebar: #2D73E9;
  --color-teal: #20BEC8;

  /* Surfaces */
  --color-canvas: #EDF1F9;
  --color-surface: #FFFFFF;
  --color-surface-muted: #F5F7FB;

  /* Text */
  --color-text: #171B25;
  --color-text-secondary: #6F7888;
  --color-text-on-primary: #FFFFFF;

  /* Lines and status */
  --color-border: #DCE2EB;
  --color-gridline: #D9DEE8;
  --color-track: #E2E7EF;
  --color-success: #20B8A8;
  --color-warning: #E8AE3B;

  /* Typography */
  --font-family-ui: Inter, ui-sans-serif, system-ui, sans-serif;
  --font-size-xs: 0.75rem;
  --font-size-sm: 0.875rem;
  --font-size-md: 1rem;
  --font-size-lg: 1.125rem;
  --font-size-xl: 1.375rem;

  /* Spacing */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;

  /* Shape and elevation */
  --radius-sm: 6px;
  --radius-md: 8px;
  --radius-card: 12px;
  --shadow-card: 0 3px 14px rgba(24, 48, 86, 0.07);
}
```

## 11. Responsive behavior

Follow the Tailwind breakpoint scale (mobile-first): `sm` ≥640px · `md` ≥768px · `lg` ≥1024px · `xl` ≥1280px.

| Range | Sidebar & nav | Card grid | Tables & charts |
|---|---|---|---|
| `xl` (≥1280px) | Full sidebar (~19–20% width) | Wide analytics + donut row, 3 cards below | Full tables, side-by-side charts |
| `lg` (1024–1280px) | Sidebar ~200px | Same rows, tighter gaps | Full tables, 20px card padding |
| `md` (768–1024px) | Drawer (hamburger) or 72px icon rail | 1–2 columns, lower cards wrap | Tables scroll-x with sticky first column |
| Base (<768px) | Drawer / bottom nav | Single stacked column | Full-width charts, condensed axis labels |

- Never hide the primary action on small screens; move it into the compact header or a floating button.
- The line, donut, and bar charts always resize with their containers; keep legends readable and never truncate them.
- Card padding: 24–28px (desktop) → 16px (mobile); metric values 20–24px → 18–20px.
- Minimum touch target 44px; collapse the full search field into an icon below `md`.

## 12. Motion & animation

| Token | Value | Use for |
|---|---|---|
| `--motion-fast` | `150ms` | Hover, focus, tooltips |
| `--motion-base` | `250ms` | Drawer, dropdowns, expand/collapse |
| `--motion-slow` | `400ms` | Card entrances, chart animation |
| `--ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | Default for all motion |
| `--ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | Symmetric motion (toggles, progress) |

Use `linear` only for continuous motion (spinners, skeleton shimmer).

- Animate `transform` and `opacity` only, so motion stays at 60fps.
- Card and button hover: lift 2–4px with a soft shadow over 150ms; press: `scale(0.98)`.
- Entrance: fade plus `translate-y(8–12px)` with a 40–60ms stagger between cards; KPI numbers count up over 400–600ms.
- Drawer: 250ms ease-out slide with an overlay fade; tooltips fade in over 150ms.
- Loading: skeleton shimmer (1200ms loop); spinners only inside action buttons.
- `prefers-reduced-motion`: disable entrances, shimmer, and count-ups; render the final state immediately.
- Animate the primary blue series first, then teal; keep the donut's segment proportions exact during animation.

## 13. Do / Don't

### Do

- Use cobalt blue for primary actions and active navigation.
- Use teal to distinguish secondary data.
- Keep the workspace light and cards white.
- Maintain consistent card radii, spacing, and icon sizing.
- Use restrained shadows and clear typographic hierarchy.
- Preserve chart labels, legends, and accessible descriptions.

### Don't

- Do not use the bright blue tablet backdrop as the application canvas.
- Do not turn every component blue; reserve blue for hierarchy and emphasis.
- Do not use heavy shadows, thick borders, or excessive gradients.
- Do not make secondary labels so pale that they become unreadable.
- Do not introduce unrelated accent colors without a clear semantic purpose.
- Do not treat the distorted text in the reference image as authoritative product copy.

## 14. Reference interpretation and confidence

The reference is a rasterized dashboard mockup with some small text that is blurred or visually distorted. The overall structure, color relationships, card treatment, and chart styles are clear; exact font family, brand color values, spacing measurements, and component dimensions are not.

Accordingly:
- HEX values and measurements in this guide are **approximate visual matches**, not verified source design tokens.
- The suggested font stack is a practical implementation choice, not a confirmed identification of the original font.
- Use the guide to reproduce the visual language and hierarchy, not to reproduce illegible labels verbatim.
