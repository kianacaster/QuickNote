
# QuickNotes

A simple, fast note-taking app designed for instant thought capture without interrupting your workflow.

The core idea of QuickNotes is to have a lightweight text box appear with a single keypress, allowing you to jot down a thought, press Enter, and have it disappear. Your note is instantly saved to a timestamped text file, letting you get back to what you were doing with minimal distraction.

The public use version is untested, it might not work and I'm not really that bothered to find out. My personalized version does and that's all that matters.
## Features

- **Minimalist Interface**: A clean, borderless window appears in the center of your screen, ready for input.
- **Instant Save**: Press `Enter` to save your note and exit. Press `Esc` to close without saving.
- **Timestamped Notes**: Every note is automatically saved with the current date and time.
- **Easy Access**: Use the `/open` command to quickly view your entire notes file.
- **Cross-Platform**: Works on Linux, macOS, and Windows.

## Intended Use: Keybinding

QuickNotes is most effective when launched with a global hotkey or keybinding. This allows you to summon the note-taking window from anywhere in your operating system.

For example, you can add the following to your Hyprland configuration (`~/.config/hypr/hyprland.conf`):

```sh
# Keybind to launch QuickNotes
bind = $mainMod, N, exec, python /path/to/your/QuickNotes/quicknote_public.py
```

Replace `$mainMod, N` with your desired key combination and update the path to point to the `quicknote_public.py` script.

## Installation

This project requires the `pyglet` library.

```sh
pip install pyglet
```

## Usage

To run the application, execute the public script:

```sh
python /path/to/your/QuickNotes/quicknote_public.py
```

- **Type your note** and press `Enter` to save it.
- **Type `/open`** and press `Enter` to open your notes file with the default text editor.
- **Press `Esc`** to exit without saving.

## Configuration

The `quicknote_public.py` script includes a configuration section at the top of the file where you can easily customize:

- The location of the notes file (`NOTE_FILE`)
- Window dimensions (`WINDOW_WIDTH`, `WINDOW_HEIGHT`)
- Font settings (`FONT_NAME`, `FONT_SIZE`)
- Colors (`BACKGROUND_COLOR`, `TEXT_COLOR`)

## Project Files

- `quicknote_public.py`: The recommended version for general use. It is cross-platform and easily configurable - hopefully. I haven't actually tested it.
- `quicknote.py`: The original, personalized script for my system that uses specific tools like `kitty` and `zsh`. 

## For more specific configuration/details/stuff, check the .py files themselves, there's some comments and stuff explaining most things I think.
