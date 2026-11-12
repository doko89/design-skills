# Hero Animation Reference — Landing Pages (Shared)

A shared reference for all six landing styles (LANDING_1 through LANDING_6). Read it as a second file — after one style file — only when the request mentions animation, interactivity, premium, or cinematic feel.

---

## 1. Usage Rules (mandatory)

- Maximum 2–3 primary effects per hero. More than that splits the visual focus and buries the CTA.
- The CTA stays the most prominent element. Animation must not cover or shift the CTA after the entrance finishes.
- The headline must read within 5 seconds. Never lock the core message behind slow animation.
- Animate only `transform` and `opacity`.
- Standard entrance: badge → title → sub → CTA (±80ms stagger, 400ms ease-out).
- One-time scroll-reveal per section (fade + 16px translate-y) at 15% visibility. Don't repeat on scroll up/down.
- Performance budget: hero image <200KB, total JS <200KB, LCP <2.5s. Lazy-load everything below the fold.
- `prefers-reduced-motion`: show all content immediately. Disable reveals and decorative motion.

---

## 2. Eight Hero Combinations

### 1. Parallax + Floating Elements — modern & immersive

- Background moves with parallax on scroll.
- Decorative objects float slowly at different speeds.
- Best for: agencies, portfolios, creative studios.
- Low risk. Make sure floating elements don't collide with text on small screens.

### 2. Parallax + Staggered Text Reveal — clean & premium

- Subtle background parallax.
- Heading appears word by word, then subtitle and CTA in sequence.
- Best for: corporate, SaaS, personal branding.
- Low risk. The safe pick when conversion is the priority.

### 3. 3D Tilt + Mouse Tracking + Spotlight — interactive

- Objects tilt following the cursor position.
- Background spotlight follows mouse movement.
- Best for: tech, product showcases, gaming.
- Heavy. Disable on touch devices and under `prefers-reduced-motion`. Provide a static pose as the default.

### 4. Gradient Mesh + Blur Morphing + Text Reveal — organic

- Gradient drifts slowly, blobs morph shape.
- Heading appears with a clip-path reveal.
- Best for: startups, creative agencies, digital studios.
- Medium. Limit blur so text stays sharp and LCP stays healthy.

### 5. Cinematic Video + Ken Burns + Fade — luxurious

- Background video as the main visual with a slow zoom.
- Dark overlay, fading text, CTA appears after the headline.
- Best for: luxury brands, hotels, travel, architecture, automotive.
- Heaviest. A poster image fallback is mandatory, mute + autoplay, and disable video on slow mobile.

### 6. Scroll-Driven + Mask Reveal — editorial

- Images open from small to fullscreen following the scroll.
- Text shifts position, foreground and background layers move at different speeds.
- Best for: storytelling, portfolios, editorial sites.
- Medium. Lock the primary CTA so it doesn't slide out of view.

### 7. Particle + Mouse Interaction + Glow — futuristic

- Particles drift randomly and react to the cursor.
- Connection lines and glow give a tech feel.
- Best for: AI, technology, cybersecurity.
- Heavy. Cap the particle count; disable on mobile and under `prefers-reduced-motion`.

### 8. Infinite Marquee + Parallax + Scroll Reveal — showcase

- Text or logos run endlessly.
- Parallax images, cards appear staggered on scroll.
- Best for: creative agencies, showcases, branding.
- Light–medium. Marquees use `linear` easing and pause on hover when they contain links.

---

## 3. Visual Character Mapping

| Website character | Recommended combination |
|---|---|
| Premium / Luxury | 5 Cinematic + Ken Burns + Fade |
| Futuristic | 3 3D Tilt + Spotlight + 7 Particle |
| Minimalist | 2 Parallax + Text Reveal + Fade |
| Creative Agency | 1 Parallax + Floating + 6 Mask Reveal |
| Modern SaaS | 4 Gradient Mesh + Stagger Reveal |
| Interactive Portfolio | 6 Scroll-Driven + 3 3D Tilt |
| Bold / Experimental | 8 Marquee + Distortion + Parallax |

---

## 4. Top Three Picks

**Best overall:** 1 + 2 — Parallax + Floating + Staggered Reveal. Alive and dimensional, readability intact.

**Best premium:** 5 + 6 — Cinematic + Slow Zoom + Mask Reveal. Expensive, cinematic feel.

**Best interactive:** 3 + 6 — 3D Tilt + Cursor Tracking + Scroll-Driven. Most memorable, needs a mobile fallback.

---

## 5. Technology

| Effect | Technology |
|---|---|
| Parallax | GSAP ScrollTrigger |
| Staggered Reveal | GSAP / Framer Motion |
| 3D Tilt | Vanilla JS / React |
| 3D Object | Three.js / React Three Fiber |
| Gradient Morphing | CSS / GSAP |
| Particle System | Three.js / tsParticles |
| Scroll-driven | GSAP ScrollTrigger |
| Smooth Scrolling | Lenis |
| Text Animation | GSAP SplitText |

---

## 6. Responsive Behavior & Fallbacks

*Follow the Tailwind breakpoint scale (mobile-first): `sm` ≥640px · `md` ≥768px · `lg` ≥1024px · `xl` ≥1280px.*

- Base (<768px): disable mouse tracking, 3D tilt, and particles. Replace video with a poster image.
- `md` (768–1024px): reduce parallax, slow floating, keep the marquee running.
- `lg` and up: all combinations allowed at full strength, as long as the performance budget holds.
- Touch devices without hover: all cursor-based effects permanently off.
- A sticky mobile CTA is worth more than decorative motion. Prioritize the CTA.

---

## 7. Motion Tokens

| Token | Value | Used for |
|---|---|---|
| `--motion-fast` | `150ms` | Hover, focus |
| `--motion-base` | `250ms` | Drawer, dropdown, expand/collapse |
| `--motion-slow` | `400ms` | Hero entrance, scroll-reveal |
| `--ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | Default for all motion |
| `--ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | Symmetric motion |

`linear` is only for continuous motion (marquee, spinner).

---

## 8. Mapping to Landing Styles

| Style | Matching combinations | Why |
|---|---|---|
| LANDING_1 AMZ Marketer (purple AI) | 4 Gradient Mesh + Reveal | AI and startup feel |
| LANDING_2 Freedom Funnels (lifestyle photos) | 1 Parallax + Floating | Floating photos are already its signature |
| LANDING_3 DigitalHub (product grid) | 8 Marquee + Scroll Reveal | Product and logo showcase |
| LANDING_4 ClassiAds (ads + 3D accents) | 2 Stagger Reveal + 3 light Tilt | 3D accents on cards, text stays fast |
| LANDING_5 Travel Agency | 5 Cinematic + Ken Burns | Destinations need a cinematic feel |
| LANDING_6 Healthcare (dark gallery) | 2 Parallax + Text Reveal | Calm and trustworthy, frugal animation |
