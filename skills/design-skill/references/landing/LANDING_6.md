# Style Design System - Healthcare / Hospital Landing Page

This document contains the design style guide (*design system*) for a web-based healthcare, hospital, or medical clinic platform UI, adapted directly from the **Anaverse Hospital** landing page.

---

## 1. Color Palette

The theme blends clean, trustworthy **Royal Blue / Clinical Blue** with soft gradients and safe contrast accents for the medical and healthcare industry.

| Category | Color Name | Hex Value (Estimate) | Primary Usage |
| :--- | :--- | :--- | :--- |
| **Primary** | Hospital Blue | `#1652E2` | Primary button (*CTA*), active links, priority badges, bottom header banner. |
| **Primary Dark** | Deep Royal Navy | `#0B1F4F` | Main heading text (*headings*), hospital name, dark section backgrounds. |
| **Background Light**| Soft Ice Tint | `#F2F6FE` | Overall page background (*body bg*), secondary cards, transparent badges. |
| **Surface / Card** | Pure White | `#FFFFFF` | Doctor card containers, news cards, service cards, and modals. |
| **Text Muted** | Cool Gray / Slate | `#5A6A85` | Sub-text, short descriptions, date info, doctor specialties. |
| **Accent Highlight**| Warm Gold / Amber | `#F59E0B` | Doctor star ratings, performance/achievement indicators. |
| **Soft Accent** | Light Blue / Cyan Tint | `#E8F0FE` | Hashtag badge backgrounds, icon circle backgrounds, and secondary pill buttons. |

---

## 2. Typography

Uses a modern sans-serif typeface that is professional, clean, legible, and gives a calm, trustworthy feel.

*   **Recommended Font Family:** Inter, Plus Jakarta Sans, or Public Sans.
*   **Text Hierarchy:**
    *   **Hero Heading (H1):** 36px – 44px | Bold (`700`) | Deep Royal Navy (`#0B1F4F`) with Primary Blue accents.
    *   **Section Title (H2):** 24px – 28px | Bold (`700`) / Semi-Bold (`600`).
    *   **Card Title (H3):** 16px – 18px | Semi-Bold (`600`) | Primary text color.
    *   **Body Text:** 14px – 15px | Regular (`400`) | Line-height: `1.6` | Gray (`#5A6A85`).
    *   **Caption / Badge Text:** 12px – 13px | Medium (`500`).

---

## 3. UI Components & Visual Elements (UI Components)

### A. Cards & Containers (*Cards & Containers*)
*   **Border Radius:**
    *   Standard cards (Services, News, Doctors): `16px` – `20px` (`rounded-2xl`).
    *   Hero Image / Banner Frame: `24px` (`rounded-3xl`).
    *   Pill Badges & Buttons: `9999px` (`rounded-full`).
*   **Shadows:**
    *   *Soft Elevation:* `box-shadow: 0px 8px 24px rgba(22, 82, 226, 0.06);` on doctor and facility cards.
    *   *Hover Effect:* Cards lift slightly (`translate-y-[-4px]`) with a softer shadow.
*   **Visual Shapes:** Curved shapes (*curved wave / smooth mask*) on images and section boundaries.

### B. Buttons (*Buttons*)
*   **Primary Button:** `#1652E2` background, white text, `rounded-lg` or `rounded-full`, with a small arrow icon on the right side.
*   **Secondary / Ghost Button:** White background with a thin `#1652E2` border, or a transparent background with `#1652E2` text.
*   **Badge Button (Pill):** Small size with fully rounded corners (`rounded-full`), transparent light-blue background with blue text.

### C. Iconography & Media (*Icons & Photography*)
*   **Icon Style:** Simple, consistent medical-based line-art / duotone icons in light-blue (`#E8F0FE`) circles.
*   **Photography:**
    *   High-resolution realistic photos with bright lighting (*high key lighting*).
    *   Focus on friendly smiles, clean atmospheres, professional doctors, and humane interactions between medical staff and patients.

---

## 4. Page Layout & Structure (Layout Architecture)

1.  **Top Navigation (Header):**
    *   Hospital logo on the left.
    *   Centered horizontal navigation menu.
    *   Primary *"Daftar Online"* action button at the top right.
2.  **Hero Section:**
    *   2-column format: invitation text, tagline, and *CTA* buttons on the left; main photo (Doctor & Patient) in an organic frame on the right.
    *   *Floating Stat Bar:* Statistics row (*15+ Doctors, 25,000+ Patients, 98% Satisfaction*) floating on the hero boundary.
3.  **About / Profile Section:**
    *   Hospital building/facility view beside the vision description & 24-hour service excellence.
4.  **Our Services (Service Grid):**
    *   Horizontal 6-column grid showing icons and names of key services (Specialist Clinics, Inpatient Care, ER, Radiology, Laboratory, Pharmacy).
5.  **Our Doctors (Carousel / Slider):**
    *   Doctor profile photo cards with name, specialty, star rating, and left/right arrow navigation.
6.  **Modern Facilities (Dark Section Accent):**
    *   Dark/navy background for visual contrast on its gallery.
7.  **Health News & Tips (Article Grid):**
    *   Article cards with thumbnail photos, category badges, titles, and release dates.
8.  **CTA Banner / Call Center (Footer Banner):**
    *   Solid blue banner at the bottom with a prominent emergency contact *(021) 1234 5678* for fast response.

---

## 5. Responsive Behavior

*Follow the Tailwind breakpoint scale (mobile-first): `sm` ≥640px · `md` ≥768px · `lg` ≥1024px · `xl` ≥1280px.*

| Range | Hero | Navigation | Grids & sections |
|---|---|---|---|
| `xl` (≥1280px) | 2 columns, max-w-7xl container | Full | 3-column article grid, 96px padding |
| `lg` (1024–1280px) | Tight 2 columns | Full | 3-column article grid |
| `md` (768–1024px) | Stacked (text → visual) | Hamburger + drawer | 2-column article grid, 64px padding |
| Base (<768px) | 1 column, sticky-bottom emergency CTA | Hamburger | 1 column, 48px padding |

- Hero heading 48–56px (desktop) → 32–36px (mobile); emergency number at least 20px and always fully readable.
- Dark gallery section: full-bleed at all sizes; photo grid goes 3→1 columns.
- The call-center CTA banner becomes sticky-bottom on mobile so it's always reachable; it must not cover form content.

---

## 6. Motion & Animation

| Token | Value | Used for |
|---|---|---|
| `--motion-fast` | `150ms` | Hover, focus |
| `--motion-base` | `250ms` | Drawer, dropdown, expand/collapse |
| `--motion-slow` | `400ms` | Hero entrance, scroll-reveal |
| `--ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | Default for all motion |
| `--ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | Symmetric motion |

`linear` is only for continuous motion (marquee, spinner).

- Animate only `transform` and `opacity`.
- The emergency number is ALWAYS static — no pulsing/blinking animation distracting from an emergency.
- Staged hero entrance: badge → title → sub → CTA (±80ms stagger, 400ms ease-out).
- One-time scroll-reveal per section (fade + 16px translate-y) at 15% visibility; article cards hover-lift.
- `prefers-reduced-motion`: show all content immediately; disable reveals and decorative motion.
