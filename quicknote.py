## QuickNote but for my highly specific usecase

# Probably don't use this.

# If you use Linux (idk which ones will work, I'm on arch/hyprland)
# and you use kitty as your terminal, with a Zsh shell and OhMyZsh (think that's what it's called)
# and you have a CLEANLAUNCH variable set to 0 by default in your zsh config file
# because you have loads of ascii art and shit that pop up when you launch
# the terminal and you don't want that all to appear when 
# launching the terminal to show the text file with /open
# and xdg-open doesn't work and you can't be bothered
# to set up your system properly:
# this is the program for you!
# send me 20 quid


#!/usr/bin/env python3
import pyglet
import os
import subprocess
from datetime import datetime

NOTE_FILE = os.path.expanduser("~/notes.txt")
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 60
FONT_NAME = 'monospace'
FONT_SIZE = 20
BACKGROUND_COLOR = (40, 40, 40, 230)
TEXT_COLOR = (238, 238, 238, 255) 
PROMPT = ""

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

display = pyglet.display.get_display()
screen = display.get_default_screen()

win_x, win_y = get_center_coordinates(screen.width, screen.height, WINDOW_WIDTH, WINDOW_HEIGHT)

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
    if symbol == pyglet.window.key.ENTER:
        note_text = document.text[len(PROMPT):]
        if note_text.strip() == "/open":
            try:
                subprocess.Popen(['kitty', '--hold', 'zsh', '-c', f'cat {NOTE_FILE}'], env={'CLEANLAUNCH': '1', **os.environ}, start_new_session=True, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except FileNotFoundError:
                print("Error: kitty not found. Please install it or change the command to your preferred terminal emulator.")
            pyglet.app.exit()
        else:
            save_note(note_text)
            pyglet.app.exit()
    elif symbol == pyglet.window.key.ESCAPE:
        pyglet.app.exit()

window.push_handlers(caret)

pyglet.app.run()

