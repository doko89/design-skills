# Personal Finance & Expense Tracker - Style Guide

This *Design System* document is designed specifically around the **Personal Finance & Expense Tracker** app interface. It sets visual and technical standards to keep UI/UX design and interface (*front-end*) development consistent.

---

## 1. Color Palette

The app adopts **Electric Royal Blue** as its base color, combined with a multi-color palette (*vibrant categorical palette*) to distinguish expense categories and analytics charts.

### A. Primary & Interface Colors

| Color Name | Hex Code | Primary Usage |
| :--- | :--- | :--- |
| **Electric Royal Blue** | `#1E65FF` | Header banner, primary card (*Account Balance*), FAB (*Floating Action Button*), active filter. |
| **Soft Blue Tint** | `#EBF2FF` | Active category highlight, filter badge/capsule backgrounds. |
| **Deep Charcoal** | `#1A202C` | Page titles, primary amounts, high-emphasis text. |
| **App Background** | `#F4F7FC` | App base background (*light mode*). |
| **Surface White** | `#FFFFFF` | Card (*cards*), statistics container, and transaction list item backgrounds. |

### B. Categorical Colors (Donut Chart & Icons)

Used specifically for financial category visualization, pie charts, and icons:

| Category | Hex Code | Visual Representation |
| :--- | :--- | :--- |
| **Shopping** | `#2F80ED` | Medium Blue |
| **Home** | `#00C9A7` | Mint / Teal Green |
| **Food & Drink** | `#FF4B4B` | Bright Red |
| **Trips** | `#B83280` | Purple / Magenta |
| **Transport** | `#F2994A` | Orange |
| **Health & Beauty** | `#27AE60` | Leaf Green |
| **Sport** | `#56CCF2` | Light Blue / Cyan |

### C. Financial Indicators

| Indicator | Hex Code | Usage |
| :--- | :--- | :--- |
| **Income** | `#27AE60` | Incoming transaction numbers (`+$2,775`), positive trend lines. |
| **Expenses** | `#EB5757` | Outgoing transaction numbers (`-$1,634.94`), expense bars. |

---

## 2. Typography

Uses a clean modern sans-serif font with high financial-number legibility (recommended: **Plus Jakarta Sans**, **Inter**, or **Roboto**).

| Typography Level | Size | Weight | Usage Example |
| :--- | :--- | :--- | :--- |
| **Display Metric** | `24px` - `28px` | Bold (`700`) | Main Balance (`$10,157`), Total Amount (`$1,570`) |
| **Screen Title** | `18px` - `20px` | SemiBold (`600`) | Header titles (`Categories`, `View Transactions`) |
| **Section Header** | `15px` - `16px` | Bold (`700`) | "Cash Flow", "Budgets Summary", "Category Summary" |
| **List Title / Coin** | `14px` - `15px` | SemiBold (`600`) | Category names (`Food & Drink`), menu options |
| **Body Amount** | `13px` - `14px` | Medium (`500`) | Transaction amounts (`800.50$`, `+2,775$`) |
| **Caption / Subtext** | `11px` - `12px` | Regular (`400`) | Transaction counts (`2 Transactions`), dates (`05 Tuesday`) |

---

## 3. Elevation & Shadows (Shadow & Elevation)

A subtle elevation system for a lightweight visual feel (*clean & modern look*):

```css
/* Standard Cards & Transaction Items */
box-shadow: 0px 4px 16px rgba(30, 101, 255, 0.06);

/* Primary Account Card & Header Overlay */
box-shadow: 0px 10px 25px rgba(30, 101, 255, 0.22);

/* Floating Action Button (FAB) Center */
box-shadow: 0px 6px 20px rgba(30, 101, 255, 0.40);
```

---

## 4. Corner Softness (Border Radius)

* **Hero Card / Top Header Panel:** `0px 0px 24px 24px` (rounded bottom corners)
* **Inner Floating Panels / Cards:** `20px` - `24px`
* **Category Icon Boxes:** `12px` - `14px` (rounded boxes)
* **Progress Bars / Status Chips:** `8px` or `50px` (capsule)
* **FAB Button:** `50%` (perfect circle)

---

## 5. Main UI Components

### A. Top Header Banner
* Solid `#1E65FF` background with a *header curved bottom*.
* Shows the screen title, *Back* button, and a secondary action button (e.g., calendar icon).

### B. Analytics Charts
1. **Donut Chart (Category Pie Chart):**
   * *Stroke Width:* `16px` - `20px`
   * Shows the total value at the center of the chart (*Center Label*).
2. **Comparison Spline Chart (Line Chart):**
   * Two trend lines (green for *Income*, red for *Expenses*).
   * Focus point (*Data Marker*) as a small shadowed bubble.

### C. Budget & Category Progress Bars
* *Track* background: `#F0F4FA`.
* *Fill* color follows the category identity color (e.g., red for *Food & Drink*, blue for *Shopping*).
* Shows used vs *Remaining Budget* values.

### D. Bottom Navigation Bar with Center FAB
* White (`#FFFFFF`) bottom navigation tab with a curved center *notch*.
* **Floating Action Button (FAB):** Blue `#1E65FF` add (`+`) button floating at the center of the bottom navigation.

---

## 6. Layout & Spacing

* **Page Margin:** `16px` - `20px` (left & right)
* **Vertical Gap (Between Sections):** `16px` - `20px`
* **Item List Padding:** `12px` - `16px`
* **Category Icon Size:** `40px x 40px` with a `20px` internal icon.

---

## 7. Responsive Behavior

*Mobile-first base 360–430px; use the Tailwind scale upward: `sm` ≥640px · `md` ≥768px · `lg` ≥1024px.*

- Base design 360–430px: 1 column, 16–20px margins, full-width cards.
- ≥`sm` (large phones / portrait tablets): max-w-md centered container; donut + legend stacked; category rows 1 column.
- `md` and up (tablets): max-w-lg; bottom-nav + center FAB stay at the bottom.
- Center FAB: always above the bottom-nav with safe-area clearance; must not cover nav items at 360px.
- Safe area: use `env(safe-area-inset-*)` for the header banner, bottom-nav, and FAB.
- Landscape: header banner height ≤40vh; period chips become a horizontal scroll row.
- Dynamic text: support scaling up to 130% without clipping (wrap, avoid fixed heights).
- Touch targets ≥44px with ≥8px gaps between targets.

---

## 8. Motion & Animation

| Token | Value | Used for |
|---|---|---|
| `--motion-fast` | `150ms` | Touch feedback, tab fade |
| `--motion-base` | `250ms` | Screen transitions, sheets |
| `--motion-slow` | `400ms` | Entrance, chart animation |
| `--ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | Default for all motion |
| `--ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | Toggles, progress |

- Screen transitions: 250–300ms ease-out slide-x + fade; back button = reverse direction.
- Budget & category progress bars fill in 500ms ease-out; segmented donut fades in piece by piece.
- FAB morph +/× 200ms + light haptic; FAB action menu staggers 50ms.
- Tab switching: 150ms fade with no sliding, for stability.
- Pull-to-refresh: resistance indicator + spinner; initial data uses a 1200ms skeleton shimmer.
- `prefers-reduced-motion`: replace all slides with a fast 150ms fade; disable shimmer.
