# Style Design Guidelines: TwitHR Dashboard

This document defines the design system (*Design System*) and visual style guidelines based on the *TwitHR* HR management dashboard interface.

---

## 1. Color Palette

The palette carries a modern SaaS style dominated by bluish purple (*indigo/violet*) as the primary identity, paired with a bright background and clean component cards.

| Category | Color | Estimated HEX Code | Primary Usage |
| :--- | :--- | :--- | :--- |
| **Primary / Brand** | Purple / Indigo | `#6366F1` / `#5B4FCF` | Navigation sidebar, primary button (*CTA*), welcome banner, active icons, highlight elements. |
| **Background** | Bright Blue / Ice Blue | `#F0F4FF` | Overall page background (*canvas background*). |
| **Surface / Card** | Clean White | `#FFFFFF` | Background for cards (*cards*), tables, calendar panels, and profile widgets. |
| **Neutral Dark** | Charcoal Black | `#1E293B` | Primary text, titles (*headings*), usernames, and table labels. |
| **Neutral Gray** | Medium Gray | `#64748B` | Sub-text, descriptions, inactive icons, date/meta text. |
| **Border / Divider**| Thin Line Gray | `#E2E8F0` | Divider lines between table rows and component separators. |

---

## 2. Typography

Uses a clean, geometric modern sans-serif *font family* optimized for dashboard data readability.

*   **Font Family:** `Inter`, `Poppins`, sans-serif
*   **Text Hierarchy:**
    *   **Dashboard Title (H1):**
        *   Size: ~22px - 24px (Bold / Semibold)
        *   Color: Neutral Dark (`#1E293B`)
    *   **Card Header / Banner Text:**
        *   Size: ~16px - 18px (Bold), white inside the purple banner.
    *   **Body & Table Text:**
        *   Size: ~13px - 14px (Regular / Medium)
        *   Color: Neutral Dark / Neutral Gray for secondary text.
    *   **Small / Meta Text:**
        *   Size: ~11px - 12px (Regular) for date labels, statuses, and designations.

---

## 3. Layout & Structure

The design uses a **Multi-Column Dashboard with Sidebar** structure:
*   **Left Sidebar (Fixed Width):** Holds the brand logo (*TwitHR*), primary navigation menu (Dashboard, Recruitment, Onboarding, Reports, Calendar, Settings), and a premium feature promo box at the bottom.
*   **Primary Content Area (Right):**
    *   **Top Header:** Holds the page title ("Dashboard"), search/notification icons, and the user profile (*Mr. Smith*).
    *   **Primary Grid (Center-Right):** Uses an asymmetric layout where the left column holds the *Welcome Banner* and *Recruitment Progress* table, while the right column holds the calendar widget (*October 2020*) and the HR Manager profile card.
*   **Container & Card Border Radius:** Consistent smooth corners (`border-radius: 12px` to `16px`) for an organic, user-friendly feel.

---

## 4. UI Components

### A. Sidebar & Navigation
*   **Menu Item:** Has an icon to the left of the menu text. The active menu is marked with a white/bright background and purple text, while other menus are white on a dark purple background.
*   **Upgrade Card:** Small box at the bottom of the sidebar with a bright white background, a mini illustration, and a premium feature button.

### B. Banner & Buttons
*   **Hero Banner ("Hello Mr Smith!"):** Purple gradient background with a supporting vector illustration on the right, informative text, and a bright orange rounded *Read More* button.
*   **Primary Action Button ("View All"):** Small pill-shaped (*pill-shaped*) purple button with white text to expand the table list.

### C. Data Tables (Recruitment Table)
*   **Column Structure:** *Full Name* (with round profile photo), *Designation* (job position badge with a colorful pastel background), *Status* (interview stage with a color dot indicator), and an action button (*ellipsis* `...`).
*   **Designation Badges:** Small text labels with soft pastel backgrounds (pink, yellow, light blue, light green).

### D. Calendar & Widgets (Right Side)
*   **Mini Calendar:** Full monthly calendar with the selected date circled in blue/purple, plus month navigation buttons at the top.
*   **Profile Card ("Mr Smith"):** Framed profile photo, job title (*Sr. HR Manager*), quick action buttons (message, email, file), and a company info summary (*Joining Date*, *Projects Active*).

---

## 5. Responsive Behavior

*Follow the Tailwind breakpoint scale (mobile-first): `sm` ≥640px · `md` ≥768px · `lg` ≥1024px · `xl` ≥1280px.*

| Range | Sidebar & navigation | Card grid | Tables & widgets |
|---|---|---|---|
| `xl` (≥1280px) | Full sidebar | Content + right column (calendar, profile) | Full recruitment table |
| `lg` (1024–1280px) | 200–220px sidebar | Narrower right column | Full table, 20px card padding |
| `md` (768–1024px) | Drawer (hamburger) or 72px icon rail | 1 column, widgets below content | Table scroll-x + sticky name column |
| Base (<768px) | Drawer / bottom-nav | Stack: content → calendar → profile | Table becomes one card per candidate |

- Never hide primary actions (add candidate, profile quick actions) on small screens.
- Mobile candidate cards hold: photo, name, position badge, interview status, action button — with no clipped columns.
- Pastel designation badges stay readable (minimum 12px) and wrap neatly in narrow cards.
- Banner + buttons: full-width buttons below `md`; minimum 44px touch targets.

---

## 6. Motion & Animation

| Token | Value | Used for |
|---|---|---|
| `--motion-fast` | `150ms` | Hover, focus, tooltips |
| `--motion-base` | `250ms` | Drawer, dropdown, expand/collapse |
| `--motion-slow` | `400ms` | Card entrance, widget animation |
| `--ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | Default for all motion |
| `--ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | Symmetric motion (toggles, progress) |

`linear` is only for continuous motion (spinners, skeleton shimmer).

- Animate only `transform` and `opacity` for 60fps.
- Card/button hover: lift 2–4px + soft shadow (150ms); press: `scale(0.98)`.
- Entrance: fade + `translate-y(8–12px)`, 40–60ms stagger between candidate cards.
- Selected calendar date: 150ms circle color transition; status badges fade in as data loads.
- Drawer: 250ms ease-out slide + overlay fade.
- Loading: skeleton shimmer (1200ms loop); spinners only inside action buttons.
- `prefers-reduced-motion`: disable entrance and shimmer; show the final state immediately.
