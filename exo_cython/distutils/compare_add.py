from timeit import timeit
from python_add import pyadd
from cython_add import add

print('Pure Python version: %fs' % timeit('pyadd(1, 2)', 'from python_add import pyadd'))
print('Cython version: %fs' % timeit('add(1, 2)', 'from cython_add import add'))