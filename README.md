# design-skills

[![skills.sh](https://skills.sh/b/doko89/design-skills)](https://skills.sh/doko89/design-skills)

A collection of agent skills for UI design and brand identity work. Install them
into your AI coding agent with a single command.

## Skills

| Skill | What it does |
|---|---|
| [design-skill](skills/design-skill/) | Applies 23 UI style guides (dashboards, landing pages, login screens, mobile apps) plus a shared hero-animation reference, with Tailwind breakpoints and motion tokens. |
| [logo-design](skills/logo-design/) | Designs modern, professional logos and brand marks as clean, scalable SVG files, and verifies them by rendering previews. |

## Install

Install all skills in this collection:

```bash
npx skills add doko89/design-skills -g -y
```

Or install a single skill:

```bash
npx skills add doko89/design-skills -s design-skill -g -y
npx skills add doko89/design-skills -s logo-design -g -y
```

Browse and discover more skills at [skills.sh](https://skills.sh/doko89/design-skills).

## Requirements

- `logo-design` uses `scripts/render_preview.py` to render SVG previews, which
  requires Python and `cairosvg` (`pip install cairosvg`).
- `design-skill` has no dependencies beyond the reference files in this repo.

## Repository structure

```
skills/
├── design-skill/      # SKILL.md + references/
└── logo-design/       # SKILL.md + references/ + scripts/
```

## License

No license file yet — all rights reserved unless a license is added later.
