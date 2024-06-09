#!/usr/bin/env scriptisto

import argparse
import glob
import shutil
import subprocess
from multiprocessing import Pool, cpu_count
from pathlib import Path

# scriptisto-begin
# script_src: convert_to_pdf.py
# build_cmd: pyinstaller convert_to_pdf.py --onefile
# target_bin: dist/convert_to_pdf
# scriptisto-end



def sort_chapters(file: Path) -> int:
    return int(file.name.split()[1].strip(".pdf"))

def process_odt_files(tmp_dir: Path, file_path: Path) -> None:
    subprocess.run(["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", tmp_dir, file_path], check=True)

def convert_odt_to_pdf(odt_dir: Path, output_pdf: Path) -> None:
    tmp_dir = Path.home() / "tmp"
    files = map(Path, glob.glob("**/*.odt", root_dir=odt_dir, recursive=True))
    file_paths = [odt_dir / file for file in files]
    with Pool(cpu_count()) as pool:
        pool.starmap(process_odt_files, [(tmp_dir, file_path) for file_path in file_paths])
    pdfs = sorted(map(Path, glob.glob(f"{tmp_dir}/*.pdf")), key=sort_chapters)
    subprocess.run(["pdfunite", *pdfs, output_pdf], check=True)
    print(f"Output PDF: {output_pdf}")
    shutil.rmtree(tmp_dir, onexc=print)


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert ODT files to PDF")
    parser.add_argument("-d", type=Path, required=True, help="Directory containing ODT files")
    parser.add_argument("-o", type=Path, help="Output PDF file")

    args = parser.parse_args()
    convert_odt_to_pdf(args.d, args.o)

    
if __name__ == '__main__':
    main()
