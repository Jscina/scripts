#!/bin/bash

files=$(ls -A)

for file in ${files[@]}; do
	if [[ $file == "install.sh" || $file == "README.md" || $file == "LICENSE" || $file == ".gitignore" ]]; then
		continue
	elif [[ -d "$file" ]]; then
		continue
	fi

	if [ ! -d ~/.local/bin ]; then
		echo "Creating ~/.local/bin"
		mkdir -p ~/.local/bin
	fi

	echo "Checking if $file link exists"
	if [ -L "~/.local/bin/$file" ]; then
		echo "Removing existing symlink ~/.local/bin/$file"
		rm ~/.local/bin/$file
	fi

	if [ -f "$file" ]; then
		echo "Installing $file"
		chmod +x $file
		ln -s "$(pwd)/$file" ~/.local/bin/$file
	fi
done
