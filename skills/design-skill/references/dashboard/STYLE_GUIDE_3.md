# UI Style Guide & Design System — SalesHub Dashboard

This interface design style guide (*User Interface Style Guide*) is derived from the **SalesHub Dashboard** interface. It serves as the standard reference for keeping visuals, UI components, and color schemes consistent in app development.

---

## 1. Color Palette

The palette uses a *Soft Indigo & Clean White* theme with varied bright accents for statistics and chart data representation.

### A. Brand & Neutral Colors
*   **Primary Brand:** `#3F49A6` / `Indigo Blue` (used on the logo, active menu status, primary metric icons, and main trend lines).
*   **Main Background:** `#EEF2F7` / `Soft Lavender Gray` (outer app area background).
*   **Card Background:** `#FFFFFF` / `Pure White` (base color for cards, panels, and the search bar).
*   **Text Primary:** `#1E293B` / `Dark Slate` (primary text color for titles and important numbers).
*   **Text Secondary / Muted:** `#8E9BBA` / `Cool Gray` (inactive menu text, chart labels, and sub-text).

### B. Data Visualization Colors
*   **Pie Chart & Stacked Bar Segments:**
    *   **Indigo:** `#3F49A6`
    *   **Periwinkle / Soft Blue:** `#8C9CDD`
    *   **Amber / Orange:** `#F59E0B`
    *   **Cyan / Light Blue:** `#38BDF8`
    *   **Purple / Violet:** `#A855F7`
*   **Trend / Negative Status:** `#EF4444` / `Soft Red` (percentage decrease indicator, e.g., `-16.21%`).

---

## 2. Typography

The typography system uses a minimalist, proportional modern sans-serif typeface.

*   **Font Family:** `Inter`, `Plus Jakarta Sans`, or `System UI Sans-serif`.
*   **Text Hierarchy Scale:**
    *   **Brand Logo Title:** 18px, Bold (`#3F49A6`).
    *   **Metric Value (Large):** 20px - 22px, Bold (`#1E293B`).
    *   **Card / Section Title:** 15px - 16px, Semi-Bold (`#1E293B`).
    *   **Body / Table Text:** 13px - 14px, Regular / Medium (`#334155`).
    *   **Subtext / Axis Label:** 11px - 12px, Regular (`#8E9BBA`).

---

## 3. Layout & Structure (Layout & Grid)

*   **Sidebar Navigation (Left):**
    *   Docked on the left with an active-position indicator as a thick edge line on the far left of the active menu item (*Active Indicator Line*).
    *   Inactive menu text uses pale gray (*paled text*).
*   **Header Bar (Top):**
    *   Divided into a *Search Input* on the left, a date range filter (*Date Picker*) in the center, and the notification bell plus user profile on the right.
*   **Main Content Grid:**
    *   **Top Metric Cards:** 4 side-by-side columns for process summaries (*Picked, Shipped, Delivered, Invoice*).
    *   **Middle Section:** Split layout (Sales Trend chart 2/3 width + Sales-per-City pie chart 1/3 width).
    *   **Bottom Section:** Split layout (per-channel Stacked Bar chart 1/2 width + Top Products table 1/2 width).

---

## 4. UI Components

### A. Cards & Containers (Cards)
*   **Border Radius:** `12px` to `16px` for smooth rounded corners.
*   **Border & Shadow:** No border (*no border*); relies on a very subtle *Soft Drop Shadow* to separate cards from the main background.

### B. Inputs & Filters (Form Controls)
*   **Search Box & Select Dropdown:**
    *   White background with a thin border (*border: 1px solid #E2E8F0*).
    *   `Border Radius`: `8px`.
    *   Includes a search or calendar icon to the left of the label.

### C. Compact Metric Elements (Metric Cards)
*   **Metric Icon Box:** Icons in the top metric cards sit in blunt-cornered square containers (`border-radius: 8px`) in *Indigo Blue* (`#3F49A6`) with white icons.

### D. Data Tables
*   **Table Header:** Medium gray, *Regular* text, aligned with the data columns.
*   **Table Rows:** Use thin horizontal divider lines (`#F1F5F9`).
*   **Alignments:**
    *   Item name text is *left-aligned*.
    *   Numeric values (Price, Quantity, Total) are *right-aligned*.

### E. Charts (Visualization)
1.  **Line Chart (Sales Trend):**
    *   Shows a two-line comparison (This Week vs Last Week).
    *   The primary line uses Indigo (`#3F49A6`) with data point markers (*data dots*).
    *   The comparison line uses neutral gray (`#CBD5E1`).
2.  **Pie Chart:**
    *   Full circle chart divided by category color proportions.
    *   The *Legend* sits below the chart in a vertical list with percentages right-aligned.
3.  **Stacked Bar Chart:**
    *   Thin vertical bars divided into colored segments representing distribution channels per day.

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
- Card padding 24px (desktop) → 16px (mobile); compact metric cards go 1 column below `md`.
- Minimum 44px touch targets; side-by-side filters/inputs stack on mobile.
- The pie chart legend stays vertical below the chart at all sizes; stacked bars thin proportionally and tooltips replace hidden axis labels on mobile.

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
- Entrance: fade + `translate-y(8–12px)`, 40–60ms stagger between cards; metric numbers count up in 400–600ms.
- Drawer: 250ms ease-out slide + overlay fade; chart tooltips: 150ms fade.
- Loading: skeleton shimmer (1200ms loop); spinners only inside action buttons.
- `prefers-reduced-motion`: disable entrance, shimmer, and count-up; show the final state immediately.
- Stacked bar segments grow from the bottom (400ms); pie slices fade in one by one following the legend order.
