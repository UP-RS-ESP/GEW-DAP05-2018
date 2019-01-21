python2 setup.py build
cp build/lib.*/fib.so .
rm -rf build fib.c
python2 bench.py
rm -rf fib.so pfib.pyc
