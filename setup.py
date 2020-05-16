from setuptools import setup
from setuptools import find_packages

MAJOR_VERSION = '0'
MINOR_VERSION = '1'
MICRO_VERSION = '0'
VERSION = "{}.{}.{}".format(MAJOR_VERSION, MINOR_VERSION, MICRO_VERSION)


setup(name='randomalphabet',
      version=VERSION,
      description="Command line tool to encode and decode text",
      url='https://github.com/CorruptedArk',
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
          'Development Status :: 5 - Production/Stable',
          'Topic :: Encryption'
      ],
      packages=find_packages(),
      entry_points={'console_scripts': ['randomalphabet = randomalphabet.randomalphabet:main']},
      zip_safe=False,
      platforms='any')


