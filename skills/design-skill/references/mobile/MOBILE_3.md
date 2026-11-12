# Crypto Wallet & Trading Mobile App - Style Guide

This *Design System* document is designed specifically around the **Crypto Wallet & Trading** app interface. It provides visual and technical standards for UI/UX designers and interface (*front-end*) developers.

---

## 1. Color Palette

The app uses a dominant **Electric Blue / Light Violet** scheme with **Bright Red/Green** accents typical of financial and *crypto trading* apps to mark price fluctuations.

### A. Primary & Brand Colors

| Color Name | Hex Code | Primary Usage |
| :--- | :--- | :--- |
| **Electric Violet** | `#6C5CE7` | Hero Card (Combined Wallet Value), *Buy* button, active filter. |
| **Soft Violet Tint** | `#F1F0FE` | Filter chip backgrounds, secondary tabs, action containers. |
| **Deep Slate/Navy** | `#1E272E` | Primary text, page titles, crypto price numbers. |
| **App Background** | `#F8F9FD` | Overall app background (*light mode*). |
| **Card Surface** | `#FFFFFF` | Info card backgrounds, transaction list items, coin cards. |

### B. Functional & Trading Colors

| Color Name | Hex Code | Primary Usage |
| :--- | :--- | :--- |
| **Positive Green** | `#00B894` | Price increase percentages (`+5.15%`), incoming transaction values (`+XRP 20.12`). |
| **Negative Red** | `#FF7675` | Price decrease percentages (`-4.13%`), outgoing transactions (`-BTC 0.085`), *Sell* button. |
| **Muted Grey** | `#A4B0BE` | Date labels, sub-header text, secondary USD conversion prices. |

---

## 2. Typography

Uses a modern sans-serif font with high number legibility (recommended: **Inter**, **SF Pro Display**, or **Plus Jakarta Sans**).

| Typography Role | Size | Weight | Usage Example |
| :--- | :--- | :--- | :--- |
| **Display / Metric** | `26px` - `30px` | Bold (`700`) | Current Price (`$62,809.80`), Combined Wallet (`$1,592.02`) |
| **Screen Title** | `18px` - `20px` | SemiBold (`600`) | Title bar (`Bitcoin`, `Transactions`) |
| **Section Header** | `15px` - `16px` | Bold (`700`) | "My Cryptocurrencies", "Ranking List" |
| **Coin Symbol & Price** | `14px` - `15px` | SemiBold (`600`) | Asset names (`BTC Bitcoin`), order book numbers |
| **Body / Label** | `12px` - `13px` | Medium (`500`) | Action buttons (`Send`, `Receive`, `Buy/Sell`) |
| **Caption / Change** | `11px` - `12px` | Regular (`400`) | Transaction dates, price change percentages |

---

## 3. Elevation & Shadows (Shadow & Elevation)

Uses subtle violet-tinted shadows for a *soft depth* effect.

```css
/* Card & List Items Elevation */
box-shadow: 0px 6px 18px rgba(108, 92, 231, 0.06);

/* Hero Wallet Card Elevation */
box-shadow: 0px 12px 28px rgba(108, 92, 231, 0.25);

/* Floating Chart Area Shadow */
filter: drop-shadow(0px 8px 16px rgba(108, 92, 231, 0.15));
```

---

## 4. Corner Softness (Border Radius)

* **Hero Cards / Wallet Banners:** `24px`
* **Content Cards / List Containers:** `16px` - `20px`
* **Action Buttons (Buy/Sell/Timeframe):** `12px` - `14px`
* **Crypto Icon Container:** `50%` (perfect circle)

---

## 5. Main UI Components

### A. Wallet Header Card
* **Background:** Solid `#6C5CE7` or a smooth linear gradient toward light purple.
* **Action Layout:** A rounded *floating white bar* with 3 action buttons (*Send*, *Receive*, *Buy/Sell*) at the bottom of the balance banner.

### B. Crypto Chart (Area Graph)
* **Curve Line:** Smooth spline in `#6C5CE7` (`stroke-width: 3px`).
* **Area Fill:** Transparent gradient from purple (`rgba(108, 92, 231, 0.3)`) at the top fading to transparent (`0%`) at the bottom.
* **Timeframe Selector:** Small capsule tabs (`24h`, `1w`, `1m`, `6m`, `1y`) with the active tab in purple `#6C5CE7`.

### C. Watchlist & Coin Cards
* **Layout:** Horizontal grid (2 columns) or vertical list (*list row*).
* **Coin Icons:** Circles with each coin's unique background color (Bitcoin: orange, Ethereum: purple, Ripple: black/gray).

### D. Order Book & Trading Actions
* **Order Book Table:** *Bid* (green), *Price*, and *Ask* (red) columns.
* **Trading Buttons (Bottom Bar):** Side-by-side two-button layout:
  * **Sell:** Red `#FF7675`
  * **Buy:** Purple `#6C5CE7`

---

## 6. System Spacing & Grid

* **Page Margin:** `20px` (left & right)
* **Section Gap:** `20px` - `24px`
* **Card Internal Padding:** `16px`
* **Icon-to-Text Gap:** `12px`

---

## 7. Responsive Behavior

*Mobile-first base 360–430px; use the Tailwind scale upward: `sm` ≥640px · `md` ≥768px · `lg` ≥1024px.*

- Base design 360–430px: 1 column, 20px margins, full-width cards.
- ≥`sm` (large phones / portrait tablets): max-w-md centered container; watchlist 1 column; chart full-width.
- `md` and up (tablets): max-w-lg; order book may use 2 columns (bid/ask side by side).
- The order book becomes bid/ask tabs below `sm`; price numbers use tabular-nums so they don't shift.
- Safe area: use `env(safe-area-inset-*)` for the header, bottom nav, and trading action buttons.
- Landscape: chart height ≤40vh; timeframe chips become a horizontal scroll row.
- Dynamic text: support scaling up to 130% without clipping (wrap, avoid fixed heights).
- Touch targets ≥44px with ≥8px gaps between targets; Buy/Sell buttons side by side, full-width.

---

## 8. Motion & Animation

| Token | Value | Used for |
|---|---|---|
| `--motion-fast` | `150ms` | Touch feedback, tab fade |
| `--motion-base` | `250ms` | Screen transitions, chart redraw |
| `--motion-slow` | `400ms` | Entrance, chart animation |
| `--ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | Default for all motion |
| `--ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | Toggles, progress |

- Screen transitions: 250–300ms ease-out slide-x + fade; back button = reverse direction.
- Rising/falling prices: 300ms green/red flash on the number (not the whole card) to avoid distraction.
- Area chart: 250ms redraw when the timeframe changes; crosshair cursor follows touch without lag.
- Tab switching: 150ms fade with no sliding, for stability.
- Watchlist pull-to-refresh: resistance indicator + spinner; initial data uses a 1200ms skeleton shimmer.
- `prefers-reduced-motion`: replace all slides with a fast 150ms fade; disable flash & shimmer (show the final value).
