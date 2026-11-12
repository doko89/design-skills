# Design System & Style Guide: Sign Up UI

This document contains the design style guide and visual specifications extracted from the *Sign Up* page interface.

---

## 1. Color Palette

### Primary & Accent Colors
* **Primary Blue/Indigo**: `#6C72FF` or `#7075FF` *(used for the Primary Button)*
* **Primary Hover / Deep Blue**: `#5A60E0`
* **Success / Indicator Icon**: `#8D9BFF` or `#7A88FF` *(used on the validation checkmark icon)*

### Background Colors
* **Outer Canvas Background**: `#8A95FF` to `#7B88FF` *(soft purplish/bluish gradient)*
* **Modal / Card Background**: `#FFFFFF` *(clean white)*
* **Secondary / Social Button BG**: `#FFFFFF` *(with a soft shadow)*
* **Decorative Shapes**: `#E3E7FF` / `#DCE1FF` with transparency (opacity ~30-50%)

### Typography Colors
* **Heading Text**: `#515589` / `#4A4D7A` *(dark indigo/slate blue)*
* **Subheading / Label Text**: `#A5A7C3` / `#9CA0C2` *(muted purplish gray)*
* **Input Text**: `#4A4E69`
* **Divider Text / Secondary Links**: `#B0B3C9`
* **Link Active Highlight**: `#5B61E6` *("Sign in" text)*

---

## 2. Typography

* **Primary Font Family**: Modern, clean, friendly-looking sans-serif (recommended: `Inter`, `Plus Jakarta Sans`, or `Poppins`).

### Text Hierarchy
* **Title (Sign up)**:
  * Size: `28px` - `32px`
  * Weight: `Bold` (700)
  * Line Height: `1.2`
  * Color: Heading Text (`#515589`)
* **Subtitle (Join the community today!)**:
  * Size: `14px` - `16px`
  * Weight: `Regular` (400)
  * Color: Label Text (`#A5A7C3`)
* **Form Labels (Email, Password)**:
  * Size: `12px` - `13px`
  * Weight: `Medium` (500)
  * Color: Label Text (`#A5A7C3`)
* **Input Values**:
  * Size: `14px`
  * Weight: `Medium` (500)
  * Color: Input Text (`#4A4E69`)
* **Button Text**:
  * Size: `15px`
  * Weight: `Semi-Bold` (600)
  * Color: `#FFFFFF`
* **Footer Text / Links**:
  * Size: `13px` - `14px`
  * Weight: `Regular` / `Semi-Bold` (Link)

---

## 3. UI Components

### A. Modal / Card Container
* **Border Radius**: `24px` or `30px` *(modern rounded corners)*
* **Box Shadow**: `0px 20px 40px rgba(0, 0, 0, 0.08)`
* **Background**: `#FFFFFF`
* **Aspect Ratio / Padding**: Symmetrically structured with generous internal padding (`padding: 48px 64px`).

### B. Social Login Button (Google)
* **Height**: `48px`
* **Width**: `100%` / max-width `320px`
* **Border Radius**: `24px` (Fully rounded / pill shape)
* **Background**: `#FFFFFF`
* **Box Shadow**: `0px 4px 12px rgba(108, 114, 255, 0.12)`
* **Layout**: Centered flexbox (Icon + Label)

### C. Form Input Fields (Line/Minimalist Style)
* **Style**: Underline / Bottom Border only
* **Border Bottom**: `1.5px solid #E2E5F1`
* **Focus State**: `1.5px solid #6C72FF`
* **Indicator Icons**: Circle icon on the right side of the input (`20px x 20px`) in `#8D9BFF` with a white checkmark symbol.
* **Spacing**: `24px` gap between fields.

### D. Primary Button (Sign Up)
* **Height**: `48px`
* **Border Radius**: `24px` (Pill shape)
* **Background**: `#6C72FF`
* **Box Shadow**: `0px 8px 20px rgba(108, 114, 255, 0.35)`
* **Hover State**: Background `#5A60E0`, slight scale up (`transform: scale(1.01)`).

---

## 4. Visual & Decorative Elements

* **Soft Abstract Circles**:
  * Semi-transparent circles (`opacity: 0.3 - 0.5`) at the bottom-left and top-right corners of the page for a soft, dynamic visual effect.
* **Divider**:
  * A subtle centered "or" text with a thin line or flexible margins.

---

## 5. Tailwind CSS Implementation (Quick Reference)

```html
<!-- Card Frame -->
<div class="bg-white rounded-3xl shadow-2xl p-12 max-w-lg w-full text-center relative overflow-hidden">
  
  <!-- Title & Subtitle -->
  <h1 class="text-3xl font-bold text-[#515589] mb-1">Sign up</h1>
  <p class="text-sm text-[#A5A7C3] mb-8">Join the community today!</p>

  <!-- Google Auth Button -->
  <button class="w-full py-3 px-6 rounded-full bg-white shadow-md hover:shadow-lg flex items-center justify-center gap-3 text-[#A5A7C3] font-medium transition-all mb-6">
    <img src="google-icon.svg" class="w-5 h-5" alt="Google" />
    <span>Use Google account</span>
  </button>

  <!-- Divider -->
  <span class="text-xs text-[#B0B3C9] block mb-6">or</span>

  <!-- Inputs -->
  <div class="space-y-6 text-left mb-8">
    <div class="border-b-2 border-gray-200 pb-2 relative">
      <label class="block text-xs text-[#A5A7C3] mb-1">Email</label>
      <input type="email" class="w-full bg-transparent outline-none text-[#4A4E69] text-sm" value="pozingis.laimonas@gmail.com">
      <span class="absolute right-0 bottom-2 bg-[#8D9BFF] text-white rounded-full p-1 text-xs">✓</span>
    </div>
  </div>

  <!-- Submit Button -->
  <button class="w-full py-3.5 rounded-full bg-[#6C72FF] hover:bg-[#5A60E0] text-white font-semibold shadow-lg shadow-[#6C72FF]/30 transition-all">
    Sign up
  </button>
</div>
```

---

## 6. Responsive Behavior

*Follow the Tailwind breakpoint scale (mobile-first): `sm` ≥640px · `md` ≥768px · `lg` ≥1024px · `xl` ≥1280px.*

| Range | Card | Illustration | Form |
|---|---|---|---|
| `lg` and up (≥1024px) | Split/centered modal max-w-4xl | Full | Fields may use 2 columns where suitable |
| `md` (768–1024px) | Stacked, max-w-md centered | Top banner ≤220px or hidden | 1 column |
| Base (<768px) | Full-screen sheet (0 margin) | Hidden / thin strip | 48px inputs, full-width button |

- When the illustration is hidden, keep the title/brand so context is not lost.
- The modal becomes a full-screen sheet below `md`; Google button full-width; fields stack in 1 column.
- The mobile keyboard must not cover the submit button; the page must be scrollable. Short landscape (<500px): hide the illustration, tighten padding.

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
- Modal entrance: scale 0.96→1 + 250ms fade; social button hover-lift 150ms.
- Login ↔ signup transitions: 250ms cross-fade.
- `prefers-reduced-motion`: all transitions become instant (or a fast 100ms fade).
