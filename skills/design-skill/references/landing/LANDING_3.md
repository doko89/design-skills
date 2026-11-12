# Style Design Guide - DigitalHub

This style design guide documents the key visual elements used in the interface, covering the color palette, typography, button styles, and supporting UI components.

---

## 1. Color Palette

This design uses a clean, bright professional color combination dominated by the dark blue/indigo typical of modern digital platforms, paired with soft pastel purple accents.

| Category | Color | Hex Code (Estimate) | Primary Usage |
| :--- | :--- | :--- | :--- |
| **Primary** | Indigo Blue / Dark Purple | `#4F46E5` or `#4338CA` | Primary button (CTA), highlighted text header, brand icon |
| **Primary Light** | Light Pastel Purple/Blue | `#EEF2FF` or `#F3E8FF` | Specific section backgrounds, category badges, decorative elements |
| **Text Dark** | Charcoal Black / Dark Slate | `#0F172A` or `#1E293B` | Main headings, important display text |
| **Text Muted** | Medium Gray | `#64748B` or `#4B5563` | Descriptions, subtext, navigation menu, product prices |
| **Background** | Clean White / Off-White | `#FFFFFF` / `#F8FAFC` | Main page background (body) |
| **Card Background** | White / Light Gray Border | `#FFFFFF` with a thin border (`#E2E8F0`) | Product cards (*Product Cards*), feature boxes |

---

## 2. Typography

The font is a modern **Sans-Serif** that is clean, geometric, and easy to read at all screen sizes (similar to *Inter* or *Plus Jakarta Sans*).

* **Heading 1 (Hero Title):**
  * Size: Large, thick (*Extra Bold*).
  * Traits: Combines black text with purple/indigo on key phrases (e.g., *"Digital Products That Inspire & Empower You"*).
* **Heading 2 & 3 (Sub-headings / Section Titles):**
  * Size: Medium to large, thick (*Semi-bold*).
  * Traits: Left or center aligned with generous spacing to keep sections clear.
* **Body Text (Descriptions / Products):**
  * Size: Standard (`14px` - `16px`), regular weight (*Regular*).
  * Color: Dark gray for comfortable readability.

---

## 3. UI Components & Elements

### A. Buttons
* **Primary Button (Filled):**
  * Background: Indigo blue / purple (`Primary`).
  * Text: Clean white, thick (*Medium*).
  * Corners: Smoothly rounded (`border-radius: 8px`).
  * Examples: the *"SHOP NOW"* and *"ADD TO CART"* buttons on product listings.
* **Secondary Button (Outlined):**
  * Transparent background with a thin indigo/purple border and matching text (example: the *"BROWSE CATEGORIES"* button).

### B. Cards & Product Grid
* **Product Card:**
  * Background: Clean white in a thin-bordered grid or with a soft shadow.
  * Corners: Rounded (`border-radius: 12px`).
  * Card contents: Digital product preview image/mockup, product title, star rating (with reviews), price, and an *"Add to Cart"* button at the bottom.

### C. Category Icons & Badges
* Product categories are represented by minimalist icons inside circles with soft pastel backgrounds (light purple, light green, light orange, etc.).
* Small purple/blue badges for special labels (example: *"NEW ARRIVALS"*).

---

## 4. Layout & Spacing

* **Grid & Alignment:** Uses a tidy, symmetric layout structure. The hero has two columns (text & CTA buttons on the left, device/laptop mockup visuals on the right).
* **Whitespace:** Generous vertical spacing between sections for a modern, airy, elegant aesthetic.
* **Footer & Trust Badges:** The bottom section includes accepted payment method icons (Visa, PayPal, etc.), quick navigation links, and a *newsletter* form with a soft purple box background.

---

## 5. Responsive Behavior

*Follow the Tailwind breakpoint scale (mobile-first): `sm` ≥640px · `md` ≥768px · `lg` ≥1024px · `xl` ≥1280px.*

| Range | Hero | Navigation | Grids & sections |
|---|---|---|---|
| `xl` (≥1280px) | 2 columns, max-w-7xl container | Full | 4-column product grid, 96px section padding |
| `lg` (1024–1280px) | Tight 2 columns | Full | 3-column product grid |
| `md` (768–1024px) | Stacked (text → visual) | Hamburger + drawer | 2-column product grid, 64px padding |
| Base (<768px) | 1 column, full-width CTA | Hamburger | 1–2 column product grid, 48px padding |

- Hero heading 48–56px (desktop) → 32–36px (mobile); section titles 32px → 24–28px.
- Category icons: horizontal scroll row on mobile; payment badges wrap neatly.
- Newsletter form: input above the button under `md`; laptop mockup scales down proportionally, never cropping information.

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
- Product card hover-lift + 1.03 image zoom (250ms); CTA press `scale(0.98)`.
- `prefers-reduced-motion`: show all content immediately; disable reveals and zoom.
