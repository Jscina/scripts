#!/bin/bash

# Convert ODT files to PD
convert_odt_to_pdf() {
	local odt_dir=$1
	local tmp_dir=$2

	find "$odt_dir" -name "*.odt" -type f -print0 | while IFS= read -r -d '' file; do
		libreoffice --headless --convert-to pdf --outdir "$tmp_dir" "$file" >/dev/null 2>&1
		if [ $? -eq 0 ]; then
			echo "Converted $file to PDF"
		else
			echo "Error converting $file to PDF"
		fi
	done
}

# Combine PDF files into a single PDF
combine_pdfs() {
	local output_pdf=$1
	local tmp_dir=$2

	# Sort PDF files by chapter number
	sorted_pdfs=()
	while IFS= read -r -d $'\0'; do
		sorted_pdfs+=("$REPLY")
	done < <(find "$tmp_dir" -name "*.pdf" -print0 | sort -zV)

	pdfunite "${sorted_pdfs[@]}" "$output_pdf"

	if [ $? -eq 0 ]; then
		echo "Output PDF: $output_pdf"
	else
		echo "Error combining PDFs to $output_pdf"
	fi
}

main() {
	if [ $# -ne 2 ]; then
		echo "Usage: $0 <odt_dir> <output_pdf>"
		exit 1
	fi

	local odt_dir=$1
	local output_pdf=$2
	local tmp_dir="$HOME/tmp"

	if [ ! -d "$tmp_dir" ]; then
		mkdir -p "$tmp_dir"
	fi

	convert_odt_to_pdf "$odt_dir" "$tmp_dir"
	combine_pdfs "$output_pdf" "$tmp_dir"

	rm -rf "$tmp_dir"
}

main "$@"
