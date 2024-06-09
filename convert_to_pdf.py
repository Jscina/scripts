import argparse
import glob
import shutil
import subprocess
from enum import StrEnum
from functools import partial
from pathlib import Path


class FileType(StrEnum):
    ODT = ".odt"
    PDF = ".pdf"

def sort_chapters(file: Path, file_type: FileType) -> int:
    return int(file.name.split()[1].strip(file_type.value))

def convert_odt_to_pdf(odt_dir: Path, output_pdf: Path) -> None:
    tmp_dir = Path.home() / "tmp"
    files = map(Path, glob.glob("**/*.odt", root_dir=odt_dir, recursive=True))
    for file in sorted(files, key=partial(sort_chapters, file_type=FileType.ODT)):
        file_path = odt_dir / file
        print(f"Converting {file_path}")
        subprocess.run(["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", tmp_dir, file_path], check=True)
    pdfs = sorted(map(Path, glob.glob(f"{tmp_dir}/*.pdf")), key=partial(sort_chapters, file_type=FileType.PDF))
    subprocess.run(["pdfunite", *pdfs, output_pdf], check=True)
    print(f"Output PDF: {output_pdf}")
    shutil.rmtree(tmp_dir)


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert ODT files to PDF")
    parser.add_argument("-d", type=Path, required=True, help="Directory containing ODT files")
    parser.add_argument("-o", type=Path, help="Output PDF file")

    args = parser.parse_args()
    convert_odt_to_pdf(args.d, args.o)

    
if __name__ == '__main__':
    main()
