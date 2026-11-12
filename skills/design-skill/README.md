# design-skill

Applies a local UI design system for dashboards, landing pages, login screens,
and mobile apps. The agent reads the matching reference file before writing or
changing UI code, then follows its design tokens, responsive rules, and motion
tokens as-is.

## Contents

- 8 dashboard styles (`references/dashboard/`)
- 6 landing page styles + 1 shared hero-animation reference (`references/landing/`)
- 4 login styles (`references/login/`)
- 5 mobile app styles (`references/mobile/`)

## Install

```bash
npx skills add doko89/design-skills -s design-skill -g -y
```

See [SKILL.md](SKILL.md) for the full usage guide.
