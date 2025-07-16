#!/usr/bin/env python3
# QuickNotes - A simple, fast note-taking app.

# This application provides a quick way to capture notes from your desktop.
# Designed to be frictionless, so you can quickly jot your ideas without 
# interrupting your workflow.

# Simply type your note and press Enter to save it.

# Features:
# - A minimalistic, borderless window that appears in the center of the screen.
# - Saves notes with timestamps to a text file.
# - Type "/open" and press Enter to open the notes file.

# Dependencies:
#   - pyglet: can be installed with pip via `pip install pyglet`

# FYI I have not tested this on any other OS or with any text editors
# I have a personal version of it (also in the repo) 
# which is just based af so if it doesn't work, frankly, 
# I don't care. Deal with it. 

import pyglet
import os
import subprocess
import sys
from datetime import datetime

# --- Configuration ---
# You can change these values to customize the app if you want.

# The file where notes are saved.
# os.path.expanduser("~") ensures this works on all operating systems.
NOTE_FILE = os.path.expanduser("~/quicknotes.txt")

# Window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 60

# Font settings
FONT_NAME = 'monospace'
FONT_SIZE = 20

# Colors are in (Red, Green, Blue, Alpha) format (0-255)
BACKGROUND_COLOR = (40, 40, 40, 230)
TEXT_COLOR = (238, 238, 238, 255)

# A prompt to display in the text box. 
# Best left empty but you do you ig.
PROMPT = ""

# --- End of Configuration ---

def get_center_coordinates(screen_width, screen_height, window_width, window_height):
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    return x, y

def save_note(text):
    if not text.strip():
        return
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(NOTE_FILE, "a") as f:
        f.write(f"[{timestamp}] {text}\n")

def open_notes_file():
    try:
        if not os.path.exists(NOTE_FILE):
            open(NOTE_FILE, 'a').close()

        if sys.platform == "win32":
            os.startfile(NOTE_FILE)
        elif sys.platform == "darwin":
            subprocess.run(["open", NOTE_FILE], check=True)
        else:
            subprocess.run(["xdg-open", NOTE_FILE], check=True)
    except Exception as e:
        print(f"Error opening notes file: {e}")

try:
    display = pyglet.display.get_display()
    screen = display.get_default_screen()
    win_x, win_y = get_center_coordinates(screen.width, screen.height, WINDOW_WIDTH, WINDOW_HEIGHT)
except Exception as e:
    print(f"Could not get screen info, placing window at (0,0). Error: {e}")
    win_x, win_y = 0, 0

window = pyglet.window.Window(
    width=WINDOW_WIDTH,
    height=WINDOW_HEIGHT,
    style='borderless',
    caption='QuickNote'
)
window.set_location(win_x, win_y)
window.set_vsync(False)
window.activate()

batch = pyglet.graphics.Batch()

background = pyglet.shapes.Rectangle(
    0, 0, WINDOW_WIDTH, WINDOW_HEIGHT,
    color=BACKGROUND_COLOR,
    batch=batch
)

document = pyglet.text.document.UnformattedDocument(PROMPT)
document.set_style(0, len(PROMPT), dict(color=TEXT_COLOR, font_name=FONT_NAME, font_size=FONT_SIZE))
layout = pyglet.text.layout.IncrementalTextLayout(
    document,
    width=WINDOW_WIDTH - 20,
    height=WINDOW_HEIGHT,
    multiline=False,
    batch=batch
)
layout.x = 10
layout.y = WINDOW_HEIGHT // 2
layout.anchor_y = 'center'

caret = pyglet.text.caret.Caret(layout, color=(238, 238, 238))
caret.visible = True

@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.ENTER or symbol == pyglet.window.key.NUM_ENTER:
        note_text = document.text[len(PROMPT):]
        if note_text.strip().lower() == "/open":
            open_notes_file()
        else:
            save_note(note_text)
        pyglet.app.exit()
    elif symbol == pyglet.window.key.ESCAPE:
        pyglet.app.exit()

if __name__ == "__main__":
    window.push_handlers(caret)
    pyglet.app.run()
