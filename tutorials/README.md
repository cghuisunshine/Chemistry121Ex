# Chapter tutorials

These original study outlines follow the chapter numbers, section headings,
and workbook page references already recorded in `index.html` for the UBC
*Chemistry 111, 121 and 141 Integrated Resource Package, 2024–2025*.
They were written from that outline; the full workbook was not available in
this project. They are study companions rather than reproductions of its
assigned learning objectives, research features, or exercise solutions.

Each `chapter-NN.md` contains explanations, worked examples, and three
practice questions. The outline format follows the chapter-tutorial-html
skill. A `::: Question` block followed by an answer and a closing `:::`
becomes a native expandable answer. Numeric `##` headings must match the
contents; `## Practice` is the final section.

To rebuild all eleven pages with Python's standard library:

```sh
python3 tools/build_tutorials.py
```

The builder validates that every subsection in the index has content, then
embeds `tutorial.css` and `tutorial.js` in each root-level `chapter-NN.html`.
The resulting pages work as standalone files with no external fonts,
scripts, or network requests. JavaScript adds chapter search, expand and
collapse controls, formula copying, and complete-chapter printing. Reading,
section navigation, and revealing practice answers work without JavaScript.

Preview the project with `python3 -m http.server 8765` and open `index.html`.
The index has separate links for opening chapters and specific subsections,
preserving its double-click-to-copy labels. `content.html` also lists all
eleven tutorials.
