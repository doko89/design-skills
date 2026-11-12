# Super Finti UI Design System & Style Guide

This visual style guide (Style Guide) is based on the **Super Finti** fintech dashboard interface.

---

## 1. Color Palette

This dashboard uses a **Soft Pastel Glassmorphism** aesthetic blending a clean light background with pastel gradient accents.

### Primary Brand & UI Base
* **Sidebar & Main Background:** `#F7F8FC` / `#FAFAFF` (Ultra Soft Gray-Blue)
* **Card Container Background:** `#FFFFFF` (Pure White)
* **Text Primary (Dark Slate):** `#1E1F31` / `#2B2D42`
* **Text Secondary / Muted:** `#8D93A5` / `#94A3B8`

### Card Gradient Palette (Pastel Cards)
* **Working Balance Card (Gradient):** `linear-gradient(135deg, #FFE8D6 0%, #E0E7FF 50%, #C7D2FE 100%)`
* **Saving Status Card (Gradient):** `linear-gradient(135deg, #FFF3E0 0%, #FFE4E6 50%, #FFD1D1 100%)`
* **Credit Card (Mint Gradient):** `linear-gradient(135deg, #DCFCE7 0%, #BBF7D0 60%, #86EFAC 100%)`
* **Help Center Card (Glassmorphic):** `linear-gradient(180deg, #FFF7ED 0%, #E0E7FF 100%)` with blur.

### Icon Badge Colors (Upcoming Transactions & Stats)
* **Purple (Water Bill / Task Bar):** `#5B46F6`
* **Coral Red (Salary Redwhale / Negative Amount):** `#FF5668`
* **Bright Blue (Electric Bill / Wise):** `#0099FF`
* **Amber / Gold (Income Transfers):** `#FFAB00`
* **Emerald Green (Success / Mint Accent):** `#10B981`

---

## 2. Typography

* **Primary Font Family:** `Plus Jakarta Sans`, `Inter`, or `Outfit` (Modern Rounded Sans-serif)

### Text Scale & Hierarchy

| Role | Size (px / rem) | Weight | Usage Example |
| :--- | :--- | :--- | :--- |
| **Hero Balance / Number** | `26px - 30px` (`1.625rem - 1.875rem`) | Bold (700) | `PKR 9,250,000` |
| **Card Title / Main Header** | `16px - 18px` (`1rem - 1.125rem`) | Semi-Bold (600) | `Latest Transactions`, `Upcoming Transactions` |
| **Card Label / Sub-title** | `12px - 13px` (`0.75rem - 0.8125rem`) | Semi-Bold (600) | `Your Working Balance`, `Your Saving Status` |
| **Body / List Item** | `13px - 14px` (`0.8125rem - 0.875rem`) | Medium (500) | `Payment Sent to Shakir`, `Electric Bill` |
| **Section Label / Small Text** | `11px - 12px` (`0.6875rem - 0.75rem`) | Semi-Bold (600) / Regular | `Main Navigation`, `Settings & Schedules`, `Mon, Mar 1` |

---

## 3. Elevation, Shadows & Glassmorphism

* **Standard Card Elevation:**
  `box-shadow: 0px 10px 30px rgba(220, 225, 240, 0.4);`
* **Colored Glow (Bar Chart & Floating Badges):**
  * Coral Glow: `box-shadow: 0px 8px 16px rgba(255, 86, 104, 0.4);`
  * Purple Glow: `box-shadow: 0px 8px 16px rgba(91, 70, 246, 0.4);`
  * Teal Glow: `box-shadow: 0px 8px 16px rgba(16, 185, 129, 0.4);`
* **Glassmorphism Backdrop (Help Center):**
  `backdrop-filter: blur(12px); background: rgba(255, 255, 255, 0.6);`

---

## 4. Border Radius & Corners

* **Top Summary Cards:** `20px` - `24px` (Very Soft Rounded)
* **List Row / Input / Badges:** `12px` - `14px`
* **Icon Containers (Square Soft):** `14px`
* **Search Input & Buttons:** `12px` - `20px` (Pill-like / Soft)

---

## 5. Standard UI Components

### A. Top Balance & Status Cards
* Cards use very subtle pastel gradient combinations.
* Amount numbers print bold in a strong dark color (`#1E1F31`) for high contrast.
* The credit card at the top right uses a curved wave motif (concentric curves) with white transparency.

### B. Summary Bar Charts (Tasks Summary)
* **Background Bar:** Warm light gray (`#F1F3F9`) with `border-radius: 6px`.
* **Active Progress Bar:** Solid colors (Coral, Indigo, Teal) with a matching **Glow / Soft Shadow** under the bar.

### C. Transaction Lists
* **List Item Styling:**
  * Left icon badge as a rounded box (`14px` radius) with a solid background and white icon.
  * Transaction names use `Medium (500)` font.
  * `+`-signed amounts are green (`#10B981`); `-` or unsigned amounts are red/dark.

### D. Floating Help Center Banner (Sidebar Bottom)
* Background uses a subtle pastel gradient with a glass (glassmorphism) effect.
* A floating circle badge at the top of the card with a help icon (`?`).
* CTA button as a solid white capsule with bold text.

---

## 6. Layout & Spacing

* **Sidebar Width:** `240px - 260px`
* **Grid Spacing (Gutter):** `24px`
* **Card Inner Padding:** `20px` - `24px`

---

## 7. Responsive Behavior

*Follow the Tailwind breakpoint scale (mobile-first): `sm` ≥640px · `md` ≥768px · `lg` ≥1024px · `xl` ≥1280px.*

| Range | Sidebar & navigation | Card grid | Tables & charts |
|---|---|---|---|
| `xl` (≥1280px) | Full sidebar 240–260px | 3–4 columns | Full list, side-by-side charts |
| `lg` (1024–1280px) | 220px sidebar | 2–3 columns | Full list, 20px card padding |
| `md` (768–1024px) | Drawer (hamburger) or 72px icon rail | 1–2 columns | Full-width list, compact bar chart |
| Base (<768px) | Drawer / bottom-nav | 1 column (stacked) | Full-width charts, compact axes |

- Never hide primary actions on small screens; move them to a compact header or floating button.
- Pastel gradient cards: stack to 1 column below `md`; keep text contrast over gradients at all sizes.
- The help-center banner (sidebar footer) moves below the content — or behind a help button — when the sidebar becomes a drawer.
- Minimum 44px touch targets; transaction rows full-width with 16px padding on mobile.

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

- Animate only `transform` and `opacity` for 60fps; NEVER animate the glassmorphism blur value (expensive, causes jank).
- Card/button hover: lift 2–4px + soft shadow (150ms); press: `scale(0.98)`.
- Entrance: fade + `translate-y(8–12px)`, 40–60ms stagger between cards; top-balance count-up 500ms.
- Transaction rows: 150ms highlight on hover; summary bar chart grows from the baseline (400ms).
- Drawer: 250ms ease-out slide + overlay fade.
- Loading: skeleton shimmer (1200ms loop); spinners only inside action buttons.
- `prefers-reduced-motion`: disable entrance, shimmer, and count-up; show the final state immediately.
