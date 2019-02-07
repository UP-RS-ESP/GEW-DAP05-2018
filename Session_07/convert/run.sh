python2 setup.py build
cp build/lib.*/vrt.so .
rm -rf build vrt.c
python2 bench.py
