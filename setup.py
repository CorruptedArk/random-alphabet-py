# random-alphabet-py is a command line tool to encode and decode text using a randomized cipher
#   Copyright (C) 2020  Noah Stanford <noahstandingford@gmail.com>
# 
#   random-aphabet-py is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
# 
#   random-alphabet-py is distributed in the hope that it will be interesting and useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
# 
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""This module handles installation, packaging, and running of the randomalphabet package"""

from setuptools import setup
from setuptools import find_packages
from randomalphabet.__main__ import get_version


setup(name='randomalphabet',
      version=get_version(),
      description="A command line tool to encode and decode text",
      url="https://github.com/CorruptedArk/random-alphabet-py",
      author='CorruptedArk',
      author_email='noahstandingford@gmail.com',
      license='GPLv3',
      classifiers=[
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.6',
          'Topic :: Encryption'
      ],
      packages=find_packages(),
      entry_points={'console_scripts': ['randomalphabet = randomalphabet.__main__:main']},
      zip_safe=False,
      platforms='any')
