import os
from src.client import SignClient

multiline_test = []

top_line = "Python rocks!"
bottom_line = "Ruby is cool too :)"
multiline_test = [top_line, bottom_line]

pwd = os.path.dirname(os.path.realpath(__file__))
lowlevel_path = os.path.join(pwd, 'src', 'bin')
glyphs_path = os.path.join(pwd, 'src', 'glyphs')

SignClient(glyphs_path, lowlevel_path).send_message(multiline_test)
