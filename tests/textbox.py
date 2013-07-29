#!/usr/bin/env python
from pilex import ImageDraw
import Image
import ImageFont
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-a", "--halign", default='left')
options, args = parser.parse_args()

lines = open('../LICENSE', 'r').read()
image = Image.new('RGB', (512, 512), 'white')
font = ImageFont.truetype('droid-sans.ttf', 20)
draw = ImageDraw.Draw(image)
draw.textbox(
    (10, 10, 492, 492), lines, font, 'black', halign=options.halign
)
del draw
image.show()
