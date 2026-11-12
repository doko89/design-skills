# Style Design Guidelines: Adminator Login Interface

This document defines the design system and visual style guidelines based on the **Adminator** login page interface.

---

## 1. Color Palette

This design blends a modern gradient on the hero/branding side with a very clean neutral background on the interactive form section.

| Category | Color / Gradient | HEX Code (Estimate) | Primary Usage |
| :--- | :--- | :--- | :--- |
| **Primary Accent** | Royal Electric Blue | `#2563EB` | Primary button (Sign in), filled checkbox, active action text. |
| **Hero Gradient Start** | Vivid Blue | `#3B82F6` | Top-left side of the hero panel background. |
| **Hero Gradient End** | Indigo / Violet | `#6D28D9` / `#7C3AED` | Bottom-right side of the hero panel background. |
| **Background Light** | Off-White / Soft Gray | `#F3F4F6` / `#F8FAFC` | Main background of the form section (right column). |
| **Card / Glass Tint** | Translucent White | `rgba(255, 255, 255, 0.15)` | Testimonial box on the hero panel (*glassmorphism effect*). |
| **Text Dark** | Deep Charcoal | `#111827` | Main heading (*Welcome back*), important text labels. |
| **Text Muted** | Slate Gray | `#6B7280` | Descriptions, placeholders, footer text, *divider labels*. |
| **Text Light / White** | Pure White | `#FFFFFF` | Text on the hero panel, input card background, primary button. |
| **Border / Line** | Light Gray | `#E5E7EB` | Dividers (*divider*), social media button borders. |

---

## 2. Typography

The typography uses a very clean and structured modern/geometric *sans-serif* style.

*   **Font Family:** `Inter`, `Plus Jakarta Sans`, or `System Sans-Serif`.
*   **Text Hierarchy:**
    *   **Hero Display Title:**
        *   Size: `~36px` - `40px` | *Weight:* **Bold (700)** | *Leading:* `1.2`
        *   Color: `#FFFFFF`
    *   **Form Heading (Welcome Back):**
        *   Size: `~30px` - `32px` | *Weight:* **Bold (700)**
        *   Color: `#111827`
    *   **Body Text / Hero Subtitle:**
        *   Size: `~14px` - `16px` | *Weight:* **Regular (400)**
        *   Color: `rgba(255, 255, 255, 0.8)` (Hero) / `#6B7280` (Form)
    *   **Mono / Badge Text (2026 . V3.1 PREVIEW):**
        *   Size: `~12px` | *Weight:* **Medium (500)** | *Letter Spacing:* Uppercase / Wide
    *   **Labels & Buttons:**
        *   Size: `~13px` - `14px` | *Weight:* **Semi-Bold (600)**

---

## 3. Layout & Grid

Uses a **Full-Height Split Screen (50/50 Layout)** pattern:

*   **Left Panel (Hero & Branding Area - 50%):**
    *   Striking blue-to-purple gradient background.
    *   Vertical arrangement (*Flexbox Column / Space-between*):
        *   **Header:** Logo & Brand Name (*Adminator*).
        *   **Center:** Tagline, product description, and *Testimonial Card*.
        *   **Footer:** Version and location info (*2026 . BUILT IN RIGA, LV*).
*   **Right Panel (Form Input Area - 50%):**
    *   Integrated neutral background.
    *   Centered arrangement (*Centered Content*) with a maximum width limit (*Max-width* ~`400px`).
    *   **Top Bar Header:** Navigation links (*Back to home*, *Create account*).

---

## 4. Components & UI Elements

### A. Testimonial Card (Glassmorphism Effect)
*   **Background:** Frosted transparent pattern (`backdrop-filter: blur(12px)` with `background: rgba(255, 255, 255, 0.12)`).
*   **Border:** `1px solid rgba(255, 255, 255, 0.2)`.
*   **Border Radius:** `16px`.
*   **Content:** Translucent white quote text and an initial avatar (*SK - Sara Kim*).

### B. Form Input Fields
*   **Style:** Clean White Card background with a very thin border.
*   **Icons:** *Inline* icons to the left of the placeholder (envelope icon for Email, lock icon for Password).
*   **Border Radius:** `10px` - `12px`.
*   **Focus State:** 2px blue ring when active.

### C. Buttons
*   **Primary CTA (Sign in):**
    *   Color: Vibrant Blue (`#2563EB`).
    *   Content: Text + Right Arrow Icon (`Sign in →`).
    *   Border Radius: `10px`.
*   **Social Login Buttons (Google, GitHub, Apple):**
    *   Color: White with a thin gray border (`#E5E7EB`).
    *   Layout: 3 side-by-side columns (*Grid/Flex Row*).
    *   Content: Platform logo + platform name.

### D. Checkbox & Links
*   **Checkbox:** Rounded corners (*Rounded Checkbox*) with a blue accent color when active.
*   **Links:** Blue accent color with no *underline* for primary actions (*Create account*, *Forgot?*).

---

## 5. Micro-interactions & Spacing

*   **Corner Radius Standard:**
    *   Small (Input/Buttons): `8px` - `10px`
    *   Medium (Cards/Containers): `16px`
*   **Form Padding:** Loose vertical spacing (`gap: 16px` to `24px`) gives an easy-to-read visual rhythm.

---

## 6. Responsive Behavior

*Follow the Tailwind breakpoint scale (mobile-first): `sm` ≥640px · `md` ≥768px · `lg` ≥1024px · `xl` ≥1280px.*

| Range | Card | Testimonial | Form |
|---|---|---|---|
| `lg` and up (≥1024px) | 50/50 split | Full glass testimonial | Fields may use 2 columns where suitable |
| `md` (768–1024px) | Stacked, max-w-md centered | Condensed/hidden testimonial | 1 column |
| Base (<768px) | Full-bleed (0 margin) | Hidden | 48px inputs, full-width button |

- When the testimonial card is hidden, keep the title/brand so context is not lost.
- The glassmorphism testimonial card hides below `lg`; form is max-w-md centered with a 16–24px gap.
- The mobile keyboard must not cover the submit button; the page must be scrollable. Short landscape (<500px): tighten padding.

---

## 7. Motion & Animation

*These duration tokens complement Section 5 (micro-interactions): radius & spacing live there, timing & easing live here.*

| Token | Value | Used for |
|---|---|---|
| `--motion-fast` | `150ms` | Hover, focus, field ring |
| `--motion-base` | `250ms` | Panel cross-fade, error messages |
| `--motion-slow` | `400ms` | Card entrance |
| `--ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | Default for all motion |
| `--ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | Symmetric motion |

- Validation errors: NO shake; error message fade-slide 250ms + red ring on the field.
- Submit button: loading = spinner inside the button + disabled; success = fade to the status/next-step instruction.
- Glass card: Do NOT animate the blur value; fade-slide position/opacity only (250–400ms).
- Login ↔ signup transitions: 250ms cross-fade.
- `prefers-reduced-motion`: all transitions become instant (or a fast 100ms fade).
