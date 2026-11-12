# Style Design Guide - ClassiAds

This style design guide documents the key visual elements used in the interface, covering the color palette, typography, button styles, and UI components with a modern 3D/glassmorphism touch.

---

## 1. Color Palette

This design uses a clean white background paired with bright blue accents and pastel gradient elements (purple, light blue, and orange) for a modern, friendly, dynamic feel.

| Category | Color | Hex Code (Estimate) | Primary Usage |
| :--- | :--- | :--- | :--- |
| **Primary** | Bright Blue / Cobalt | `#2563EB` or `#3B82F6` | Primary button (Search CTA), icon accents, important links |
| **Primary Light** | Soft Light Blue / Lavender | `#DBEAFE` / `#EEF2FF` | Search box background, category badges, decorative elements |
| **Text Dark** | Charcoal Black / Slate | `#0F172A` or `#1E293B` | Main headings, ad names, important text |
| **Text Muted** | Medium Gray | `#64748B` or `#94A3B8` | Subtext, category descriptions, prices, navigation buttons |
| **Background** | Clean White / Ice White | `#FFFFFF` / `#F8FAFC` | Main page background (body background) |
| **Card & Accent** | White with Glass/Shadow | Glassmorphism variations | Ad card boxes (*Featured Ads*), floating 3D elements |

---

## 2. Typography

The font is a modern **Sans-Serif** that is clean, geometric, and highly readable (*readability*) at all screen sizes.

* **Heading 1 (Hero Title):**
  * Size: Large, thick (*Bold / Extra Bold*).
  * Traits: Prominent headline text welcoming users (example: *"Busing Ciallewrădeds"*).
* **Heading 2 & 3 (Sub-headings / Section Titles):**
  * Size: Medium to large, thick (*Semi-bold*).
  * Traits: Left-aligned with generous spacing to clarify section separation (e.g., *"Featured Ads"*).
* **Body Text & Metadata (Descriptions / Cards):**
  * Size: Standard (`12px` - `14px`), regular to *medium*.
  * Color: Dark to light gray to distinguish product titles from supporting info (such as star ratings or location).

---

## 3. UI Components & Elements

### A. Search & Input Fields
* **Search Bar:**
  * Background: Clean white with elongated rounded corners (*pill-shaped* / `border-radius: 9999px`) or a thin-bordered box with a soft shadow.
  * Includes a bright blue search action button at its end.

### B. Buttons
* **Primary Button (Filled):**
  * Background: Bright blue (`#3B82F6`).
  * Text: Clean white, thick (*Medium*).
  * Corners: Smoothly rounded (`border-radius: 8px` to `12px`).
* **Ghost / Outlined Button:**
  * Top navigation buttons with an elegant transparent or thin white background.

### C. Cards & Grid (Ad Cards / Featured Ads)
* **Product / Ad Card:**
  * Background: Clean white with a thin border and a soft drop shadow for a *floating* feel.
  * Corners: Rounded (`border-radius: 12px` - `16px`).
  * Card contents: Product/vehicle preview image, status label ("New"), ad title, star rating indicator, and a quick action button.

### D. 3D & Floating Accents
* The page is decorated with clay/glassmorphic-style 3D graphics (such as a tilted phone icon, transparent colorful bubbles) for a modern, interactive, aesthetic feel.

---

## 4. Layout & Spacing

* **Grid & Alignment:** Uses a tidy modular grid-based layout to display ad listings in an orderly way (4 columns for product/ad items).
* **Whitespace:** Loose vertical and horizontal spacing for a clean, airy, well-organized feel.

---

## 5. Responsive Behavior

*Follow the Tailwind breakpoint scale (mobile-first): `sm` ≥640px · `md` ≥768px · `lg` ≥1024px · `xl` ≥1280px.*

| Range | Hero / search | Navigation | Ad grid |
|---|---|---|---|
| `xl` (≥1280px) | Full search bar + side filters | Full | 4 columns, 96px section padding |
| `lg` (1024–1280px) | Full search | Full | 3–4 columns |
| `md` (768–1024px) | Full-width search, filters become drawer/chips | Hamburger + drawer | 2 columns, 64px padding |
| Base (<768px) | Search + full-width button | Hamburger | 1–2 columns, 48px padding |

- Hero heading 40–48px (desktop) → 28–32px (mobile); ad prices/info must never clip in narrow cards.
- Search column full-width on mobile with the search button attached; filters become a horizontal scrolling chip row.
- 3D accents & floating elements hide below `sm` to keep focus on the ad listings.

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
- Staged hero entrance: badge → title → search (±80ms stagger, 400ms ease-out).
- Search results: 40ms fade-in stagger per card when filters change; skeleton while loading.
- Ad card hover-lift + 1.03 image zoom (250ms); favorite button color transition 150ms.
- `prefers-reduced-motion`: show all content immediately; disable reveals and zoom.
