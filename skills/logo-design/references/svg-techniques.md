# SVG techniques for logos

All examples use `viewBox="0 0 512 512"`.

## Boilerplate
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" role="img">
  <title>Brand name</title>
  <defs>
    <linearGradient id="brand-g1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#3B82F6"/>
      <stop offset="1" stop-color="#06B6D4"/>
    </linearGradient>
  </defs>
  <!-- shapes -->
</svg>
```

## Rounded shapes
- Rounded rect: `<rect x="96" y="96" width="320" height="320" rx="72"/>`
- Thick ribbon with round ends: `<path d="M120 380 L256 140" stroke="url(#g)" stroke-width="64" stroke-linecap="round" fill="none"/>`
- Rounded polygon: draw with `stroke-linejoin="round"` and a stroke of the same color as the fill, which rounds the corners for free.

## Overlapping layers (depth)
```svg
<rect x="150" y="130" width="240" height="180" rx="40" fill="url(#g-light)"/>
<rect x="120" y="190" width="240" height="180" rx="40" fill="url(#g-dark)" opacity=".85"/>
```
Use a darker tint where shapes overlap by drawing the intersection as its own path with a deeper gradient. This is more reliable than `mix-blend-mode`.

## Negative space: use evenodd compound path (preferred)
Put the hole as a second subpath in the same `<path>`. Tested to render correctly everywhere.
```svg
<path fill-rule="evenodd" fill="url(#g1)"
  d="M150 380 C98 380 64 342 64 296 ... Z      <!-- outer cloud -->
     M256 190 L316 252 H280 V330 H232 V252 H196 Z"/>  <!-- arrow hole -->
```
If you add a `stroke` to round corners, keep the hole larger than the stroke width, otherwise the stroke fills it.

## Negative space with mask (fallback only)
Masks are less portable: some renderers ignore them or clip to the wrong region. If you must:
```svg
<mask id="cut" maskUnits="userSpaceOnUse" x="0" y="0" width="512" height="512">
  <rect width="512" height="512" fill="#fff"/>
  <path d="..." fill="#000"/>   <!-- black = removed -->
</mask>
<path d="M..." fill="url(#g1)" mask="url(#cut)"/>
```
Always render on the dark background to confirm the hole is really transparent.

## Ribbon crossing (over/under)
1. Draw the full loop as a stroked path.
2. Redraw only the short overlapping segment on top using the same gradient (or a slightly darker one) and add a thin gap by first drawing that segment slightly thicker in the background color via a mask rather than white.

## Rotational symmetry
```svg
<g id="petal"><path d="M256 256 C 216 180 216 110 256 80 C 296 110 296 180 256 256Z" fill="url(#g1)"/></g>
<use href="#petal" transform="rotate(72 256 256)"/>
<use href="#petal" transform="rotate(144 256 256)"/>
<!-- ... -->
```
For maximum compatibility, repeat the `<path>` instead of `<use>` if the file will be imported into design tools.

## Isometric cube
Top face: `M256 96 L400 176 L256 256 L112 176Z` lightest; left: `M112 176 L256 256 L256 416 L112 336Z` mid; right: `M400 176 L256 256 L256 416 L400 336Z` darkest.

## Ring passing in front/behind (orbit)
Draw the ring, then a `clipPath` that hides half of it behind the center shape, then draw the other half over the shape.

## Stripe cuts (speed lines)
Draw the main shape, then add 2-3 parallel diagonal bands with lighter/darker gradients from the shape's left edge, clipped to the shape via `clip-path`.

## App icon tile
```svg
<rect width="512" height="512" rx="112" fill="url(#tile)"/>
<g transform="translate(96 96) scale(.625)"> <!-- mark scaled to 320px -->
```
Use white or a light-tinted version of the mark on a saturated gradient tile.

## Wordmark lockup
Canvas 1200x400: mark at x=60 (height 280), text starting x=400, baseline vertically centered. Weight 600-700, tight letter-spacing (-1% to -2%).

## Common pitfalls
- Duplicate gradient IDs across inlined SVGs, so prefix them.
- White "fake" cut-outs: use evenodd holes instead.
- `<mask>` without `maskUnits="userSpaceOnUse"` and explicit region can clip the whole shape.
- `gradientUnits` default is objectBoundingBox: for strokes on straight horizontal/vertical lines the bbox has zero height or width and the gradient will not render. Use `gradientUnits="userSpaceOnUse"` with explicit coordinates in that case.
- Forgetting `fill="none"` on stroked paths.
- Using `filter` effects, which render inconsistently.
