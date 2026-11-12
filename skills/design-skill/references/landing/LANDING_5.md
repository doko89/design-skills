# Style Design System - Travel Agency Landing Page

This document defines the design style guide (*design system*) for a tourism or travel agency (*Travel Agency*) website UI, inspired by a clean layout, origami/paper aesthetics, and a modern color blend.

---

## 1. Colors (Color Palette)

The palette is dominated by bright sky blue for a professional, fresh, spacious, friendly travel-industry feel, paired with clean white accents and subtle gradients.

| Category | Color Name | Hex Value / Code | Primary Usage |
| :--- | :--- | :--- | :--- |
| **Primary** | Sky Blue | `#1A82FF` (Estimate) / Bright Blue | Primary button (*CTA*), active icons, important navigation elements. |
| **Secondary** | Deep Navy / Slate | `#0F172A` / `#1E293B` | Primary text, headings, and high-contrast elements. |
| **Background** | Ice White / Light Blue Tint | `#F0F6FF` / `#F8FAFC` | Overall page background (*body background*). |
| **Surface / Card** | Pure White | `#FFFFFF` | Card (*cards*), search container (*search bar*), and modal panel backgrounds. |
| **Accent / Highlight** | Soft Gold / Yellow | `#F59E0B` | Star rating labels, popular badges, and highlight (*badge*) elements. |
| **Text Muted** | Slate Gray | `#64748B` | Sub-text, secondary descriptions, and input labels. |

---

## 2. Typography

Uses a modern sans-serif typeface that is clean, geometric, and highly readable (*readable*) at all screen sizes.

*   **Primary Font Family:** Inter, Plus Jakarta Sans, or Poppins.
*   **Text Hierarchy:**
    *   **Hero Heading (H1):** 36px – 48px, Bold (`700`), contrasting white/navy.
    *   **Section Heading (H2):** 24px – 28px, Semi-Bold (`600`).
    *   **Card Title (H3):** 16px – 18px, Medium / Semi-Bold (`500` / `600`).
    *   **Body Text:** 14px, Regular (`400`), secondary text color (`#64748B`).
    *   **Button & Navigation:** 14px, Medium (`500`).

---

## 3. UI Components & Visual Elements (UI Components)

### A. Cards & Containers (*Cards & Containers*)
*   **Border Radius:** Smoothly rounded corners (*rounded corners*), ranging from `16px` to `24px` (`rounded-2xl`).
*   **Shadows:** A *soft drop shadow* for a *floating effect*, e.g., `box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);`.
*   **Glassmorphism / Transparency:** Light transparency with *backdrop blur* on some navigation or search panel sections.

### B. Buttons (*Buttons*)
*   **Primary Button:** Bright blue (`#1A82FF`) with rounded corners (`rounded-full` or `rounded-xl`), white text, and a *hover* effect that slightly brightens or lifts the button.
*   **Secondary / Outline Button:** Transparent or white background with a thin border and theme-matching text color.

### C. Illustrations & Graphic Assets
*   **Illustration Style:** 3D paper origami theme (*paper-craft style*) such as paper plane icons, clouds, and world landmarks to reinforce adventure and creativity.
*   **Iconography:** Minimalist line icons (*line icons*) colored to match secondary text or blue accents.

---

## 4. Page Layout & Structure (Layout & Grid)

*   **Container Width:** Standard *max-width* around `1200px` to `1280px` with responsive horizontal *padding*.
*   **Spacing / Whitespace:** Loose spacing between *sections* (around 60px – 80px) to keep the interface clean (*spacious & breathable*).
*   **Main Section Structure:**
    1.  *Navbar* (top navigation menu with logo, page links, and action button).
    2.  *Hero Section* with a main headline and an interactive *Search Widget* (Flights, Hotels, Cars, Experiences).
    3.  *Trust Badges* (best price guarantee, secure booking, 24/7 support).
    4.  *Popular Packages* (destination card grid with prices and ratings).
    5.  *Pricing Details* (package comparison table or cards: Economy, Premium, Business, Luxury).
    6.  *How to Book* (booking steps as a horizontal flow).
    7.  *Footer / Statistics* (achievement summary and customer reviews).

---

## 5. Responsive Behavior

*Follow the Tailwind breakpoint scale (mobile-first): `sm` ≥640px · `md` ≥768px · `lg` ≥1024px · `xl` ≥1280px.*

| Range | Hero + search widget | Navigation | Grids & sections |
|---|---|---|---|
| `xl` (≥1280px) | Full search widget (tabs + side-by-side fields) | Full | 3-column package grid, 96px padding |
| `lg` (1024–1280px) | Compact search widget | Full | 3-column package grid |
| `md` (768–1024px) | Fields stack in 2 columns | Hamburger + drawer | 2-column package grid, 64px padding |
| Base (<768px) | Tabs + fields stack vertically | Hamburger | 1 column, 48px padding |

- Hero heading 48–56px (desktop) → 32–36px (mobile); package prices always stay on one full line with their rating.
- The pricing table (Economy–Luxury) becomes one card per package below `md`, featured package stays first.
- The *How to Book* flow goes horizontal to vertical on mobile; trust badges wrap to 2 columns.

---

## 6. Motion & Animation

| Token | Value | Used for |
|---|---|---|
| `--motion-fast` | `150ms` | Hover, focus |
| `--motion-base` | `250ms` | Drawer, widget tabs, expand/collapse |
| `--motion-slow` | `400ms` | Hero entrance, scroll-reveal |
| `--ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | Default for all motion |
| `--ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | Symmetric motion |

`linear` is only for continuous motion (marquee, spinner).

- Animate only `transform` and `opacity`.
- Staged hero entrance: title → sub → search widget (±80ms stagger, 400ms ease-out).
- One-time scroll-reveal per section (fade + 16px translate-y) at 15% visibility; booking steps reveal in sequence.
- Widget tab switching (Flights/Hotels/Cars): 250ms field cross-fade; destination cards hover-zoom images 1.03.
- `prefers-reduced-motion`: show all content immediately; disable reveals and zoom.
