---
name: logo-design
description: Design modern, professional logos and brand marks as clean, scalable SVG files. Use this skill whenever the user asks for a logo, icon, brand mark, monogram, app icon, emblem, favicon, or wordmark, or wants to redesign or vary an existing logo, even if they don't say "SVG". Produces gradient-based geometric marks in the style of contemporary tech/startup branding (overlapping translucent shapes, negative space, rounded forms, letter monograms) and verifies them by rendering a preview.
metadata:
  author: doko89
  version: "1.0.0"
---

# Logo Design (SVG)

Create original logo marks as hand-authored SVG. The target aesthetic is the contemporary
"gradient geometric" style seen in modern tech/startup branding: simple bold shapes, smooth
gradients, rounded corners, overlap and transparency, and clever use of negative space.

Always reply to the user in the language they write in. Write SVG code comments and file names in English.

## Workflow

1. **Brief** (ask at most one short round of questions, only for what is missing):
   - Brand name (and initial letter(s) for monograms)
   - Industry / what the brand does
   - Mood keywords (e.g. trustworthy, playful, fast, premium)
   - Color preference, or "you choose"
   - Mark only, mark + wordmark, or app-icon container
   If the user already gave enough, skip asking and state your assumptions in one line.

2. **Concept**: Pick 3 distinct concepts (see `references/concepts.md`). Each should rest on ONE
   simple idea, e.g. "letter M built from two overlapping ribbons", "drop shape with negative-space
   arrow". Avoid generic clip-art (lightbulbs, globes, handshakes, stock swooshes).

3. **Build** each concept as its own SVG following the rules below. Read
   `references/svg-techniques.md` for gradient, overlap, mask and negative-space recipes, and
   `references/palettes.md` for color choices.

4. **Verify**: render every SVG to PNG with `scripts/render_preview.py`, then actually look at the
   PNG (use the view tool). Check it against the checklist below and fix problems before showing the user.

5. **Deliver**: save files to an `outputs/` folder in the current working directory (ask the user if they prefer a different location), present them, and in 2-4 sentences say what
   each concept means and which one you recommend. Offer refinements (color, shape, wordmark).

## Design rules

- **One idea per mark.** If it needs explaining for more than one sentence, simplify.
- **Geometry first.** Build on a 512x512 (or 1024x1024) square canvas, `viewBox="0 0 512 512"`,
  with the mark centered and about 10-15% padding. Use a consistent grid, and keep angles to
  multiples of 15 degrees where possible.
- **Rounded, friendly corners.** Use `stroke-linejoin="round"`, `stroke-linecap="round"`, or rounded
  paths. Avoid sharp, spiky details unless the brand is aggressive on purpose.
- **Gradients with purpose.** 2 stops, same hue family or neighboring hues (blue to cyan, orange to
  red, purple to pink). Light-to-dark direction should suggest depth. Max 3 colors per mark.
- **Overlap and depth.** Use overlapping shapes with `opacity` 0.6-0.9 or darker/lighter variants of
  the same hue to fake folds, ribbons, and layers.
- **Negative space.** Hide a second shape (arrow, drop, bolt, letter) in the gaps. Cut it as a hole
  using ONE compound path with `fill-rule="evenodd"` (outer shape + hole as a second subpath). This
  is the most portable method (works in browsers, Figma, Illustrator, and the preview renderer).
  Use `<mask>` only when evenodd can't do it, and give it `maskUnits="userSpaceOnUse"` with explicit
  x/y/width/height. Never paint a white shape on top (breaks on colored backgrounds).
  Note: if the outer shape has a stroke, the hole must be big enough that the stroke doesn't fill it in.
- **Must work small.** Mark should read at 32x32 px. No hairline strokes (min stroke about 6% of the mark size),
  no tiny details, no text inside the mark except a deliberate monogram.
- **Scalable and clean SVG.** Only `<path>`, basic shapes, `<linearGradient>`, `<radialGradient>`,
  `<clipPath>`, `<defs>` (and `<mask>` sparingly). No raster images, no external fonts or links, no filters
  (blur/drop-shadow) unless the user asks, since they render inconsistently.
- **Unique gradient IDs per file** (e.g. `g1`, `g2` prefixed with the concept name) so files can be
  inlined together without collisions.
- **Text:** if a wordmark is requested, convert it to simple geometric paths when feasible, otherwise
  use `<text>` with a generic fallback stack (`'Inter','Helvetica Neue',Arial,sans-serif`),
  and tell the user the font needs to be outlined before print use.
- **Accessibility/meta:** include `<title>` with the brand name and `role="img"`.

## Output files

For each concept deliver:
- `<brand>-<concept>.svg`: the full-color mark (transparent background)
- optionally `<brand>-<concept>-lockup.svg` (mark + wordmark) and `-mono.svg` (single color, for
  light/dark use) when the user wants a fuller set
- optionally an `-app-icon.svg`: mark on a rounded-square (rx about 22% of size) gradient tile

When presenting several concepts, also produce one `overview.png` contact sheet
(`scripts/render_preview.py --sheet`) on white and on dark backgrounds.

## Verification checklist (look at the rendered PNG)

- Is the silhouette recognizable at a glance and at 32px? (render with `--sizes 32,64,256`)
- Is the mark centered with even padding, and visually balanced?
- Do gradients look smooth, with enough contrast between overlapping parts?
- Does negative space truly show the background through (view the dark-background render; the hole should look dark, not white)?
- Any stray points, uneven curves, or overlaps that look accidental? Fix the path.
- Does it work on a dark background? Adjust or provide a mono/reversed version.

## Scripts

- `scripts/render_preview.py <file.svg ...> [--sizes 32,128,512] [--bg white|dark|transparent] [--sheet out.png]`
  renders SVGs to PNG for inspection, and validates that the SVG parses and has no external references.
  Requires `cairosvg` (`pip install cairosvg --break-system-packages`).
