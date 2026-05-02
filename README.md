# Static Site Generator

A markdown-to-HTML static site generator built in Python, created as part of the [Boot.dev](https://www.boot.dev) backend development course.

## What It Does

Takes a directory of markdown files and converts them into a fully functional static website. You write your content in markdown, run the generator, and it outputs clean HTML pages ready to serve — or in this case, deploy to GitHub Pages.

Live site: [https://oaftobar.github.io/staticSite/](https://oaftobar.github.io/staticSite/)

## How It Works

The generator is built in layers, each one building on the last:

1. **Inline markdown parsing** — converts raw text into `TextNode` objects, handling bold, italic, code, links, and images
2. **HTML node tree** — a `LeafNode` and `ParentNode` class system that represents HTML as a tree before rendering it to a string
3. **Block markdown parsing** — splits a full markdown document into blocks (paragraphs, headings, code blocks, quotes, lists) and determines the type of each
4. **Page generation** — reads markdown files, converts them to HTML, injects them into an HTML template, and writes the output
5. **Recursive file handling** — copies static assets and generates pages for every markdown file found in the content directory

## Running It Locally

```bash
./main.sh
```

Then open `http://localhost:8888` in your browser.

## Building for Production

```bash
./build.sh
```

This generates the site into the `docs/` directory with the correct base path for GitHub Pages.

## Project Structure

```
content/        # Markdown source files
static/         # Static assets (CSS, images)
docs/           # Generated site output (committed for GitHub Pages)
src/            # Python source code
template.html   # HTML template with {{ Title }} and {{ Content }} placeholders
```

## What I Learned

This was my first real Python project of this scale. Coming in, I understood the basics but struggled with a lot of the details.

**Things that tripped me up:**
- Class inheritance and `super().__init__()` — I kept passing `self` manually and mixing up positional vs keyword arguments until it finally clicked
- Indentation errors were a constant battle, especially as files got longer
- Circular imports — I didn't know this was even a thing until I almost created one between `textnode.py` and `inline_markdown.py`
- Recursive functions — the `split_nodes_image` function in particular took a while to get right, specifically tracking the "remaining" text after each image was extracted
- Git — I didn't commit throughout the project and had to set everything up at the end, which was its own adventure

**Things I got better at:**
- Knowing when to create a new file vs. add to an existing one
- Python list comprehensions — by the end I was writing them naturally
- Reading error messages and tracing them back to the actual problem
- Thinking about where functions belong based on their imports and dependencies

## Built With

- Python 3
- Zero external dependencies — just the standard library
