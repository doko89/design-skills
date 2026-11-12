# Suburban UI Design System & Style Guide

This visual style guide (Style Guide) is based on the **Suburban** dashboard UI.

---

## 1. Color Palette

### Primary & Accent Colors
* **Primary Brand / Sidebar Background:** `#4C46F0` / `#4838EA` (Electric Royal Blue)
* **Accent Highlight / Gradient Primary:** `#5646FF` (Bright Indigo / Violet)
* **Accent Light / Soft Indigo (Icon Backgrounds):** `#EEEDFD` / `#EAE8FF`
* **Accent Success (Green):** `#00C896` / `#22C55E`
* **Accent Danger / Negative (Red):** `#EF4444` / `#F87171`

### Neutral Colors
* **Main App Background:** `#F4F5FB` (Very Light Slate/Gray)
* **Card / Container Background:** `#FFFFFF` (Pure White)
* **Text Dark (Headings & Primary Text):** `#2D3748` / `#1E293B`
* **Text Muted (Labels & Secondary Text):** `#8C98A9` / `#64748B`
* **Border / Divider:** `#E2E8F0` / `#EDF2F7`

---

## 2. Typography

* **Primary Font Family:** `Inter`, `Roboto`, or `Plus Jakarta Sans` (modern sans-serif)

### Text Scale & Hierarchy

| Role | Size (px / rem) | Weight | Usage |
| :--- | :--- | :--- | :--- |
| **Heading 1 / Metric Value** | `28px - 32px` (`1.75rem - 2rem`) | Bold (700) | Primary metric numbers (e.g., 39881, 42283) |
| **Heading 2 / App Title** | `20px` (`1.25rem`) | Semi-Bold (600) | Brand name ("Suburban"), header sub-title |
| **Heading 3 / Card Title** | `14px - 16px` (`0.875rem - 1rem`) | Semi-Bold (600) | Widget/card titles ("Sales", "Purchases", "Overview") |
| **Body / Standard Text** | `13px - 14px` (`0.8125rem - 0.875rem`) | Regular (400) / Medium (500) | Sidebar menu text, list text |
| **Caption / Sub-label** | `11px - 12px` (`0.6875rem - 0.75rem`) | Regular (400) | Sub-text ("Since last month", "9:30 am" timestamps) |

---

## 3. Elevation & Shadows (Shadows & Elevation)

* **Base Elevation (Cards):**
  `box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.03);`
* **Active / Focus Card Elevation:**
  `box-shadow: 0px 8px 20px rgba(76, 70, 240, 0.25);`
* **Floating Element (Tooltip/Active Row):**
  `box-shadow: 0px 10px 25px rgba(76, 70, 240, 0.35);`

---

## 4. Border Radius & Corners

* **Cards / Container:** `8px` - `12px`
* **Buttons / Tags:** `6px` - `8px`
* **Icon Bubbles / Avatars:** `50%` (Fully Circular)
* **Active Highlight Card:** `8px`

---

## 5. UI Components (Standard)

### A. Sidebar Navigation
* **Background:** Indigo Blue (`#4C46F0`)
* **Normal Text:** Semi-transparent white (`rgba(255, 255, 255, 0.7)`)
* **Active State Item:**
  * Background: Slightly darker / saturated blue (`#3B32E0`)
  * Text: Solid White (`#FFFFFF`)
  * Left Indicator (Optional): White bar / highlight block

### B. Metric Summary Cards
* **Layout:** 3-column grid
* **Elements:**
  1. Title (Top Left, Muted Color)
  2. Main Value (Large, Bold)
  3. Trend Indicator (Bottom Left):
     * Positive: Green Icon ($\uparrow$) + Percentage Value
     * Negative: Red Icon ($\downarrow$) + Percentage Value
  4. Circular Icon Badge (Top Right): Soft light purple background (`#EEEDFD`) with a primary blue icon.

### C. Active Item List (Example: "Overview Widget")
* **Default Row:** Dark text with a gray sub-label.
* **Active / Selected Row (Highlight):**
  * Background: Blue linear gradient (`#5646FF` to `#4C46F0`)
  * Text & Accent: Fully White (`#FFFFFF`)
  * Border Radius: `6px`
  * Shadow: Soft blue-tinted drop-shadow.

### D. Activity Feed List
* **Timeline Layout:**
  * **Date Column:** Date (Bold, Medium) & Time (Light, Small)
  * **User Column:** Name (Primary Color / Medium Weight) & Activity Sub-text.

### E. Chart Styles
* **Line Chart:**
  * Line stroke: `#4C46F0` (Thickness: `2px` - `3px`)
  * Smooth curve (Bezier interpolation)
* **Bottom Stat Bar (Card Footer Highlight):**
  * Full-width background block in `#4C46F0`
  * Text Inside: White with clear vertical dividers.

---

## 6. Spacing System

* **Base Unit:** `8px`
* **Padding Inside Cards:** `20px` - `24px`
* **Gap Between Cards (Grid Spacing):** `20px`
* **Sidebar Padding:** `24px` (Left/Right)

---

## 7. Responsive Behavior

*Follow the Tailwind breakpoint scale (mobile-first): `sm` ≥640px · `md` ≥768px · `lg` ≥1024px · `xl` ≥1280px.*

| Range | Sidebar & navigation | Card grid | Tables & charts |
|---|---|---|---|
| `xl` (≥1280px) | Full sidebar | 3–4 columns | Full table, side-by-side charts |
| `lg` (1024–1280px) | 200–220px sidebar | 2–3 columns | Full table, 20px card padding |
| `md` (768–1024px) | Drawer (hamburger) or 72px icon rail | 1–2 columns | Table scroll-x + sticky first column |
| Base (<768px) | Drawer / bottom-nav | 1 column (stacked) | Full-width charts, compact axes |

- Never hide primary actions on small screens; move them to a compact header or floating button.
- Charts always follow the container width; avoid fixed card heights when content can wrap.
- Card padding 20–24px (desktop) → 16px (mobile); grid gap 20px → 12–16px.
- Minimum 44px touch targets; full search becomes an icon below `md`.
- Metric summary cards go 4→2→1 columns; activity feed full-width below `md`; overview widget stacks vertically on mobile.

---

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
- Activity feed items: sequential fade-slide (50ms stagger) when the list loads.
- Drawer: 250ms ease-out slide + overlay fade; tooltips: 150ms fade.
- Loading: skeleton shimmer (1200ms loop); spinners only inside action buttons.
- `prefers-reduced-motion`: disable entrance, shimmer, and count-up; show the final state immediately.
