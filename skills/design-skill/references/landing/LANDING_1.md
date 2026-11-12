# Style Design Guide - AMZ Marketer

This style design guide documents the key visual elements used in the interface, including the color palette, typography, button styles, and UI components.

---

## 1. Color Palette

This design uses a modern, clean color palette dominated by purple (for a professional & technology/AI feel) with a bright/soft background.

| Category | Color | Hex Code (Estimate) | Primary Usage |
| :--- | :--- | :--- | :--- |
| **Primary** | Dark Purple / Indigo | `#6C3EE8` or `#6366F1` | Primary button (CTA), main text header, accents |
| **Primary Light** | Light Purple / Lavender | `#F3E8FF` / `#EDE9FE` | Card backgrounds, badges, decorative accents |
| **Text Dark** | Charcoal Black / Dark Slate | `#1E1B4B` or `#0F172A` | Main headings, important text |
| **Text Muted** | Dark Gray | `#4B5563` or `#64748B` | Descriptions, subtext, navigation |
| **Background** | Clean White / Off-White | `#FFFFFF` / `#F8FAFC` | Main background (body background) |
| **Accent / Badge** | Pastel Purple / Soft Tint | `#E2E8F0` / Pastel variations | Borders, divider lines, stat cards |

---

## 2. Typography

The font is a modern, clean, geometric, easy-to-read **Sans-Serif** (similar to *Inter*, *Plus Jakarta Sans*, or *Poppins*).

* **Heading 1 (Hero Title):**
  * Size: Large, thick (*Bold / Extra Bold*).
  * Traits: Combines black text with purple on the key phrase (example: *"Grow Your E-commerce Business"*).
* **Heading 2 (Sub-heading / Section Title):**
  * Size: Medium-large, thick (*Semi-bold*).
  * Traits: Center-aligned or left-aligned with generous spacing.
* **Body Text (Paragraphs):**
  * Size: Standard (`14px` - `16px`), regular weight (*Regular*).
  * Color: Dark gray for comfortable readability.

---

## 3. UI Components & Elements

### A. Buttons
* **Primary Button (Filled):**
  * Background: Purple (`Primary`).
  * Text: White, thick (*Medium / Semi-bold*).
  * Corners: Smoothly rounded (*Rounded / Pill-shaped* or `border-radius: 8px - 9999px`).
  * Effect: Often includes an arrow icon (`→`) to the right of the text.
* **Secondary Button (Outlined / Ghost):**
  * Transparent background with a thin border, or direct text with an icon (example: the *"Watch Demo"* button with a Play icon inside a circle).

### B. Cards & Containers
* **Stats Cards & Feature Cards:**
  * Background: Clean white (`#FFFFFF`) on a light lavender background, or white cards with a soft drop shadow.
  * Corners: Rounded (`border-radius: 12px` to `24px`).
  * Card contents: Often include icons in small circular badges or boxes with a light purple background.

### C. Badges & Tags
* Used for category labels (example: *"AI-POWERED LEARNING FOR E-COMMERCE GROWTH"*).
* Very light purple background with dark purple text and fully rounded corners (*pill badge*).

---

## 4. Layout & Spacing

* **Grid & Alignment:** Uses a centered grid system with the main content area constrained (*max-width*) for a tidy look on large screens. The hero uses a two-column layout (text on the left, visuals & stats on the right).
* **Whitespace:** Generous vertical `padding` between sections for a clean, airy, elegant feel (*clean whitespace*).
* **Visual Accents:** Abstract hand-drawn line illustrations (thin curved lines/arrows) and star/sparkle icons to sweeten the AI aesthetic.

---

## 5. Responsive Behavior

*Follow the Tailwind breakpoint scale (mobile-first): `sm` ≥640px · `md` ≥768px · `lg` ≥1024px · `xl` ≥1280px.*

| Range | Hero | Navigation | Grids & sections |
|---|---|---|---|
| `xl` (≥1280px) | 2 columns, max-w-7xl container | Full | 3–4 columns, 96px section padding |
| `lg` (1024–1280px) | Tight 2 columns | Full | 3 columns |
| `md` (768–1024px) | Stacked (text → visual) | Hamburger + drawer | 2 columns, 64px padding |
| Base (<768px) | 1 column, full-width CTA | Hamburger | 1 column, 48px padding |

- Hero heading 48–56px (desktop) → 32–36px (mobile); section titles 32px → 24–28px.
- Stat cards go 3→1 columns; hand-drawn lines & sparkles hide below `sm` to avoid crowding.
- Newsletter form: input above the button under `md`; images locked to an aspect ratio so the layout doesn't jump on load.

---

## 6. Motion & Animation

| Token | Value | Used for |
|---|---|---|
| `--motion-fast` | `150ms` | Hover, focus |
| `--motion-base` | `250ms` | Drawer, dropdown, expand/collapse |
| `--motion-slow` | `400ms` | Hero entrance, scroll-reveal |
| `--ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | Default for all motion |
| `--ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | Symmetric motion |

`linear` is only for continuous motion (marquee, spinner).

- Animate only `transform` and `opacity`.
- Staged hero entrance: badge → title → sub → CTA (±80ms stagger, 400ms ease-out).
- One-time scroll-reveal per section (fade + 16px translate-y) at 15% visibility; don't repeat on scroll up/down.
- CTA hover: lift 2px + shadow; press `scale(0.98)`. Feature cards hover-lift; pill badge fades in with the hero.
- `prefers-reduced-motion`: show all content immediately; disable reveals and decorative motion.
