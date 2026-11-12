# Style Design Guidelines

This document defines the design system and visual style guidelines based on the *Get Started / Login* page UI.

---

## 1. Color Palette

The palette follows a modern SaaS style dominated by bright blue as the primary accent, paired with neutral monochrome colors for text and backgrounds.

| Category | Color | HEX Code / Representation | Primary Usage |
| :--- | :--- | :--- | :--- |
| **Primary** | Bright Blue / Royal Blue | `#3B5BDB` (Estimate) | Primary button (CTA), logo icon, right panel background, input focus border. |
| **Neutral Dark** | Charcoal Black / Charcoal | `#1E293B` (Estimate) | Main heading (*Heading*), important text, input labels. |
| **Neutral Gray** | Medium Gray | `#64748B` (Estimate) | Sub-text, descriptions, placeholders, secondary link text (*footer*). |
| **Neutral Light**| Light Gray / Off-White | `#F8FAFC` / `#FFFFFF` | Main page background, form input field (*Input Fields*) background. |
| **Border / Stroke**| Line Gray | `#E2E8F0` (Estimate) | Dividers (*divider*), inactive input borders. |

---

## 2. Typography

Uses a clean, readable modern sans-serif *font family* (similar to *Inter* or *SF Pro*).

*   **Font Family:** `Inter`, `SF Pro Display`, sans-serif
*   **Text Hierarchy:**
    *   **Heading 1 (Page Title):**
        *   Size: ~28px - 32px (Bold / Semibold)
        *   Color: Neutral Dark
    *   **Heading 2 (Right Panel Title):**
        *   Size: ~24px (Bold / Semibold), white on a blue background.
    *   **Body / Sub-heading:**
        *   Size: ~14px (Regular)
        *   Color: Neutral Gray
    *   **Label & Form Text:**
        *   Size: ~12px - 14px (Medium)
    *   **Button Text:**
        *   Size: ~14px (Semibold), white.

---

## 3. Layout & Structure

The design uses a **Split Screen (Two-Column)** approach:
*   **Left Column (~50% width):** Holds the interactive form (Social Login, Name/Email/Password input form, Terms & Conditions checkbox, and the *Login* button).
*   **Right Column (~50% width):** Decorative panel with a *Primary* (Blue) background, showing a promotional headline, an app *dashboard mockup*, and partner/client logos at the bottom.
*   **Main Container Border Radius:** The outer container corners use smooth *rounded corners* (around `16px` - `24px`).

---

## 4. UI Components

### A. Buttons
*   **Primary Button (Login):**
    *   Background: Blue (`#3B5BDB`) with white text.
    *   Shape: Rounded corners (*Rounded*, radius around `8px` - `10px`).
    *   Effect: Has a subtle shadow (*subtle shadow*) for a sense of depth (*elevation*).
*   **Social Login Buttons (Google / Apple):**
    *   Background: White with a thin gray border.
    *   Content: Social media icon to the left of the "Log in with Google" / "Log in with Apple" text.
    *   Shape: Rounded corners (`8px`).

### B. Form Inputs
*   **Input Field:**
    *   Background: White / very light gray.
    *   Border: Thin light-gray border (`#E2E8F0`). When active/focused (*focused*), the border turns primary blue with a subtle *glow* effect.
    *   Corner radius: Rounded (`8px`).
    *   Placeholder: Light gray.
    *   Extra Feature: The *Password* input includes an eye visibility icon on the right side.

### C. Checkbox & Links
*   **Checkbox:** Small box with slightly rounded corners for the "I agree to the Terms & Privacy" consent.
*   **Links:** Text links such as "Forgot password?" and "Sign in" use primary blue with no underline, gaining an underline or darkening slightly on hover.

---

## 5. Visual Assets & Mockups
*   **Dashboard Preview:** Shows a floating analytics dashboard card illustration with a soft *drop shadow* for a professional SaaS product feel.
*   **Footer Logos:** Shows partner company logos (such as WeChat, Booking.com, Google, Spotify, Stripe) in transparent white (monochrome) at the bottom of the right panel.

---

## 6. Responsive Behavior

*Follow the Tailwind breakpoint scale (mobile-first): `sm` ≥640px · `md` ≥768px · `lg` ≥1024px · `xl` ≥1280px.*

| Range | Card | Right panel | Form |
|---|---|---|---|
| `lg` and up (≥1024px) | 50/50 split | Full dashboard preview + partner logos | Fields may use 2 columns where suitable |
| `md` (768–1024px) | Stacked, max-w-md centered | Preview becomes a banner, logos wrap | 1 column |
| Base (<768px) | Full-bleed (0 margin) | Hidden / thin strip | 48px inputs, full-width button |

- When the right panel is hidden, keep the title/brand so context is not lost.
- The dashboard preview + partner logos move below the form under `lg`; logos wrap from 3 to 2 columns on mobile.
- The mobile keyboard must not cover the submit button; the page must be scrollable. Short landscape (<500px): hide the right panel, tighten padding.

---

## 7. Motion & Animation

| Token | Value | Used for |
|---|---|---|
| `--motion-fast` | `150ms` | Hover, focus, field ring |
| `--motion-base` | `250ms` | Panel cross-fade, error messages |
| `--motion-slow` | `400ms` | Card entrance |
| `--ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | Default for all motion |
| `--ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | Symmetric motion |

- Validation errors: NO shake; error message fade-slide 250ms + red ring on the field.
- Submit button: loading = spinner inside the button + disabled; success = fade to the status/next-step instruction.
- Dashboard preview card: gentle float (±6px, 7s ease-in-out); partner logos fade in with a 60ms stagger.
- Login ↔ signup transitions: 250ms cross-fade.
- `prefers-reduced-motion`: all transitions become instant (or a fast 100ms fade).
