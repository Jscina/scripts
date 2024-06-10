# Scripts

Just a collection of random utility scripts using scriptisto and python

## Scriptisto Config

To configure scriptisto, add the following comments to the script file

```python
  #!/usr/bin/env scriptisto
  # scriptisto-begin
  # script_src: script.py
  # build_cmd: pyinstaller script.py --onefile
  # target_bin: dist/script
  # scriptisto-end
```

Sym link to `~/.local/bin` to make them available globally

```bash
  ln -s /path/to/script ~/.local/bin
```
