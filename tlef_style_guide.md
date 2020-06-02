# TLEF Style Guide

## Writing UBC EOAS Course Content With Markdown, Jupyter and Sphinx

---
> Andrew Loeppky<br>
> Teaching and Learning Enhancement Fund<br>
> Summer 2019

The goal of this document is to create a reference standard for writing course content in .md and .ipynb that is both easy to follow and seamlessly builds into executable books via Sphinx. Templates are provided for generating lecture slides (powerpoint style), student worksheets (word docs or pdf style) and laboroatory assignments with jupyter notebooks (ipynb).

The formatting presented here is based on guidelines from the [Executable Book Project](<https://github.com/executablebooks/jupyter-book/tree/master/docs/content>) (EBP), as well as the rules followed by a [markdown linter](<https://github.com/DavidAnson/markdownlint/blob/v0.20.3/doc/Rules.md#md033>) written by David Anson. Numerous "flavours" of markdown exist with various [parsers](<https://stackoverflow.com/questions/2933192/what-is-parsing-in-terms-that-a-new-programmer-would-understand>) (e.g. *Github flavoured markdown, CommonMark, Markdown Extra, ExtraMark, etc.*), with *some* cross compatability, but there is no real standard as of yet. There are often a number of ways to achieve the same output; for example, something as simple as a line break can be written as:

```markdown
line1\ line2
```

or

```markdown
line1 <br> line2
```

or

```markdown
line1

line2
```

All of these will produce the same output:

>line1 <br> line2

Not every syntax will work in every markdown flavour, so beware that simply searching online "how to create a line break in markdown" (or whatever it is you're trying to do) may give an answer that will not be compatible with the EBP framework. We are producing course content with **Jupyter Book**, which uses either the *MyST* or *CommonMark* variants of markdown (MyST is based on CommonMark with added features). MyST has the advantage of being able to run as executable notebooks, i.e. it's extremely handy for live coding in a lecture setting, as you can actually run code blocks embedded in the slides. Using the templates provided below, instructors and TA's can ensure clean builds from raw .md files to Jupyter Books, and create presentation-ready content with relatively little headache. For anything not captured by the templates that you may wish to include in your slides/labs, refer to the full description from the [MyST docs](<https://myst-parser.readthedocs.io/en/latest/using/syntax.html>).

## Formatting Slides

---

```markdown

# Title

## Subtitle

---

> Course Title
> Week # N
 ```
