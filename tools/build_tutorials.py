#!/usr/bin/env python3
"""Build standalone chapter pages from the chapter-tutorial Markdown outlines.

Run from any directory: python3 tools/build_tutorials.py
Uses only the Python standard library. The existing index TOC is the authority
for chapter titles, subsection numbers, and workbook page references.
"""
from html import escape
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'tutorials'


def inline(text):
    text = escape(text, quote=False)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    return re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)


def blocks(text):
    """Render this project's small Markdown subset and ::: answer blocks."""
    lines = text.strip().splitlines()
    output = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if line.startswith('::: '):
            question = line[4:]
            answer = []
            i += 1
            while i < len(lines) and lines[i].strip() != ':::':
                answer.append(lines[i])
                i += 1
            if i == len(lines):
                raise ValueError(f'Unclosed answer: {question}')
            output.append(f'<details class="answer"><summary>{inline(question)}'
                          '<span class="hint">Think first, then open the explanation</span></summary>'
                          f'<div class="solution">{blocks(chr(10).join(answer))}</div></details>')
            i += 1
            continue
        if line.startswith('### '):
            output.append(f'<h3>{inline(line[4:])}</h3>')
            i += 1
            continue
        if re.match(r'(?:- |\d+\. )', line):
            ordered = bool(re.match(r'\d+\. ', line))
            tag = 'ol' if ordered else 'ul'
            items = []
            pattern = r'^\d+\. ' if ordered else r'^- '
            while i < len(lines) and re.match(pattern, lines[i].strip()):
                items.append('<li>' + inline(re.sub(pattern, '', lines[i].strip())) + '</li>')
                i += 1
            output.append(f'<{tag}>' + ''.join(items) + f'</{tag}>')
            continue
        paragraph = []
        while i < len(lines) and lines[i].strip():
            if lines[i].startswith(('### ', '::: ', '- ')) or re.match(r'\d+\. ', lines[i]):
                break
            paragraph.append(lines[i].strip())
            i += 1
        if not paragraph:
            raise ValueError(f'Unsupported Markdown: {lines[i]}')
        output.append('<p>' + inline(' '.join(paragraph)) + '</p>')
    return '\n'.join(output)


TAGS = {
    2: ['Electron counting', 'Formal charge', 'Resonance'],
    3: ['VSEPR', 'Three-dimensional shape', 'Dipole cancellation'],
    4: ['Standing waves', 'Probability', 'Quantized energy'],
    5: ['Quantum numbers', 'Orbital nodes', 'Hydrogen-like ions'],
    6: ['Photon energy', 'Photoelectric effect', 'Spectral lines'],
    7: ['Electron configurations', 'Shielding', 'Periodic trends'],
    8: ['Bonding and antibonding', 'MO filling', 'Magnetism'],
    9: ['Orbital overlap', 'Hybridization', 'σ and π bonds'],
    10: ['Delocalization', 'HOMO–LUMO gap', 'Absorbed and observed colour'],
    11: ['Intermolecular forces', 'Solids', 'Polymer structure'],
    12: ['Evidence and exposure', 'Drug discovery', 'Life-cycle thinking'],
}


def figure(chapter):
    diagrams = {
        3: ('''<path class="blue" d="M90 100H290"/><text class="ink" x="65" y="106">O</text><text class="ink" x="184" y="88">C</text><text class="ink" x="300" y="106">O</text>
<path class="mint" d="M174 120H110m7 -5-7 5 7 5m89 -10h64m-7 -5 7 5-7 5"/><text class="ink" x="110" y="177">CO₂ · dipoles cancel</text>
<path class="blue" d="M490 135 550 85 610 135"/><text class="ink" x="473" y="150">H</text><text class="ink" x="542" y="75">O</text><text class="ink" x="616" y="150">H</text>
<path class="mint" d="M550 135V97m-5 7 5-7 5 7"/><text class="ink" x="454" y="177">H₂O · net dipole toward O</text>''', 'Bond polarity needs geometry', 'Equal opposite dipoles cancel in linear CO₂. In bent H₂O they produce a net dipole. Drawings are schematic.'),
        4: ('''<path class="axis" d="M75 60V200M655 60V200M75 140H655"/><path class="mint" d="M75 140Q220 -5 365 140T655 140"/><text class="ink" x="76" y="35">n = 2 · two half-wavelengths</text><text class="muted" x="65" y="224">0</text><text class="muted" x="349" y="224">L/2</text><text class="muted" x="650" y="224">L</text><circle cx="365" cy="140" r="5" fill="#f0cf8a"/><text class="ink" x="390" y="116">internal node</text><text class="muted" x="500" y="70">ψ(x)</text>''', 'A standing-wave state', 'The n = 2 box wavefunction changes sign across its central node. Squaring it gives nonnegative probability density. Schematic, not to scale.'),
        8: ('''<text class="muted" x="40" y="35">Energy increases ↑</text><path class="axis" d="M155 90 300 65M155 90 300 190M575 90 430 65M575 90 430 190"/><path class="blue" d="M80 90H155M575 90H650"/><path class="mint" d="M300 65H430M300 190H430"/><text class="ink" x="72" y="120">H 1s</text><text class="ink" x="580" y="120">H 1s</text><text class="ink" x="445" y="70">σ*1s · empty</text><text class="ink" x="445" y="195">σ1s · 2 electrons</text><text class="ink" x="345" y="180">↑↓</text>''', 'Hydrogen molecular orbitals', 'Two atomic orbitals form two MOs. H₂ occupies the bonding σ1s level and leaves σ*1s empty. This schematic is not an energy-scale calculation.'),
        10: ('''<text class="ink" x="85" y="35">Larger gap</text><text class="ink" x="450" y="35">Smaller gap</text><path class="blue" d="M80 60H260M80 195H260M445 110H625M445 195H625"/><path class="mint" d="M170 185V70m-6 9 6-9 6 9M535 185V120m-6 9 6-9 6 9"/><text class="muted" x="85" y="225">Shorter absorbed λ</text><text class="muted" x="445" y="225">Longer absorbed λ</text><text class="ink" x="280" y="140">E = hc/λ</text>''', 'Energy gaps set absorption wavelengths', 'Within a comparable molecular family, longer conjugation often reduces the frontier-orbital gap. A smaller gap absorbs a longer wavelength; perceived colour requires considering the remaining light.'),
    }
    if chapter not in diagrams:
        return ''
    drawing, title, caption = diagrams[chapter]
    return f'<figure class="diagram"><svg viewBox="0 0 730 245" role="img" aria-labelledby="diagram-title diagram-desc"><title id="diagram-title">{escape(title)}</title><desc id="diagram-desc">{escape(caption)}</desc>{drawing}</svg><figcaption>{escape(caption)}</figcaption></figure>'


def get_toc():
    index = (ROOT / 'index.html').read_text()
    match = re.search(r'const tocText = `(.+?)`;', index, re.S)
    if not match:
        raise ValueError('Could not find the index table of contents')
    entries = {}
    for number, title, page in re.findall(r'^\s*\* ([\d.]+) (.+?) \(page ([\d.]+)\)', match[1], re.M):
        entries[number] = (title, page)
    return entries


def render(chapter, entries):
    md = (SOURCE / f'chapter-{chapter:02}.md').read_text()
    title, chapter_page = entries[str(chapter)]
    lede = re.search(r'^> (.+)', md, re.M).group(1)
    headings = list(re.finditer(r'^## (.+)$', md, re.M))
    sections, links, numbers = [], [], []
    for i, heading in enumerate(headings):
        raw = heading[1]
        body = md[heading.end():headings[i + 1].start() if i + 1 < len(headings) else len(md)]
        if raw == 'Practice':
            sid, label, number, page = 'practice', 'Practice questions', '↗', None
        else:
            number = raw.split(' ', 1)[0]
            if number not in entries or int(number.split('.')[0]) != chapter:
                raise ValueError(f'Unknown section {number}')
            numbers.append(number)
            label, page = entries[number]
            sid = 'sec-' + number.replace('.', '-')
        sub = number.count('.') > 1
        level = ' subsection' if sub else ''
        page_html = f'<p class="page-ref">Workbook reference · page {escape(page)}</p>' if page else ''
        sections.append(f'<details class="lesson{level}" id="{sid}" open><summary><h2><span class="number">{number}</span> {escape(label)}</h2></summary><div class="lesson-body">{page_html}{blocks(body)}</div></details>')
        links.append(f'<li class="{"sub" if sub else "main-section"}"><a data-section-link href="#{sid}">{number if page else ""} {escape(label)}</a></li>')
    expected = {key for key in entries if key.startswith(f'{chapter}.')}
    if set(numbers) != expected or len(numbers) != len(expected):
        raise ValueError(f'Chapter {chapter} coverage mismatch: {expected.symmetric_difference(numbers)}')
    toc_html = '<ol>' + ''.join(links) + '</ol>'
    previous = (f'<a rel="prev" href="chapter-{chapter-1:02}.html">← Chapter {chapter-1}<br>{escape(entries[str(chapter-1)][0])}</a>'
                if chapter > 2 else '<a href="index.html#chapter-1">← Table of contents<br>Chapter 1: Why Study Chemistry?</a>')
    following = (f'<a rel="next" href="chapter-{chapter+1:02}.html">Chapter {chapter+1} →<br>{escape(entries[str(chapter+1)][0])}</a>'
                 if chapter < 12 else '<a href="index.html">Table of contents →<br>Choose another chapter</a>')
    extras = ''
    if chapter == 12:
        extras = '<li><a href="https://www.fda.gov/patients/learn-about-drug-and-device-approvals/drug-development-process">FDA: the drug development process</a> — supplementary overview for 12.3.1.</li><li><a href="https://www.epa.gov/greenchemistry/basics-green-chemistry">US EPA: basics and principles of green chemistry</a> — supplementary reference for 12.4.2.</li>'
    css = (SOURCE / 'tutorial.css').read_text()
    js = (SOURCE / 'tutorial.js').read_text()
    badges = ''.join(f'<span class="badge">{escape(tag)}</span>' for tag in TAGS[chapter])
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="icon" href="data:,">
<meta name="description" content="Chapter {chapter}: {escape(title, quote=True)}. Explanations, worked examples, and practice aligned to the UBC 2024–2025 ChIRP table of contents.">
<title>Chapter {chapter} — {escape(title)} | Chemistry 111, 121 &amp; 141</title>
<style>{css}</style></head><body>
<a class="skip" href="#main">Skip to tutorial</a>
<header class="top"><a href="index.html">Chemistry 111, 121 &amp; 141 / Study tutorials</a><span class="edition">UBC · Integrated Resource Package · 2024–2025</span></header>
<div class="layout"><aside class="sidebar"><nav aria-label="Chapter sections"><h2>In this chapter</h2>{toc_html}<a class="chapter-home" href="index.html#chapter-{chapter}">← All chapters</a></nav></aside>
<main class="main" id="main"><details class="mobile-toc"><summary>Browse chapter sections</summary><nav aria-label="Chapter sections on mobile">{toc_html}</nav></details>
<header id="chapter-{chapter}"><div class="eyebrow">Chapter {chapter} · Study tutorial</div><h1>{escape(title)}</h1><p class="lede">{escape(lede)}</p><div class="badges">{badges}</div></header>
<p class="scope">Original study notes aligned to the chapter and section headings in the 2024–2025 resource package table of contents. Page labels refer to the workbook. Use your workbook and course materials for the assigned learning objectives, research features, and exercises.</p>
{figure(chapter)}
<div class="toolbar" role="group" aria-label="Study controls" hidden><div class="search-wrap"><label for="search">Search this chapter</label><input type="search" id="search" placeholder="Try a concept, formula, or section number" autocomplete="off" aria-controls="lessons"></div><button id="expand" type="button">Expand all</button><button id="collapse" type="button">Collapse all</button><button id="print" type="button">Print / PDF</button></div>
<p class="status" id="search-status" role="status" aria-live="polite" hidden></p>
<div id="lessons">{''.join(sections)}</div><p class="no-results" id="no-results" hidden>No sections match. Try a shorter search or clear the search field.</p>
<section class="sources" aria-labelledby="sources-heading"><h2 id="sources-heading">Course context and further reading</h2><ul><li><a href="index.html#chapter-{chapter}">Local resource-package table of contents</a> — chapter order, section numbering, and workbook page references.</li>{extras}</ul></section>
<nav class="chapter-nav" aria-label="Previous and next chapters">{previous}{following}</nav>
<footer class="footer">Chemistry study companion · Chapter {chapter} · <a href="index.html">Return to the table of contents</a></footer></main></div>
<div id="copy-status" role="status" aria-live="polite" hidden></div><script>{js}</script></body></html>
'''


def main():
    entries = get_toc()
    for chapter in range(2, 13):
        output = ROOT / f'chapter-{chapter:02}.html'
        output.write_text(render(chapter, entries))
        print(f'Built {output.name}')


if __name__ == '__main__':
    main()
