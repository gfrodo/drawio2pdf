#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import subprocess
import pymupdf
import argparse
import os

parser = argparse.ArgumentParser(description="Convert drawio files to pdf with layers")
parser.add_argument("-o", "--output", help="pdf output file name", default="ouput.pdf")
parser.add_argument("input", help="drawio input file name")
args = parser.parse_args()

tree = ET.parse(args.input)
root = tree.getroot()

layers = []
for x in root[0][0][0]:
    if x.tag == "mxCell" and x.attrib.get("parent") == "0":
        layers.append({"name": x.attrib["value"], "visible": x.attrib.get("visible") != "0"})
    if x.tag == "object" and x[0].attrib.get("parent") == "0":
        layers.append({"name": x.attrib["label"], "visible": x[0].attrib.get("visible") != "0"})

print(layers)

subprocess.run(["drawio", "-l", "-1", "-t", "-o", ".base.pdf", "-x", args.input])
doc = pymupdf.open(".base.pdf")
page = doc.load_page(0)

for i, layer in enumerate(layers):
    subprocess.run(["drawio", "-l", str(i), "-t", "-o", ".layer.pdf", "-x", args.input])
    doc_layer = pymupdf.open(".layer.pdf")
    xref = doc.add_ocg(layer["name"], on=layer["visible"])
    page.show_pdf_page(page.rect, doc_layer, 0, oc=xref)
    doc_layer.close()

doc.save(args.output)
doc.close()
os.remove(".base.pdf")
os.remove(".layer.pdf")
