# drawio2pdf
convert drawio files to pdf using the drawio CLI.
Layers in drawio will be converted to OCGs (optional content groups) with the correct name and visibility as in the drawing.
Those Layers/OCGs can be enabled/disabled in most modern PDF viewers.

usage: drawio2pdf.py input.drawio -o output.pdf

## Requirements
python module: pymupdf

drawio desktop app in PATH as `drawio`.

## Limitations
Currently only the first drawio page is converted.
