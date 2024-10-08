# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT
# Jason Green 2024

"""
Crossfade example for boards with ONLY a NeoPixel LED.
Includes QT Py and various Trinkeys.

Requires two libraries from the Adafruit CircuitPython Library Bundle.
Download the bundle from circuitpython.org/libraries and copy the
following files to your CIRCUITPY/lib folder:
* neopixel.mpy
* adafruit_pixelbuf.mpy

Once the libraries are copied, save this file as code.py to your CIRCUITPY
drive to run it.
"""
import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)


def crossfade(color1, color2, steps=100, delay=0.01):
    for step in range(steps + 1):
        # Calculate intermediate color
        intermediate_color = (
            int(color1[0] + (color2[0] - color1[0]) * step / steps),
            int(color1[1] + (color2[1] - color1[1]) * step / steps),
            int(color1[2] + (color2[2] - color1[2]) * step / steps),
        )
        # Set LED color
        pixels.fill(intermediate_color)
        time.sleep(delay)


print("GCS SREM Monitoring Activated!")

while True:
    # Define mint green and cyan with max brightness of 15
    mint_green = (0, 14, 0)  # Mint green
    cyan = (0, 7, 7)  # Cyan

    # Crossfade from mint green to cyan
    crossfade(mint_green, cyan)

    # Crossfade back from cyan to mint green
    crossfade(cyan, mint_green)
