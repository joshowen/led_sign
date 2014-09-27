"""A convenience class to send messages to the LED sign.

The client takes a "message" which is a 2-item tuple of strings. The first item
is the top message and the second is the bottom.
"""

from os.path import abspath, dirname, join

from sign import LEDSign, Array
from simplefont import sign_font


_pwd = dirname(abspath(__file__))
_default_glyphs_path = join(_pwd, 'glyphs')


class SignClient:
    def __init__(self, glyphs_path=None, lowlevel_path=None):
        self.lowlevel_path = lowlevel_path if lowlevel_path else _pwd
        self.glyphs_path = glyphs_path if glyphs_path else _default_glyphs_path
        self._font = sign_font(self.glyphs_path)

    def send_message(self, message):

        matrix = self._render_multiline(message)

        if not matrix:
            return False

        text_for_sign = Array().zero_one(matrix)

        # Send text to led sign
        LEDSign(self.lowlevel_path).pic(text_for_sign)
        return True

    def send_multiple_messages(self, messages, empty=('', '')):
        """Send multiple messages to sign.

        messages -- a list of length-2 tuples

        Keyword arguments:
        empty -- the message to show if `messages' is empty (default ('', ''))
        """
        font = sign_font(self.glyphs_path)

        texts_for_sign = []
        for msg in messages:
            texts_for_sign.append(self._render_multiline(msg))

        if texts_for_sign:
            text_for_sign = '\n\n'.join(Array().zero_one(text)
                                        for text in texts_for_sign)
        else:
            text_for_sign = Array().zero_one(self._render_multiline(empty))

        # Send text to led sign
        LEDSign(self.lowlevel_path).pic(text_for_sign)
        return True

    def _render_multiline(self, msg):
        return self._font.render_multiline(
            msg,
            LEDSign.SCREEN_HEIGHT / 2,
            {
                "ignore_shift_h" : True,
                "fixed_width" : LEDSign.SCREEN_WIDTH
                }
            )

