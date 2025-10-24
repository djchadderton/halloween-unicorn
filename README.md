# Halloween Unicorn Demo

Small demo that runs a Halloween-themed animation on a Galactic Unicorn
display attached to a Raspberry Pi Pico (or compatible Pico board).

## Features
- Ghosts, bats and pumpkins animated from PNG spritesheets.
- Background colour fades.
- Scrolling text with shadow.

## Requirements
- Raspberry Pi Pico (or Pico-compatible board) with Galactic Unicorn hardware
- MicroPython firmware with the following libraries available on the device:
  - galactic (GalacticUnicorn)
  - picographics (PicoGraphics)
  - pngdec (PNG decoder)
  - Any helper modules included in this repo (e.g. `sequences.py`, sprite PNGs)

The [Pimoroni custom build of MicroPython](https://github.com/pimoroni/pimoroni-pico) includes the GalacticUnicorn, PicoGraphics and PNGdec libraries.

## Repository layout
- main.py — optional entrypoint; copy or rename `halloween.py` to `main.py` for automatic execution on boot
- halloween.py — main demo program (animation loop)
- pngsprite.py — small helper to draw sprites from a PNG spritesheet
- sequences.py — frame sequences used by the demo
- *.png — spritesheet images used by the demo
- README.md — this file

Install / copy to device (example using mpremote on macOS)
1. Find the Pico serial device:
   - ls /dev/tty.*
   - Look for something like `/dev/tty.usbmodemXXXX`
2. Copy files to the Pico filesystem (example):
   - mpremote connect /dev/tty.usbmodemXXXX fs put halloween.py
   - (or copy as main.py to run automatically) mpremote connect /dev/tty.usbmodemXXXX fs put main.py
   - mpremote connect /dev/tty.usbmodemXXXX fs put pngsprite.py
   - mpremote connect /dev/tty.usbmodemXXXX fs put sequences.py
   - mpremote connect /dev/tty.usbmodemXXXX fs put pacman_ghosts.png bat3.png pumpkins.png
   - Or put all files in one command: mpremote connect /dev/tty.usbmodemXXXX fs put .

## Alternate tools
- Thonny: open the project files and use "Save as" -> Raspberry Pi Pico.
- rshell/ampy: also supported if you prefer those tools.

## Running
- After copying, reset the Pico. If the demo file is named `main.py` it will run automatically on boot.
- To run manually from the REPL:
  - import halloween
  - or run: exec(open("halloween.py").read())

## Customisation
- Edit `halloween.py` to change text, colours and sequences:
  - message: variable `text`
  - background/pen colours set via `display.create_pen(...)`
  - spritesheets referenced in `pngsprite` initialisation
- Animation sequences are defined in `sequences.py` and can be edited to change frames, positions, pauses and scale values used by the demo.

## Troubleshooting
- Ensure the sprite PNG files are present on the Pico and the filenames match those in the code.
- If memory/decoding issues occur, try smaller spritesheets or lower scale.
- Verify the required MicroPython libraries are installed for your firmware build.

## License
- MIT License — feel free to reuse and modify for personal projects.