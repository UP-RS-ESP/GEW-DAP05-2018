python2 setup.py build
cp build/lib.*/mog.so .
rm -rf build mog.c
python2 bench.py
rm -rf mog.so pmog.pyc
