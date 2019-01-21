python2 setup.py build
cp build/lib.*/ytrees.so .
rm -rf build ytrees.c
python2 bench.py
rm -rf ytrees.so ptrees.pyc
