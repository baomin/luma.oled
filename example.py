#!/usr/bin/env python

# Ported from https://github.com/adafruit/Adafruit_Python_SSD1306/blob/master/examples/shapes.py

from ssd1306 import device, canvas
from PIL import ImageFont, ImageDraw

font = ImageFont.load_default()
oled = device(port=1, address=0x3C)

with canvas(oled) as draw:
    # Draw some shapes.
    # First define some constants to allow easy resizing of shapes.
    padding = 2
    shape_width = 20
    top = padding
    bottom = oled.height-padding
    # Move left to right keeping track of the current x position for drawing shapes.
    x = padding
    # Draw an ellipse.
    draw.ellipse((x, top , x+shape_width, bottom), outline=255, fill=0)
    x += shape_width+padding
    # Draw a rectangle.
    draw.rectangle((x, top, x+shape_width, bottom), outline=255, fill=0)
    x += shape_width+padding
    # Draw a triangle.
    draw.polygon([(x, bottom), (x+shape_width/2, top), (x+shape_width, bottom)], outline=255, fill=0)
    x += shape_width+padding
    # Draw an X.
    draw.line((x, bottom, x+shape_width, top), fill=255)
    draw.line((x, top, x+shape_width, bottom), fill=255)
    x += shape_width+padding

    # Load default font.
    font = ImageFont.load_default()

    # Alternatively load a TTF font.
    # Some other nice fonts to try: http://www.dafont.com/bitmap.php
    #font = ImageFont.truetype('Minecraftia.ttf', 8)

    # Write two lines of text.
    draw.text((x, top),    'Hello',  font=font, fill=255)
    draw.text((x, top+20), 'World!', font=font, fill=255)
