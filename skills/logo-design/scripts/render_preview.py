#!/usr/bin/env python3
"""Render SVG logos to PNG for visual inspection and run basic sanity checks.

Usage:
  render_preview.py a.svg b.svg [--sizes 32,128,512] [--bg white|dark|transparent]
                    [--outdir DIR] [--sheet sheet.png]

For each SVG, writes <name>_<size>.png into outdir (default: next to the SVG, in ./previews).
--sheet builds a contact sheet with every logo on white and on dark backgrounds.
"""
import argparse, io, os, re, sys
import xml.etree.ElementTree as ET

try:
    import cairosvg
except ImportError:
    sys.exit("cairosvg missing: pip install cairosvg --break-system-packages")

BG = {"white": "#FFFFFF", "dark": "#0B1020", "transparent": None}


def validate(path):
    problems = []
    text = open(path, encoding="utf-8").read()
    try:
        root = ET.fromstring(text)
    except ET.ParseError as e:
        return [f"XML parse error: {e}"]
    if "viewBox" not in root.attrib:
        problems.append("missing viewBox")
    if re.search(r"<image\b", text):
        problems.append("contains <image> (raster/external); logos should be pure vector")
    if re.search(r"(href|src)=[\"']https?://", text):
        problems.append("external reference found")
    if re.search(r"<filter\b", text):
        problems.append("uses <filter>; may render inconsistently")
    if re.search(r"<mask\b", text):
        problems.append("uses <mask>; confirm on the dark render that holes are transparent "
                        "(prefer fill-rule=evenodd compound paths)")
    ids = re.findall(r'\bid="([^"]+)"', text)
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        problems.append(f"duplicate ids: {sorted(dup)}")
    for ref in set(re.findall(r"url\(#([^)]+)\)", text)):
        if ref not in ids:
            problems.append(f"url(#{ref}) has no matching id")
    return problems


def render(path, size, bg, out):
    cairosvg.svg2png(url=path, write_to=out, output_width=size, output_height=size,
                     background_color=BG[bg])


def sheet(paths, out, cell=320):
    from PIL import Image
    n = len(paths)
    W, H = cell * n, cell * 2
    img = Image.new("RGB", (W, H), "white")
    for i, p in enumerate(paths):
        for row, bg in enumerate(("white", "dark")):
            buf = io.BytesIO()
            cairosvg.svg2png(url=p, write_to=buf, output_width=cell - 60,
                             output_height=cell - 60, background_color=BG[bg])
            tile = Image.open(buf).convert("RGB")
            cellimg = Image.new("RGB", (cell, cell), BG[bg])
            cellimg.paste(tile, (30, 30))
            img.paste(cellimg, (i * cell, row * cell))
    img.save(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("svgs", nargs="+")
    ap.add_argument("--sizes", default="512")
    ap.add_argument("--bg", default="white", choices=BG)
    ap.add_argument("--outdir")
    ap.add_argument("--sheet")
    a = ap.parse_args()

    ok = True
    for p in a.svgs:
        probs = validate(p)
        status = "OK" if not probs else "ISSUES"
        print(f"[{status}] {p}")
        for pr in probs:
            print(f"   - {pr}")
        if probs and any(x.startswith("XML") for x in probs):
            ok = False
            continue
        outdir = a.outdir or os.path.join(os.path.dirname(os.path.abspath(p)), "previews")
        os.makedirs(outdir, exist_ok=True)
        stem = os.path.splitext(os.path.basename(p))[0]
        for s in [int(x) for x in a.sizes.split(",")]:
            out = os.path.join(outdir, f"{stem}_{s}.png")
            render(p, s, a.bg, out)
            print(f"   -> {out}")
    if a.sheet:
        sheet(a.svgs, a.sheet)
        print(f"contact sheet -> {a.sheet}")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
