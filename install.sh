#!/usr/bin/env bash

# Ensure ~/.local/bin exists
if [ ! -d ~/.local/bin ]; then
	echo "Creating ~/.local/bin directory"
	mkdir -p ~/.local/bin
fi

# Function to install a script
install_script() {
	local script_path="$1"
	local script_name=$(basename "$script_path")

	echo "Installing $script_name"

	# Make script executable
	chmod +x "$script_path"

	# Check if a symlink already exists
	if [ -L "$HOME/.local/bin/$script_name" ]; then
		echo "Removing existing symlink ~/.local/bin/$script_name"
		rm "$HOME/.local/bin/$script_name"
	fi

	# Create symlink
	ln -s "$(pwd)/$script_path" "$HOME/.local/bin/$script_name"
	echo "Installed $script_name successfully!"
}

# Files to exclude from installation
EXCLUDE_FILES=("install.sh" "README.md" "LICENSE" ".gitignore")

# Install scripts recursively from all directories
find_and_install() {
	local current_dir="$1"

	for file in "$current_dir"/*; do
		# Get basename for checking against exclude list
		filename=$(basename "$file")

		# Skip excluded files
		if [[ " ${EXCLUDE_FILES[@]} " =~ " $filename " ]]; then
			continue
		fi

		# If directory, recurse into it
		if [ -d "$file" ]; then
			find_and_install "$file"
		# If file, install it
		elif [ -f "$file" ]; then
			install_script "$file"
		fi
	done
}

# Start installation from current directory
echo "Starting installation of scripts..."
find_and_install "."
echo "All scripts installed successfully!"
