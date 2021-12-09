import os
import sys

WIN_TITLE = 'Image Drawer'
WIN_WIDTH = 600
WIN_HEIGHT = 800
WIN_SIZE = WIN_WIDTH, WIN_HEIGHT
WIN_SIZE_TK = 'x'.join(map(str, WIN_SIZE))

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CANVAS_BG_COLOR = 'black'
CANVAS_BRUSH_COLOR = 'white'
CANVAS_BRUSH_SIZE = 8

POSTSCRIPT_IMAGES_FOLDER = os.sep.join(
    [
        os.path.dirname(os.path.realpath(__file__)),
        'temp', 'postscript_images',
    ]
) + os.sep
POSTSCRIPT_IMAGE_NAME = 'pstemp.ps'

IMG_FOLDER = os.sep.join(
    [
        os.path.dirname(os.path.realpath(__file__)),
        'img',
    ]
) + os.sep

DATASET_FOLDER = os.sep.join(
    [
        os.path.dirname(os.path.realpath(__file__)),
        'img', 'dataset',
    ]
) + os.sep

RADIO_BUTTON_OPTIONS = {
    0: 'Aries',
    1: 'Taurus',
    2: 'Gemini',
    3: 'Cancer',
    4: 'Leo',
    5: 'Virgo',
    6: 'Libra',
    7: 'Scorpio',
    8: 'Sagittarius',
    9: 'Capricorn',
    10: 'Aquarius',
    11: 'Pisces',
}
