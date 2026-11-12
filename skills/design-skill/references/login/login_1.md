# Style Design System - Night Sky Login UI

This document contains the design style guide (*design system*) for the web and app login screen (*Login Screen / Authentication Card*) interface, adapted directly from the *Night Sky & Purple Gradient* themed UI design.

---

## 1. Color Palette

The color theme is dominated by modern purple (*purple/violet*) tones paired with warm yellow/gold accents (*warm yellow/gold*) and clean white contrast.

| Category | Color Name | Hex Value (Estimate) | Primary Usage |
| :--- | :--- | :--- | :--- |
| **Primary Base** | Deep Purple / Violet | `#6B46C1` / `#5B3CC4` | Main left background, *Login* action button, and focus elements. |
| **Primary Dark** | Midnight Purple | `#2D1B69` / `#1A0B40` | Night illustration color, night-sky background elements. |
| **Accent / Highlight** | Warm Sun Gold | `#FFB800` / `#F59E0B` | Moon/sun illustration, highlight points. |
| **Background Body** | Soft Purple Gray | `#805AD5` / `#7C4DFF` | Outer workspace background. |
| **Card Surface** | Pure White | `#FFFFFF` | Login form card background on the right side. |
| **Text Primary** | Deep Indigo | `#3C2A70` | Greeting heading (*"Hello! Good Morning"*), primary button label. |
| **Text Secondary** | Muted Violet / Gray | `#8E82B5` / `#A098C8` | Input placeholder text, secondary description text, and footer tip. |

---

## 2. Typography

Uses a modern sans-serif typeface with varied weights to create a clear visual hierarchy between the greeting message, form labels, and helper text.

* **Recommended Font Family:** Poppins, Plus Jakarta Sans, or Inter.
* **Text Hierarchy:**
  * **Greeting Heading (H1):** 28px – 32px | Bold (`700`) / Semi-Bold (`600`) | Deep Indigo (`#3C2A70`).
  * **Sub-Heading / Form Title:** 16px – 18px | Medium (`500`) | Indigo.
  * **Input Placeholder / Label:** 13px – 14px | Regular (`400`) | Muted Violet (`#8E82B5`).
  * **Button Text:** 14px – 16px | Medium (`500`) | White (`#FFFFFF`).
  * **Small Link / Footer Tip:** 11px – 12px | Regular (`400`) / Medium (`500`).

---

## 3. UI Components & Visual Elements (UI Components)

### A. Container & Card (*Card & Container*)
* **Split Layout Card:** The main card is split into two balanced halves (50% visual illustration on the left, 50% login form on the right).
* **Border Radius:**
  * Main Container: `20px` (`rounded-2xl`) to `24px` (`rounded-3xl`).
  * Form Field / Input: Minimalist with an underline (*underline style*) or a softly rounded box `8px`.
  * Button: `10px` – `12px` (`rounded-xl`).
* **Elevation & Shadows:**
  * The center card uses a soft layered drop shadow: `box-shadow: 0px 20px 50px rgba(45, 27, 105, 0.25);`.

### B. Form & Buttons (*Form Inputs & Buttons*)
* **Input Style (Minimalist Underline):**
  * Subtle underline in gray/light violet (`#E2E8F0` / `#D6BCFA`).
  * Placeholder text aligned above the line.
* **Primary Button (Login):**
  * Solid purple background (`#5B3CC4`), relatively full width within the form area.
  * *Hover* effect: brightness shift (+5%) or soft elevation.
* **Interactive Links:**
  * *"Forget password?"* sits at the bottom-right of the password field in small secondary-purple text.
  * *"Create Account"* sits below the login button, symmetrically centered.

### C. Illustration & Visual Vibe (*Visual & Vector Style*)
* **Illustration Style:** *Flat vector illustration* with a night landscape theme (*Night Landscape / Celestial Theme*).
* **Graphic Elements:**
  * A glowing warm-gold moon centered in a starry night-sky circle.
  * Silhouettes of hills, pine trees, and clouds in *vector layer* style.
  * A meteor/shooting star crossing diagonally.

---

## 4. Layout & Responsive Layout (*Layout Architecture*)

1. **Outer Viewport:**
   * The whole page uses a soft purple gradient background with the login card exactly centered (*center-aligned flexbox / grid*).

2. **Split Card Architecture:**
   * **Left Side (Illustration Section):**
     * Dark purple/night background.
     * Centered vector illustration at the top.
     * Inspirational sub-text at the bottom (*"Login your Account to get full User Experience"* & *"Tip: Upgrade your Account..."*).
   * **Right Side (Authentication Section):**
     * Clean white background for maximum focus on data input.
     * *Left-aligned* text orientation for the opening greeting (*"Hello! Good Morning"*).
     * Centered form area (*padded container*) holding the Username and Password fields, Forgot Password link, Login button, and Create Account option.

### Breakpoints & Screen Adaptation

*Follow the Tailwind breakpoint scale (mobile-first): `sm` ≥640px · `md` ≥768px · `lg` ≥1024px · `xl` ≥1280px.*

| Range | Card | Illustration | Form |
|---|---|---|---|
| `lg` and up (≥1024px) | 50/50 split | Full | Fields may use 2 columns where suitable |
| `md` (768–1024px) | Stacked, max-w-md centered | Top banner ≤220px or hidden | 1 column |
| Base (<768px) | Full-bleed (0 margin) | Hidden / thin strip | 48px inputs, full-width button |

- When the illustration is hidden, keep the title/brand so context is not lost.
- The night-sky panel becomes a top banner on `md` and hides at base; underline inputs keep a 48px touch area.
- The mobile keyboard must not cover the submit button; the page must be scrollable. Short landscape (<500px): hide the illustration, tighten padding.

---

## 5. Motion & Animation

| Token | Value | Used for |
|---|---|---|
| `--motion-fast` | `150ms` | Hover, focus, field ring |
| `--motion-base` | `250ms` | Panel cross-fade, error messages |
| `--motion-slow` | `400ms` | Card entrance |
| `--ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | Default for all motion |
| `--ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | Symmetric motion |

- Validation errors: NO shake; error message fade-slide 250ms + red ring on the field.
- Submit button: loading = spinner inside the button + disabled; success = fade to the status/next-step instruction.
- Login ↔ signup transitions: 250ms cross-fade.
- Stars/meteors: very subtle motion (small opacity/translate, loop ≥8s); disable entirely under `prefers-reduced-motion`.
- `prefers-reduced-motion`: all transitions become instant (or a fast 100ms fade).
