# Personal Finance Mobile App - Style Guide

This *Design System* document is designed specifically around the **Personal Finance & Expense Tracker** app interface with its *Vibrant Deep Purple & Soft Coral* feel. It sets visual and technical standards to keep UI/UX and interface (*front-end*) development consistent.

---

## 1. Color Palette

The app carries a *Deep Purple* palette as its dominant color with *Coral/Pink* accents and soft pastel elements for a cheerful, modern, intuitive feel.

### A. Primary & Interface Colors

| Color Name | Hex Code | Primary Usage |
| :--- | :--- | :--- |
| **Deep Electric Purple** | `#5B00D2` | Primary balance card, primary action button (FAB), memo header, active-identified buttons. |
| **Soft Lilac / Purple Tint** | `#ECE4FF` | Active cards/icons (e.g., the `Device` category), inactive tab toggles. |
| **Soft Coral / Pink** | `#FF497C` | *Expenses* graphic accents, *donut chart*, negative trend indicators. |
| **Primary Text (Dark Charcoal)** | `#1E1E2F` | Screen titles, transaction amount text, keypad numbers. |
| **Muted / Secondary Text** | `#A0A0B2` | Sub-text (dates, inactive categories), day/chart labels. |
| **App Background** | `#F9F9FE` | App base background (*Light Mode*). |
| **Surface White** | `#FFFFFF` | Transaction card backgrounds, input panels, modal sheets. |

### B. Categorical Colors (Donut Chart & Category Icons)

Used specifically to distinguish transaction categories and expense statistics:

| Category | Hex Code | Visual Representation |
| :--- | :--- | :--- |
| **Shopping / Primary Chart** | `#5B00D2` | Deep Purple |
| **Device / Expense Chart** | `#FF497C` | Soft Coral / Pink |
| **Grocery / Accent Chart** | `#FFA3C8` | Light Pastel Pink |
| **Salary / Allowance Icon** | `#6CE5C8` | Soft Mint Green |
| **Other / Empty Chart Track** | `#E5E5EF` | Light Grey |

---

## 2. Typography

Uses a round, clean modern sans-serif font (recommended: **Plus Jakarta Sans**, **Poppins**, or **Inter**).

| Typography Level | Size | Weight | Usage Example |
| :--- | :--- | :--- | :--- |
| **Display Metric** | `26px` - `28px` | Bold (`700`) | Main Balance (`IDR 7.736.000`) |
| **Screen Title** | `18px` - `20px` | Bold (`700`) | Screen headers (`Expenses`, `October - Week 3`) |
| **Section Header** | `15px` - `16px` | Bold (`700`) | `Recent transactions`, `Total Ballance` |
| **Card / List Title** | `14px` - `15px` | SemiBold (`600`) | Transaction names (`WiFi TP-Link N300`, `Bomber Jacket`) |
| **Body / Amount** | `13px` - `14px` | SemiBold (`600`) | Transaction amounts (`- 324.000`, `+ 8.500.000`) |
| **Caption / Subtext** | `11px` - `12px` | Regular (`400`) | Sub-details (`Device`, `Today`, `Welcome back`) |
| **Keypad Numbers** | `22px` - `24px` | Medium (`500`) | Numbers on the custom keypad (`1-9`, `0`) |

---

## 3. Elevation & Shadows (Shadow & Elevation)

The elevation system focuses on the primary card and floating buttons for visual depth:

```css
/* Main Balance Card & FAB Button */
box-shadow: 0px 10px 24px rgba(91, 0, 210, 0.25);

/* Soft Card / Item List */
box-shadow: 0px 4px 12px rgba(30, 30, 47, 0.03);

/* Toggle Switch / Category Active Indicator */
box-shadow: 0px 4px 10px rgba(91, 0, 210, 0.15);
```

---

## 4. Corner Softness (Border Radius)

* **Main Balance Card:** `24px` (highly rounded corners)
* **Custom Keypad Panel / Top Header:** `20px` - `24px`
* **Category Icon Boxes:** `14px` (Rounded Square)
* **Toggle Bar (Income/Expenses Switch):** `50px` (Full Capsule)
* **Floating Action Button (FAB):** `50%` (Circle)

---

## 5. Main UI Components

### A. Top Balance Card
* Solid `#5B00D2` card with a transparent curved pattern background (*subtle wave overlay*).
* Has an *Income* and *Expenses* summary at the bottom of the card with small indicator arrows.

### B. Segmented Toggle Control (Income / Expenses)
* Capsule with a white `#FFFFFF` or `#F0F0F7` background.
* The selected item is a `#5B00D2` capsule with white text.

### C. Bar & Donut Analytics Chart
* **Donut Chart:** `14px` - `16px` stroke thickness combining purple, coral, and pink.
* **Dual-Color Bar Chart:** Vertical bars split into 2 colors (purple on top for *Income*, pink/coral below for *Expenses*).

### D. Category Grid Selectors
* 3-column grid for picking category icons (`Medice`, `House`, `Shopping`, `Device`, etc.).
* **Active state:** Background turns `#ECE4FF` with a `#5B00D2` icon.

### E. Custom Numpad / Keypad Input
* Memo/amount display with a `#5B00D2` header and right-side cursor.
* 3x4 number button grid with no box borders, for a *clean & minimalist* feel.

---

## 6. Layout & Spacing

* **Page Margins:** `20px` (left & right)
* **Grid Spacing (Category Icons):** `16px`
* **List Item Vertical Gap:** `12px`
* **Icon Size Standard:** `24px` inside a `44px x 44px` container.

---

## 7. Responsive Behavior

*Mobile-first base 360–430px; use the Tailwind scale upward: `sm` ≥640px · `md` ≥768px · `lg` ≥1024px.*

- Base design 360–430px: 1 column, 20px margins, full-width cards.
- ≥`sm` (large phones / portrait tablets): max-w-md centered container; category grid 4 columns; numpad full-width at the bottom.
- At 360px: category grid goes 4→3 columns so icons stay ≥44px; numpad docks at the bottom with safe-area.
- `md` and up (tablets): max-w-lg; bottom navigation stays, max 5 items.
- Safe area: use `env(safe-area-inset-*)` for the header, numpad, and other bottom elements.
- Landscape: numpad + summary may sit side by side (2 columns) when height <500px.
- Dynamic text: support scaling up to 130% without clipping (wrap, avoid fixed heights).
- Touch targets ≥44px; numpad buttons at least 64px with ≥8px gaps between buttons.

---

## 8. Motion & Animation

| Token | Value | Used for |
|---|---|---|
| `--motion-fast` | `150ms` | Touch feedback, tab fade |
| `--motion-base` | `250ms` | Screen transitions, toggle indicator |
| `--motion-slow` | `400ms` | Entrance, chart animation |
| `--ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | Default for all motion |
| `--ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | Toggles, progress |

- Screen transitions: 250–300ms ease-out slide-x + fade; back button = reverse direction.
- Numpad buttons: 0.95 press-scale + light haptic; digits appear instantly with no delayed animation.
- Income/Expenses toggle: indicator slides in 250ms ease-in-out; bar/donut charts redraw in 250ms.
- Category grid: selection = badge scale-in 150ms; tab switching: 150ms fade with no sliding.
- Pull-to-refresh: resistance indicator + spinner; initial data uses a 1200ms skeleton shimmer.
- `prefers-reduced-motion`: replace all slides with a fast 150ms fade; disable shimmer.
