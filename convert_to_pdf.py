#!/usr/bin/env scriptisto

import argparse
import glob
import shutil
import subprocess
from pathlib import Path

# scriptisto-begin
# script_src: convert_to_pdf.py
# build_cmd: pyinstaller convert_to_pdf.py --onefile
# target_bin: dist/convert_to_pdf
# scriptisto-end


def sort_chapters(file: Path) -> int:
    return int(file.name.split()[1].strip(".pdf"))


def convert_odt_to_pdf(odt_dir: Path, output_pdf: Path) -> None:
    tmp_dir = Path.home() / "tmp"
    files = map(Path, glob.glob("**/*.odt", root_dir=odt_dir, recursive=True))
    file_paths = [odt_dir / file for file in files]
    for file in file_paths:
        try:
            subprocess.run(["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", tmp_dir, file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print(f"Converted {file} to PDF")
        except Exception as e:
            print(f"Error: {e}")
    try:
        pdfs = sorted(map(Path, glob.glob(f"{tmp_dir}/*.pdf")), key=sort_chapters)
        subprocess.run(["pdfunite", *pdfs, output_pdf], check=True)
        print(f"Output PDF: {output_pdf}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        shutil.rmtree(tmp_dir, onexc=print)



def main() -> None:
    parser = argparse.ArgumentParser(description="Convert ODT files to PDF")
    parser.add_argument("-d", type=Path, required=True, help="Directory containing ODT files")
    parser.add_argument("-o", type=Path, help="Output PDF file")

    args = parser.parse_args()
    convert_odt_to_pdf(args.d, args.o)

    
if __name__ == '__main__':
    main()
