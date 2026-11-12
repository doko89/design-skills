# FinanceFlow UI Design System & Style Guide

This visual style guide (Style Guide) is based on the **FinanceFlow** financial dashboard interface.

## 1. Color Palette

This dashboard carries a **Clean, Ultra-Minimalist, & Vivid Blue Accent** design with a crystal-clear all-white background and strong electric blue accent contrast.

### Primary & Accent Colors

* **Primary Electric Blue:** `#0066FF` / `#0D6EFD` (primary brand color, active buttons, debit cards)

* **Primary Soft Gradient (Chart & Cards):** `linear-gradient(180deg, rgba(0, 102, 255, 0.12) 0%, rgba(255, 255, 255, 0) 100%)`

* **Success Mint / Green:** `#10B981` / `#D1FAE5` (pill tag "+23% vs last month", "Connected" status badge)

* **Warning / Pending Orange:** `#F59E0B` / `#FEF3C7` ("PENDING" status badge)

* **Chart Accent Blue Shades:** `#0047AB` (Navy Blue), `#3B82F6` (Sky Blue), `#60A5FA` (Light Blue)

### Neutral Colors

* **Main Background:** `#F8FAFC` / `#F1F5F9` (Clean Cool Slate)

* **Card / Container Background:** `#FFFFFF` (Pure White)

* **Text Dark (Headings & Values):** `#0F172A` / `#1E293B`

* **Text Muted (Labels & Timestamps):** `#64748B` / `#94A3B8`

* **Border & Dividers:** `#F1F5F9` / `#E2E8F0`

## 2. Typography

* **Primary Font Family:** `Inter`, `Plus Jakarta Sans`, or `Outfit`

### Text Scale & Hierarchy

| Role | Size (px / rem) | Weight | Usage Example |
| ----- | ----- | ----- | ----- |
| **Heading 1 / Hero Amount** | `24px - 28px` (`1.5rem - 1.75rem`) | Semi-Bold (600) / Bold (700) | `$12,135.69` |
| **Heading 2 / Metric Large** | `20px - 22px` (`1.25rem - 1.375rem`) | Semi-Bold (600) | `$58,764.25` |
| **Heading 3 / Section Header**| `15px - 16px` (`0.9375rem - 1rem`) | Semi-Bold (600) | `Total Outstanding`, `Transaction History` |
| **Body Text / User Name** | `13px - 14px` (`0.8125rem - 0.875rem`) | Medium (500) | `Naziya Islam`, `Ayerin`, `Pay Verified` |
| **Caption / Sub-label** | `11px - 12px` (`0.6875rem - 0.75rem`) | Regular (400) | `@naziyaislam`, `The Walt Disney Company`, `Feb 15` |

## 3. Elevation & Shadows (Shadows & Elevation)

* **Minimal Card Shadow:**
  `box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.02);` (very subtle, almost flat)

* **Active Tooltip Shadow (Chart):**
  `box-shadow: 0px 8px 24px rgba(0, 102, 255, 0.15);`

* **Hover Button Shadow:**
  `box-shadow: 0px 6px 16px rgba(0, 102, 255, 0.25);`

## 4. Border Radius & Corners

* **Main App Canvas Radius:** `24px`

* **Cards / Containers:** `16px`

* **Buttons & Inputs:** `10px` - `12px`

* **Pill Badges (Connected / Pending):** `20px` (Full Pill)

* **Avatars:** `50%` (Fully Circular)

## 5. Standard UI Components

### A. Minimalist Sidebar

* Clean white background (`#FFFFFF`) separated by a thin vertical border (`#F1F5F9`).

* **Profile Section:** Round avatar on the left with the name (Bold) and `@handle` username (Muted) below it.

* **Menu Items:** Thin icons with medium text.

* **Active Menu State:** Text and icon in primary blue (`#0066FF`), with no thick pill background (only a simple indicator or bold font).

* **Notification Badge:** Pink circle holding a counter number (e.g., `10` on the Events menu).

### B. Summary & Metric Cards

* All-white background with large currency values (cent fractions slightly smaller or thin gray).

* **Header Icon:** Small minimalist gray/blue icon beside the card title.

### C. Chart & Tooltip Interface

* **Area Line Chart:** Smooth blue stroke line (`2px`) with a transparent gradient fill under the line.

* **Interactive Tooltip Card:** Floating white card with a soft blue shadow, showing chart point date and amount details.

* **Time-range Selector:** Mini pill buttons (`1M`, `3M`, `6M`, `1Y`) with the active state on a light gray background (`#F1F5F9`).

### D. Action Table / Transaction History

* **Row Design:** Clean row format with no thick borders.

* **Avatar & Meta:** User profile photo, bright name, and company name sub-text (e.g., *eBay*, *Pizza Hut*).

* **Action Button ("Send Invoice"):**

  * Primary / First Row: Solid Blue (`#0066FF`) with white text + icon.

  * Outline / Standard Rows: Thin border (`#E2E8F0`), transparent background, dark gray text + icon.

### E. Visual Cards & Donut Chart

* **Vivid Blue Credit Card:** Solid blue card (`#0066FF`) with an abstract curved transparent motif on its background.

* **Donut Chart (Payroll Summary):** Half-circle chart (semi-donut) split across navy blue, bright blue, and cyan.

## 6. Layout & Grid

* **Sidebar Width:** `220px`

* **Top Search Bar:** Curved pill-like input (`12px` radius) with a gray search icon.

* **Grid Gutter:** `20px` - `24px`

## 7. Responsive Behavior

*Follow the Tailwind breakpoint scale (mobile-first): `sm` ≥640px · `md` ≥768px · `lg` ≥1024px · `xl` ≥1280px.*

| Range | Sidebar & navigation | Card grid | Tables & charts |
|---|---|---|---|
| `xl` (≥1280px) | Full 220px sidebar | 3–4 columns | Full action table, side-by-side charts |
| `lg` (1024–1280px) | 200px sidebar | 2–3 columns | Full table, 20px card padding |
| `md` (768–1024px) | Drawer (hamburger) or 72px icon rail | 1–2 columns | Table scroll-x + sticky first column |
| Base (<768px) | Drawer / bottom-nav | 1 column (stacked) | Full-width charts, compact axes |

- Never hide primary actions on small screens; move them to a compact header or floating button.
- The top search pill becomes an icon below `md`; tap to expand a full-width search overlay.
- Transaction history table: scroll-x with sticky date/action columns; below `sm` it may become one card per transaction.
- Donut + visual cards stack vertically on mobile; never clip the legend.
- Minimum 44px touch targets; card padding 20–24px → 16px.

## 8. Motion & Animation

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
- Entrance: fade + `translate-y(8–12px)`, 40–60ms stagger between cards; summary numbers count up in 400–600ms.
- Chart tooltips: 150ms fade following cursor/focus; table rows highlight 150ms on hover.
- Drawer: 250ms ease-out slide + overlay fade.
- Loading: skeleton shimmer (1200ms loop); spinners only inside action buttons.
- `prefers-reduced-motion`: disable entrance, shimmer, and count-up; show the final state immediately.
