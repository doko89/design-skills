# UI Style Guide & Design System

This interface design style guide (*User Interface Style Guide*) is derived from the **Adminator Dashboard** design. Use this reference to keep visuals, components, and layout consistent in future app or dashboard development.

---

## 1. Colors

The palette carries a minimalist modern style with a clean background plus bright blue accents and contrasting status indicators.

*   **Primary (Main Color / Accent):**
    *   `#2563EB` or `#3B82F6` / Bright Blue (used for active menus, primary action buttons, navigation elements, and progress diagrams).
*   **Neutral & Background:**
    *   `#F8FAFC` (primary app background / clean *off-white*).
    *   `#FFFFFF` (card container, panel, and table backgrounds).
    *   `#64748B` / `#94A3B8` (secondary text, labels, and medium gray icons).
    *   `#0F172A` / `#1E293B` (primary text, headings, and dark stat numbers).
*   **Semantic / Status Colors:**
    *   **Success / Positive Trend:** `#10B981` (green for rising percentages or positive status).
    *   **Danger / Negative Trend:** `#EF4444` (red for metric drops or warnings).
    *   **Warning / Neutral Status:** `#F59E0B` (yellow/orange for *bounce rate* or specific progress).

---

## 2. Typography

Uses a clean modern sans-serif typeface with a highly readable scale (*Inter* or *SF Pro* style).

*   **Font Family:** Sans-serif (System UI / Inter).
*   **Hierarchy:**
    *   **Welcome / Page Title:** 24px - 28px, Bold (`#0F172A`).
    *   **Section Title (Section/Card Title):** 16px, Semi-bold (`#0F172A`).
    *   **Stat Value / Metrics:** 28px - 32px, Bold (primary stat numbers).
    *   **Body Text / Labels:** 13px - 14px, Regular/Medium (`#334155`).
    *   **Caption / Metadata / Subtext:** 11px - 12px, Regular (`#64748B`).

---

## 3. Layout & Structure (Layout & Grid)

*   **Left Sidebar Navigation:**
    *   Fixed width (*fixed width*), holding the product logo, menu categories (*Workspace*, *Communications*, *Components*), and the user profile at the bottom.
    *   The active menu is marked with a subtle bright-blue background and blue text.
*   **Top Header Bar:**
    *   Shows a *breadcrumb* (*Workspace > Dashboard*), a *Search* bar, notification icon, and profile button at the top right.
*   **Main Content Area:**
    *   Primary workspace with spacious padding.
    *   Uses a rounded-corner card-based layout (*Card-based Layout*).
*   **Top Metric Grid (Top Stat Cards):**
    *   4 columns of compact stat cards side by side in one row (Total visits, Page views, Unique visitors, Bounce rate).

---

## 4. UI Components

### A. Cards
*   **Border Radius:** `16px` for white card containers on a light gray background.
*   **Shadow / Elevation:** Very subtle shadow (*subtle shadow*) for a minimalist depth effect.
*   **Background:** Clean white (`#FFFFFF`).

### B. Buttons
*   **Primary Button (+ New report):**
    *   Bright blue background.
    *   Rounded corners (*border-radius: 10px* - `12px`).
    *   White text with an icon on the left (e.g., a plus or download arrow icon).
*   **Pro Badge:** Small blue capsule label with "PRO" text marking premium features.

### C. Stat Cards & Geography Indicators
*   **Stat Card:** Shows a small title on top, a large bold metric number, and a comparison note at the bottom (*e.g., "up from 1.12M last week"*) with a green/red trend indicator.
*   **Geography Breakdown:** Regional data row cards (United States, Europe, Australia, India) with a mini progress bar under each country's stat value.

### D. Circular Progress Charts
*   Used for performance metrics such as *New users*, *New purchases*, and *Bounce rate*.
*   Open/full circle charts with a center percentage, ringed in a matching indicator color (red, blue, yellow/orange) with short descriptive text beside them.

---

## 5. Responsive Behavior

*Follow the Tailwind breakpoint scale (mobile-first): `sm` ≥640px · `md` ≥768px · `lg` ≥1024px · `xl` ≥1280px.*

| Range | Sidebar & navigation | Card grid | Tables & charts |
|---|---|---|---|
| `xl` (≥1280px) | Full sidebar 220–260px | 3–4 columns | Full table, side-by-side charts |
| `lg` (1024–1280px) | 200–220px sidebar | 2–3 columns | Full table, 20px card padding |
| `md` (768–1024px) | Drawer (hamburger) or 72px icon rail | 1–2 columns | Table scroll-x + sticky first column |
| Base (<768px) | Drawer / bottom-nav | 1 column (stacked) | Full-width charts, compact axes |

- Never hide primary actions on small screens; move them to a compact header or floating button.
- Charts always follow the container width; avoid fixed card heights when content can wrap.
- Card padding 24px (desktop) → 16px (mobile); stat values 24px → 20px.
- Minimum 44px touch targets; full search becomes an icon below `md`.
- Circular progress shrinks proportionally on mobile (minimum 72px); geography indicators become a vertical list below `md`.

---

## 6. Motion & Animation

| Token | Value | Used for |
|---|---|---|
| `--motion-fast` | `150ms` | Hover, focus, tooltips |
| `--motion-base` | `250ms` | Drawer, dropdown, expand/collapse |
| `--ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | Default for all motion |
| `--ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | Symmetric motion (toggles, progress) |

`--motion-slow` (`400ms`) is for card entrances and chart animation; `linear` is only for continuous motion (spinners, skeleton shimmer).

- Animate only `transform` and `opacity` for 60fps.
- Card/button hover: lift 2–4px + soft shadow (150ms); press: `scale(0.98)`.
- Entrance: fade + `translate-y(8–12px)`, 40–60ms stagger between cards; progress percentages count up in 400–600ms.
- Drawer: 250ms ease-out slide + overlay fade; tooltips: 150ms fade.
- Loading: skeleton shimmer (1200ms loop); spinners only inside action buttons.
- `prefers-reduced-motion`: disable entrance, shimmer, and count-up; show the final state immediately.
- Circular progress rings fill clockwise (400ms ease-out) together with their number count-up.
