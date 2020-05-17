# random-alphabet-py
## Description
A command line tool to encode and decode text using a randomized cipher written in Python

## Usage
If installed on your system, you run as `randomalphabet` with valid arguments from any directory. 
If not installed, run `python3 randomalphabet` from this git project root directory. 

To view command line arguments and options use `randomalphabet -h` or `randomalphabet --help`

## Installation
To install without a distro specific package, run `make install` from the project root directory.

On Debian and Ubuntu based distros you can install the .deb package once it is released.
On Red Hat and Fedora based distros you can install the .rpm package once it is released.

## Packaging
To build a .deb package, first install the package `stdeb` either from apt or pip3. 
Next, run `make deb` from this project root directory.

To build a .rpm package, first install the package `rpmdevtools` from dnf.
Next, run `make rpm` from this project root directory.
