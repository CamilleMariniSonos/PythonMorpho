from distutils.core import setup
from Cython.Build import cythonize

setup(name="cython_add",
      ext_modules = cythonize("cython_add.pyx")
)