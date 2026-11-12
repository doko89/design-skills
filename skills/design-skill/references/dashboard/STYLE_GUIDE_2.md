# UI Style Guide & Design System

This interface design style guide (*User Interface Style Guide*) is derived from the **CRM Dashboard** design. Use this reference to keep visuals, components, and layout consistent in future app development.

---

## 1. Colors

The palette is dominated by clean base colors with bright accents for status indicators and metrics.

*   **Primary (Main Color / Accent):**
    *   `#4F46E5` / Indigo Blue (used for active navigation, primary buttons, main charts).
*   **Neutral & Background:**
    *   `#F8FAFC` (primary app background / *off-white*).
    *   `#FFFFFF` (card, panel, and container backgrounds).
    *   `#64748B` (secondary text / medium gray).
    *   `#0F172A` (primary text / dark).
*   **Semantic / Status Colors:**
    *   **Success / Converted:** `#10B981` (green) with a transparent light-green background.
    *   **Warning / Follow Up:** `#F59E0B` (orange/yellow).
    *   **Danger / Expense / Negative Trend:** `#EF4444` (red).
    *   **Info / New Lead:** `#3B82F6` (bright blue).
    *   **Positive Trend (Metrics):** `#22C55E` (bright green for rising percentages).

---

## 2. Typography

Uses a clean, easy-to-read modern sans-serif typeface (similar to *Inter* or *SF Pro*).

*   **Font Family:** Sans-serif (System UI / Inter).
*   **Hierarchy:**
    *   **Page Title:** 24px, Bold (`#0F172A`).
    *   **Section Title (Section/Card Title):** 16px - 18px, Semi-bold (`#0F172A`).
    *   **Body Text / Table Data:** 14px, Regular/Medium (`#334155`).
    *   **Caption / Metadata / Subtext:** 12px, Regular (`#64748B`).

---

## 3. Layout & Structure (Layout & Grid)

*   **Sidebar Navigation:**
    *   Vertical on the left side, fixed width.
    *   Contains the logo, category menus (Overview, Project, Tools), and a *Help Center* widget at the bottom.
*   **Main Content Area:**
    *   Primary content area on the right with consistent outer padding.
    *   Uses a **Card-based Layout** system (content grouped into white cards with rounded corners).
*   **Metric Card Grid (Top Stat Cards):**
    *   Divided into 4 columns of data summary cards at the top (Total Customers, Active Customers, Total Profit, Total Expense).

---

## 4. UI Components

### A. Cards
*   **Border Radius:** `16px` to `24px` for smoothly rounded card corners.
*   **Shadow / Elevation:** Uses a very thin, soft shadow (*soft drop shadow*) for an *elevation* feel above the light gray background.
*   **Background:** White (`#FFFFFF`).

### B. Buttons
*   **Primary Button:**
    *   Indigo blue background (`#4F46E5`).
    *   Rounded corners (`border-radius: 12px`).
    *   Medium-bold white text with an icon on the left (optional).
*   **Navigation Menu Item:**
    *   *Active State*: blue background with white text and rounded corners.
    *   *Default State*: gray text with no background, shifting to a subtle hover effect as the cursor approaches.

### C. Tables
*   Used in the report section (*Leads Report*).
*   **Table Header:** Small gray text in capital/normal case, with no flashy underline.
*   **Table Rows:** Separated by generous spacing and thin horizontal divider lines.
*   **Avatar:** The name column includes a circular profile photo (*circular avatar*).
*   **Status Badge:** Status labels use a capsule style (*pill badge*) with a transparent background matching the status (e.g., green for *Converted*, orange for *Follow Up*).

### D. Charts & Data Visualization
*   **Bar Chart:** Uses solid blue bars plus some striped/patterned bars for data comparison (e.g., Profit vs Expense).
*   **Donut / Progress Chart:** Hollow circle chart with a center percentage, ringed by multicolor segments (blue, red, green) showing proportional data distribution.

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
- Card padding 24px (desktop) → 16px (mobile); KPI values 24px → 20px.
- Minimum 44px touch targets; full search becomes an icon below `md`.
- Striped-vs-solid bar charts stay side by side down to `md`; below that they stack. The proportional donut legend moves below the chart on mobile.

---

## 6. Motion & Animation

| Token | Value | Used for |
|---|---|---|
| `--motion-fast` | `150ms` | Hover, focus, tooltips |
| `--motion-base` | `250ms` | Drawer, dropdown, expand/collapse |
| `--motion-slow` | `400ms` | Card entrance, chart animation |
| `--ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | Default for all motion |
| `--ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | Symmetric motion (toggles, progress) |

`linear` is only for continuous motion (spinners, skeleton shimmer).

- Animate only `transform` and `opacity` for 60fps.
- Card/button hover: lift 2–4px + soft shadow (150ms); press: `scale(0.98)`.
- Entrance: fade + `translate-y(8–12px)`, 40–60ms stagger between cards; KPI numbers count up in 400–600ms.
- Drawer: 250ms ease-out slide + overlay fade; tooltips: 150ms fade.
- Loading: skeleton shimmer (1200ms loop); spinners only inside action buttons.
- `prefers-reduced-motion`: disable entrance, shimmer, and count-up; show the final state immediately.
- Solid blue bars animate first, then the striped bars; donut segment proportions stay exact during animation.
