---
name: design-skill
description: Apply 23 local UI style guides (dashboard, landing page, login, mobile app) plus 1 shared hero animation reference, complete with Tailwind breakpoints and motion tokens whenever building, restyling, or reviewing an interface.
metadata:
  author: doko89
  version: "1.0.0"
---

# Design Skill

A guide to applying the local design system for dashboards, landing pages, login screens, and mobile apps. Always read the matching reference file before writing or changing UI code.

## When to use

Use this skill whenever the user asks to: create a new UI page or screen (dashboard, landing, login/signup, mobile screen), restyle an existing view, match a style to one of the references, add responsive behavior or animation, or review visual consistency. If the request names one of the styles below (e.g. "FinanceFlow" or "ClassiAds"), use that file directly.

## Choosing a reference file

All paths are relative to this skill's directory. Read ONLY the file that matches the request — don't load them all.

### Dashboard (`references/dashboard/`)

| File | Style | Highlights |
|---|---|---|
| STYLE_GUIDE_1.md | Cobalt Analytics | Clean blue analytics, sidebar + header, line/donut/bar charts |
| STYLE_GUIDE_2.md | Profit vs Expense | Striped-vs-solid bar chart, multicolor proportional donut |
| STYLE_GUIDE_3.md | SalesHub | Metric cards, data table, pie + stacked bar |
| STYLE_GUIDE_4.md | Statistics & Geography | Stat cards, geography indicators, circular progress |
| STYLE_GUIDE_5.md | Suburban | Activity feed, overview widget, summary cards |
| STYLE_GUIDE_6.md | Super Finti | Pastel gradient cards, glassmorphism, help-center banner |
| STYLE_GUIDE_7.md | FinanceFlow | Minimalist sidebar, search pill, donut, transaction table |
| STYLE_GUIDE_8.md | TwitHR | Recruitment table, mini calendar, profile card |

### Landing page (`references/landing/`)

| File | Style | Highlights |
|---|---|---|
| LANDING_1.md | AMZ Marketer | Purple AI, 2-column hero, stat cards |
| LANDING_2.md | Freedom Funnels 3.0 | Floating lifestyle photos, module cards |
| LANDING_3.md | DigitalHub | Product grid, payment badges, newsletter |
| LANDING_4.md | ClassiAds | Search + 4-column ad grid, 3D accents |
| LANDING_5.md | Travel Agency | Search widget, package grid, pricing table |
| LANDING_6.md | Healthcare | Dark gallery, article grid, emergency banner |

Shared landing reference (not a style): HERO_ANIMATIONS.md — 8 hero animation combinations across styles. Read it as a second file after one LANDING_X file, only when the request mentions animation, interactivity, premium, or cinematic feel.

### Login (`references/login/`)

| File | Style | Highlights |
|---|---|---|
| login_1.md | Night Sky | Purple split card, night-sky illustration, underline inputs |
| login_2.md | Sign Up | Modal, social buttons, Tailwind code sample |
| login_3.md | SaaS Split | Dashboard preview + partner logos |
| login_4.md | Adminator | Glassmorphism testimonial, loose form |

### Mobile (`references/mobile/`)

| File | Style | Highlights |
|---|---|---|
| MOBILE_1.md | Smart Home | Active/inactive device cards, toggles, gauges |
| MOBILE_2.md | FinTech | Balance hero, quick actions, transaction list |
| MOBILE_3.md | Crypto Wallet | Area chart, watchlist, order book |
| MOBILE_4.md | Expense Tracker | Budget bars, donut, bottom-nav + FAB |
| MOBILE_5.md | Personal Finance | Segmented toggle, category grid, numpad |

## How to apply

1. Read the chosen reference file thoroughly: colors, typography, components, spacing, then the responsive and motion sections. For landing pages requesting animation, also read HERO_ANIMATIONS.md as a second file.
2. Follow its design tokens as-is: color HEX values, type scale, radius, elevation, and spacing. Don't invent new values unless the user asks.
3. Apply its responsive rules: mobile-first Tailwind scale (`sm` 640, `md` 768, `lg` 1024, `xl` 1280), per-breakpoint layout adaptation, minimum 44px touch targets.
4. Apply its motion tokens: 150/250/400ms durations, ease-out as the default easing, animate only `transform` and `opacity`, respect `prefers-reduced-motion`.
5. If the request doesn't name a specific style, pick the closest match, say which one you picked, and stay consistent with it throughout the result.

## Notes

- All files are in English.
- HEX values in the files are visual estimates from the reference images; treat them as starting tokens.
- Don't add unrequested features, sections, or decorations just to "complete" the look.
