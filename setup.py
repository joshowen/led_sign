#!/usr/bin/env python

from distutils.core import setup

setup(name='led_sign',
      version='0.1',
      description='Python client to LED signs',
      url='https://github.com/metral/led_sign',
      packages=['led_sign',],
      package_dir={'led_sign': 'src'},
      package_data={'led_sign': ['glyphs/*.simpleglyphs',
                                 'bin/*.pl']},
      )
