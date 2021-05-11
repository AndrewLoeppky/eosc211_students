"""Iterate folder tree and produce .md from .pptx files
"""
import build_notebook
import image_extract
from pathlib import Path

the_dir = Path()
dest_dir = Path().home()

all_pptx = ["**/*.pptx"]
for a_pptx in all_pptx:
    list_pptx = list(the_dir.glob(a_pptx))
    for the_file in list_pptx:
        media = Path(f"{the_file.stem}_media")
        image_extract(the_file, media)
        build_notebook(the_file, media)
        print(f"converted {media} to markdown")
