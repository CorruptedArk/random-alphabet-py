install:
	sudo python3 setup.py install --record files.txt

uninstall:
	tr '\n' '\0' < files.txt | xargs -0 sudo rm -f --

package:
	python3 setup.py --command-packages=stdeb.command bdist_deb
	
