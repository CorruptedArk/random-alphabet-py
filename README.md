# random-alphabet-py
## Description
A command line tool to encode and decode text using a randomized cipher written in Python.

I do not recommend using this program for any security or privacy critical purposes. 
I am not specialized in cryptography or security. This is a hobby project that I thought was cool.

Encoding generated with this program is not compatible with [RandomAlphabet](https://github.com/CorruptedArk/RandomAlphabet) or vice-versa.

## Usage
If installed on your system, you run as `randomalphabet` with valid arguments from any directory. 
If not installed, run `python3 randomalphabet` from this git project root directory. 

To view command line arguments and options use `randomalphabet -h` or `randomalphabet --help`

## Installation
To install without a distro specific package, run `make install` from the project root directory.

### Debian Package
You can install it from my [PPA](https://launchpad.net/~corruptedark/+archive/ubuntu/ppa).

#### On Ubuntu 20.04+ based distros 
To add the repository to your system, run:
```
sudo add-apt-repository ppa:corruptedark/ppa
sudo apt update
```
After adding the repository, install the package with: 

`sudo apt install python3-randomalphabet`

#### On Debian Buster
First install `software-properties-common`
	
Then to add the repository to your system, run:
```
sudo sh -c 'echo "deb http://ppa.launchpad.net/corruptedark/ppa/ubuntu focal main\ndeb-src http://ppa.launchpad.net/corruptedark/ppa/ubuntu focal main" > /etc/apt/sources.list.d/corruptedark.list'
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E2BA18922C0D6991
sudo apt update
```
After adding the repository, install the package with: 

`sudo apt install python3-randomalphabet`

### Red Hat Package
On Red Hat and Fedora based distros you can install the .rpm package once it is released.

## Packaging
To build a .deb package, first install the package `stdeb` either from apt or pip3. 
Next, run `make deb` from this project root directory.

To build a .rpm package, first install the package `rpmdevtools` from dnf.
Next, run `make rpm` from this project root directory.
