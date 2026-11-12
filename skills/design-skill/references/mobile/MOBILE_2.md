# FinTech Mobile App - Style Guide

This visual style guide (*Design System*) is based on the **FinTech / Mobile Banking** app interface. It serves as a reference for the UI/UX team and (*front-end*) developers to ensure visual consistency, component structure, and *user experience*.

---

## 1. Color Palette

Uses a **Royal Purple** combination as the primary identity for a modern, secure, premium feel, paired with **Vibrant Yellow** as the accent color for important elements/CTAs.

### A. Primary & Accent Colors

| Color Name | Hex Code | Primary Usage |
| :--- | :--- | :--- |
| **Primary Purple** | `#5B25D9` | Hero card background, header analytics, active status bar, primary elements. |
| **Deep Violet** | `#4517AF` | Gradient on credit/balance cards, background depth elements (*depth*). |
| **Accent Yellow** | `#FFDB5C` | Quick amount chips (`$150`), active filter pillars/buttons (`Jul to Dec`), visual highlights. |
| **Soft Purple Tint** | `#F3EFFF` | Action icon backgrounds, inactive tabs, secondary badges. |

### B. Neutral Colors

| Color Name | Hex Code | Primary Usage |
| :--- | :--- | :--- |
| **Dark Charcoal (Main Text)** | `#1E1F24` | Transaction titles, primary numeric amounts, recipient names. |
| **Muted Slate (Sub Text)** | `#8F94A3` | Secondary info labels, sub-header text, time/clock, transaction status. |
| **App Background** | `#F7F8FC` | Main background of all app screens. |
| **Card Surface** | `#FFFFFF` | Transaction list backgrounds, modal pop-ups, secondary cards. |

### C. Status & Semantic Colors

| Color Name | Hex Code | Primary Usage |
| :--- | :--- | :--- |
| **Soft Red (Sent)** | `#FF8A8A` / `#FFEAEA` | Outgoing transaction status badge ("Sent"). |
| **Soft Green (Received)** | `#4CD964` / `#EAFCEB` | Incoming transaction status badge ("Received"). |

---

## 2. Typography

Uses a modern sans-serif font with high legibility (recommended: **Plus Jakarta Sans**, **Inter**, or **SF Pro Display**).

| Typography Role | Size | Weight | Line Height | Usage Example |
| :--- | :--- | :--- | :--- | :--- |
| **Display Metric** | `28px` - `32px` | Bold (`700`) | `1.2` | Main Balance (`$17,000`), Analytics (`$12,000`) |
| **Screen Title** | `18px` - `20px` | SemiBold (`600`) | `1.3` | "Analytics", "Send Money", "Your Cards" |
| **Section Header** | `15px` - `16px` | SemiBold (`600`) | `1.4` | "Operations", "Transactions", "Current Dynamic" |
| **Card Title / Name** | `14px` | SemiBold (`600`) | `1.4` | Contact names ("Daniel Alexander"), card types |
| **Body / Label Text** | `12px` - `13px` | Medium (`500`) | `1.4` | Operation labels ("Transfer", "Withdraw"), filter chips |
| **Caption / Status** | `10px` - `11px` | Regular (`400`) | `1.3` | Status badges ("Sent", "Received"), dates |

---

## 3. Elevation & Shadows

The design uses subtle depth with a *multi-layered soft shadow* style.

```css
/* Cards & Lists Elevation */
box-shadow: 0px 8px 24px rgba(91, 37, 217, 0.06);

/* Floating Hero Card & Active Accent Elevation */
box-shadow: 0px 14px 32px rgba(91, 37, 217, 0.22);

/* Quick Nominal Chip Accent Shadow */
box-shadow: 0px 6px 16px rgba(255, 219, 92, 0.4);
```

---

## 4. Corner Softness (Border Radius)

* **Hero Cards / Main Purple Panels:** `28px` - `32px`
* **Container Cards & Lists:** `20px` - `24px`
* **Pills / Quick Buttons / Badges:** `14px` - `16px` or Full Rounded (`999px`)
* **Avatar & Circle Button:** Full Rounded (`50%`)

---

## 5. Main UI Components

### A. Hero Card (Balance & Wallet Overview)
* **Background:** Vertical/diagonal gradient from `#5B25D9` to `#4517AF`.
* **Decorative Elements:** Transparent textured curved waves (*organic wave patterns*) on the card background.
* **Text:** White (`#FFFFFF`) with `80%` transparency for sub-header labels.

### B. Quick Operations Bar
* **Icon Container:** Rounded box (`16px`) in white/light purple (`#F3EFFF`).
* **Icons:** *Line-art style* in purple (`#5B25D9`).
* **Label:** Placed directly below the icon in neutral gray (`#8F94A3`).

### C. Floating Quick Amount Pills
* **Background:** Yellow accent (`#FFDB5C`).
* **Text:** Bold `14px`, dark color (`#1E1F24`).
* **Position:** Floating (*overlapping*) on the boundary between the Hero Card and the content section below.

### D. Analytics Chart & Dynamic Bar
* **Line Graph:** Smooth curve (*smooth bezier spline*) in white with circular *data nodes*.
* **Filter Pills:** Active time filter buttons use a yellow background (`#FFDB5C`) with highly rounded corners.
* **Progress Dynamic Bar:** Horizontal indicator bar for *Income* and *Outcome* with yellow & purple fills.

### E. Transaction List Item
* **Layout:** Horizontal row (*flex row*) arranged as: `[Avatar] + [Name & Status] + [Amount]`.
* **Badges:** Small "Sent" label (pink background) or "Received" label (light green background) under the contact name.

---

## 6. Layout & Spacing System

Uses an **8px**-based grid system.

* **Page Padding (Left/Right):** `20px`
* **Gap Between Cards (Vertical Gap):** `16px` - `20px`
* **Card Internal Padding:** `16px` - `24px`
* **Gap Between Transaction Items:** `12px`

---

## 7. Responsive Behavior

*Mobile-first base 360–430px; use the Tailwind scale upward: `sm` ≥640px · `md` ≥768px · `lg` ≥1024px.*

- Base design 360–430px: 1 column, 20px padding, full-width cards.
- ≥`sm` (large phones / portrait tablets): max-w-md centered container; amount pills wrap to 2 rows; balance hero card full-width.
- `md` and up (tablets): max-w-lg; bottom navigation stays, max 5 items.
- Safe area: use `env(safe-area-inset-*)` for the header, bottom nav, and floating elements.
- Landscape: balance hero height ≤40vh; quick operations bar becomes a horizontal scroll row.
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
- Balance numbers: 500ms count-up when the screen opens or the balance changes.
- Analytics bar chart grows from the baseline in 400ms; transaction items slide in with a 40ms stagger.
- Amount pills: 0.95 press-scale + light haptic.
- Pull-to-refresh: resistance indicator + spinner; initial data uses a 1200ms skeleton shimmer.
- `prefers-reduced-motion`: replace all slides with a fast 150ms fade; disable shimmer.
