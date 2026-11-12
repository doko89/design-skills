# Style Design Guide - Freedom Funnels 3.0

This design style guide (*Design System*) summarizes all visual aesthetic preferences, the color palette, typography, and UI components based on the **Freedom Funnels 3.0** landing page interface.

---

## 1. Design Overview & Theme

* **Vibe / Tone:** Feminine, Professional, Elegant, Modern, & Empowering.
* **Target Audience:** Female entrepreneurs (*Female Entrepreneurs*).
* **Visual Traits:** All-rounded shapes (*soft rounded corners*), bright warm pastel colors, and a clean layout with generous whitespace.

---

## 2. Color Palette

The palette combines warm neutrals, pastel purple accents, soft pink, fresh mint, and dark contrast colors for high text readability.

| Category | Hex Code (Estimate) | Primary Usage |
| :--- | :--- | :--- |
| **Primary Accent (Purple/Lilac)** | `#8B70EE` / `#A084E8` | Highlight words, hero background accents, special badges. |
| **Dark Neutral (Text)** | `#111111` / `#1E1E1E` | Main headings, primary button text, high-contrast text elements. |
| **Secondary Neutral (Body)** | `#555555` / `#666666` | Paragraph descriptions, subtext, explanation details. |
| **Pastel Backgrounds:** | | |
| - *Soft Pink / Peach* | `#FDEEEB` / `#FEEAE6` | Special section/card backgrounds, floating "Latest Sale" card. |
| - *Soft Yellow / Butter* | `#FEF6D8` / `#FFF3CD` | "Freedom Score" and "Millions In Sales" highlight cards. |
| - *Soft Mint / Green* | `#D1F4E0` / `#E8F8F0` | Icon badges, "Thousands Of Women Transformed" card, footer banner. |
| - *Soft Lilac / Purple* | `#EBE4FF` / `#F0EAFF` | "100K+ Months" stat card, text highlight markers. |
| **Card / Base Canvas** | `#FFFFFF` | Primary background for card components, input fields, and main containers. |
| **Page Background** | `#FAFAFA` / `#F9F8FD` | Off-white with a hint of soft warm/lavender. |

---

## 3. Typography

Uses a smooth, elegant modern **Sans-Serif** typeface (such as *Plus Jakarta Sans*, *Outfit*, or *Inter*).

* **Display / Hero Title (Heading 1):**
  * **Size:** Extra Large (36px - 48px+).
  * **Weight:** Bold (700).
  * **Key Feature:** Emphasis (*highlight*) technique on specific words by switching the color to purple/lilac (examples: *"Without You."*, *"Automated Business"*).
* **Section Title (Heading 2):**
  * **Size:** Large (24px - 32px).
  * **Weight:** Bold (700) / Semi-Bold (600).
  * **Alignment:** Center for feature explanations, left for narrative sections.
* **Body Text (Paragraphs):**
  * **Size:** Medium (14px - 16px).
  * **Weight:** Regular (400) / Medium (500).
  * **Line Height:** Relaxed (1.6 - 1.8) for high readability.
* **Badges & Labels:**
  * **Size:** Small (12px - 13px).
  * **Weight:** Medium (500).
  * **Style:** Capitalized / Title Case with rounded padding.

---

## 4. UI Components & Elements

### A. Buttons
* **Primary Button (Dark Solid):**
  * Background: Charcoal black (`#111111`).
  * Text: White (`#FFFFFF`), with a right-arrow icon (`→`).
  * Shape: Pill-shaped (`border-radius: 9999px`).
* **Secondary / Outlined Button:**
  * Background: Transparent or white.
  * Border: Thin (`1px solid #E5E5E5`).
  * Effect: Includes a Play icon (`▷`) for demo/video buttons.
* **Badge Button (Pill Tag):**
  * Used at the very top of the hero (example: *"🌸 For Female Entrepreneurs"*).
  * Light pastel pink background with a subtle border.

### B. Cards & Floating Elements
* **Floating Stat Badges:**
  * Cards floating over the hero photo with a soft drop shadow.
  * High rounded corners (`border-radius: 16px - 20px`).
  * Include circular icons with mini icons inside (e.g., heart, wallet, chart icons).
* **Feature Grid Cards (Pastel Icons):**
  * Card background: Neutral white.
  * Border radius: `16px`.
  * Icons in colorful pastel circles (mint green, lilac, peach, yellow).
* **Course / Module Preview Cards:**
  * Card header is a real photo/screenshot of the app with rounded top corners.
  * Checkmark at the bottom-right corner as a verification/completion indicator.

---

## 5. Layout, Spacing & Visual Decor

* **Header / Social Proof Section:**
  * The endorsement section (As Seen In / Press Logos) uses neutral monochrome gray (*grayscale logos*) to stay subtle and not distract from the hero visual.
* **Border Radius System:**
  * Small: `8px` (small badges).
  * Medium: `16px` (module cards, feature cards).
  * Large: `24px - 32px` (hero image containers, footer banner).
  * Full Pill: `9999px` (primary buttons, badge tags).
* **Visual Decor & Accents:**
  * Thin pastel wave/underline accents under certain heading text.
  * Real product photos (laptop, iPhone, mug, pastel flowers) for a realistic *lifestyle* feel.

---

## 6. Responsive Behavior

*Follow the Tailwind breakpoint scale (mobile-first): `sm` ≥640px · `md` ≥768px · `lg` ≥1024px · `xl` ≥1280px.*

| Range | Hero | Navigation | Grids & sections |
|---|---|---|---|
| `xl` (≥1280px) | 2 columns, max-w-7xl container | Full | 3–4 columns, 96px section padding |
| `lg` (1024–1280px) | Tight 2 columns | Full | 3 columns |
| `md` (768–1024px) | Stacked (text → visual) | Hamburger + drawer | 2 columns, 64px padding |
| Base (<768px) | 1 column, full-width CTA | Hamburger | 1 column, 48px padding |

- Hero heading 48–56px (desktop) → 32–36px (mobile); section titles 32px → 24–28px.
- Floating elements (laptop/iPhone) move below the text under `lg`; module cards go 2→1 columns on mobile.
- Footer banner: product images stack to 1 column, full-width buttons below `md`.

---

## 7. Motion & Animation

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
- Floating elements: gentle ±8px float (6s ease-in-out, infinite); product photos scale-reveal once in 400ms.
- CTA hover: lift 2px + shadow; press `scale(0.98)`.
- `prefers-reduced-motion`: show all content immediately; disable float, reveals, and decorative motion.
