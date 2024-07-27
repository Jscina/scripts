#!/bin/bash

if [ $# -gt 0 ]; then
	echo "Usage: ./install.sh"
	exit 1
fi

$files=$(ls -A)

for file in $files; do
	if [ $file == "install.sh" || $file == "README.txt" || $file == "LICENSE"]; then
		continue
	fi

	if [ -f "$file" ]; then
		echo "Installing $file"
		chmod +x $file
		ln -s "$(pwd)/$file" ~/.local/bin/$file
	fi
done
