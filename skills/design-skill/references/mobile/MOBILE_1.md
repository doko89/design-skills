# Smart Home Mobile App - Style Guide

This visual style guide (*Design System*) is based on the **Smart Home** app user interface (UI). It keeps UI/UX design and *front-end development* implementation consistent.

---

## 1. Colors (Color Palette)

The color scheme follows a **Clean, Soft & Modern Minimalist** concept, blending royal blue (*electric/accent blue*) with a very light neutral background and subtle shadows (*soft elevation*).

### A. Primary & Accent Colors
| Color Name | Hex Code | Primary Usage |
| :--- | :--- | :--- |
| **Primary Blue** | `#2F65F6` | Primary CTA button, active/ON status, active cards, selection indicators. |
| **Light Blue Accent** | `#EAF0FF` | Active icon backgrounds, inactive tabs, secondary containers. |
| **Sky Blue / Soft Accent**| `#D7E5FF` | Secondary interactive element backgrounds, hover/pressed states. |

### B. Neutral Colors
| Color Name | Hex Code | Primary Usage |
| :--- | :--- | :--- |
| **Dark Navy (Main Text)** | `#121E36` | Main headings/titles, high-value text, primary metric numbers. |
| **Slate Gray (Sub Text)** | `#708099` | Secondary text, inactive labels, descriptions, weather/temperature info. |
| **Light Gray Border** | `#E5EBF2` | Dividers, inactive card borders. |
| **App Background** | `#F2F5FA` | Overall app screen background. |
| **Card Surface** | `#FFFFFF` | Card (*cards*), dialog container, and navigation panel backgrounds. |

### C. Status & Functional Colors
| Color Name | Hex Code | Primary Usage |
| :--- | :--- | :--- |
| **Warning / Weather** | `#FFB800` | Weather indicators (sun/cloudy), minor warnings. |
| **Danger / Remove** | `#FF4D4D` | Remove/exit action text (*Remove/Delete action*). |

---

## 2. Typography

Uses a clean, modern **Sans-Serif** font family such as **Inter**, **Plus Jakarta Sans**, or **SF Pro Display**.

| Typography Role | Size | Weight | Line Height | Color |
| :--- | :--- | :--- | :--- | :--- |
| **Display / Metrics** | `28px` - `32px` | Bold (`700`) | `1.2` | `#121E36` / `#FFFFFF` |
| **Screen Title** | `20px` - `22px` | SemiBold (`600`) | `1.3` | `#121E36` |
| **Section Header** | `15px` - `16px` | SemiBold (`600`) | `1.4` | `#121E36` |
| **Card Title / Main Label**| `14px` | Medium (`500`) / SemiBold | `1.4` | `#121E36` |
| **Body Text / Subtitle** | `12px` - `13px` | Regular (`400`) | `1.5` | `#708099` |
| **Small Caption / Metric Sub**| `10px` - `11px` | Regular (`400`) | `1.4` | `#708099` |

---

## 3. Elevation (Shadows & Depth)

The app relies on very subtle shadows (*neomorphic-soft shadow*) to separate component layers from the background.

```css
/* Card Soft Shadow */
box-shadow: 0px 10px 30px rgba(18, 30, 54, 0.05);

/* Active / Floating Element Shadow */
box-shadow: 0px 12px 24px rgba(47, 101, 246, 0.25);
```

---

## 4. Corner Radius (Border Radius)

The design uses highly rounded corners (*high rounded corners*) for a friendly, modern feel.

* **Main App Screen Container:** `32px` - `40px`
* **Cards (Big/Medium):** `24px`
* **Action Buttons & Inputs:** `16px` - `20px`
* **Badges / Small Pills:** `12px` or Fully Rounded (`999px`)
* **Avatar & Circular Toggle:** Fully Rounded (`50%`)

---

## 5. Main Components (UI Components)

### A. Active vs Inactive Card States
* **Active Card State:**
  * Background: `#2F65F6` (Primary Blue)
  * Text Color: `#FFFFFF`
  * Subtext/Icon Color: `#FFFFFF` (opacity 0.8)
* **Inactive Card State:**
  * Background: `#FFFFFF`
  * Border: `1px solid #F2F5FA` (or borderless with a soft shadow)
  * Text Color: `#121E36`
  * Icon Container: `#EAF0FF` or `#F2F5FA`

### B. Toggle Switch
* **Width x Height:** `44px x 24px`
* **ON State:** Track Background `#2F65F6`, Thumb `#FFFFFF` (on the right).
* **OFF State:** Track Background `#E5EBF2`, Thumb `#FFFFFF` (on the left).

### C. Circular Gauge / Chart Loader (Light Bulbs / Usage)
* **Track Gray:** `#EAF0FF` (Thickness: `6px` - `8px`)
* **Progress Indicator:** `#2F65F6`
* **Pointer Knob:** `#2F65F6`, `12px` in diameter with a `3px` white outline.

### D. Navigation Header
* **Back Button:** Left arrow icon (`<`) at `20px` inside a minimum `40px x 40px` touch area.
* **Title:** Centered (*centered*) or left-aligned depending on the page hierarchy context.

---

## 6. Iconography & Media

* **Style:** Outlined/Line Icons with a uniform stroke width of `1.8px` to `2px`.
* **Standard Icon Size:** `20px` x `20px` or `24px` x `24px`.
* **Profile Avatar:** Circle (`50%`) with a subtle `2px` white border.

---

## 7. Layout & Spacing System

Uses an **8px** grid multiple (8, 16, 24, 32, 48).

* **Page Margin (Left/Right):** `20px` or `24px`
* **Item Gap (2-Column Card Grid):** `12px` - `16px`
* **Section Spacing (Vertical):** `24px`
* **Card Internal Padding:** `16px` - `20px`

---

## 8. Responsive Behavior

*Mobile-first base 360–430px; use the Tailwind scale upward: `sm` ≥640px · `md` ≥768px · `lg` ≥1024px.*

- Base design 360–430px: 1 column, 20–24px margins, full-width cards.
- ≥`sm` (large phones / portrait tablets): max-w-md centered container; device grid stays 2 columns down to 360px; circular gauge shrinks proportionally.
- `md` and up (tablets): max-w-lg; bottom navigation stays, max 5 items.
- Safe area: use `env(safe-area-inset-*)` for the header, bottom nav, and floating elements.
- Landscape: banner/hero height ≤40vh; chips/actions become a horizontal scroll row.
- Dynamic text: support scaling up to 130% without clipping (wrap, avoid fixed heights).
- Touch targets ≥44px with ≥8px gaps between targets.

---

## 9. Motion & Animation

| Token | Value | Used for |
|---|---|---|
| `--motion-fast` | `150ms` | Touch feedback, tab fade |
| `--motion-base` | `250ms` | Screen transitions, sheets |
| `--motion-slow` | `400ms` | Entrance, chart animation |
| `--ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | Default for all motion |
| `--ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | Toggles, progress |

- Screen transitions: 250–300ms ease-out slide-x + fade; back button = reverse direction.
- Tab switching: 150ms fade with no sliding, for stability.
- Toggle: 200ms ease-in-out knob + light haptic; active↔inactive card color transition 200ms.
- Circular gauge: needle/progress fills in 400ms ease-out when the value changes.
- Pull-to-refresh: resistance indicator + spinner; initial data uses a 1200ms skeleton shimmer.
- `prefers-reduced-motion`: replace all slides with a fast 150ms fade; disable shimmer.
