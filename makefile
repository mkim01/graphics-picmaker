all: picmaker.py
	python picmaker.py
	convert pic.ppm pic.png
clean:
	rm *.ppm
	rm *.png
