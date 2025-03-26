# Scripts Collection

A collection of useful scripts organized by category.

## Categories

### Document Processing

- `convert_to_pdf` - Converts ODT files to PDF files and merges them into a single PDF file
- `remove_empty_paragraphs` - Removes empty paragraphs from HTML files

### Gaming Utilities

- `skyrim_audio_fix` - Installs xact for Skyrim SE audio fix using winetricks
- `vortex_download` - Downloads mods using Vortex through steamtinkerlaunch

### Network Configuration

- `eduroam-linux-University_of_Toledo.py` - Configures eduroam WiFi for University of Toledo

## Installation

The install script will make the scripts executable and create symbolic links in the `~/.local/bin` directory. This allows you to run the scripts from anywhere in the terminal.

```bash
chmod +x install.sh
./install.sh
```

## Adding New Scripts

To add new scripts:

1. Place the script in the appropriate category directory
2. Make it executable: `chmod +x your_script`
3. Run the install script again: `./install.sh`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.```
