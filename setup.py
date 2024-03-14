from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
import numpy
import os

# Adjust these paths according to your build environment
rnnoise_lib_dir = os.path.abspath("./build/lib/Debug")  # Adjust based on where CMake outputs the libraries
rnnoise_include_dir = os.path.abspath("./include")  # Adjust to where your include files are

wrapper_extension = Extension(
    name="pyrnnoise.wrapper",  # Updated to reflect new package name
    sources=["pyrnnoise/wrapper.pyx"],
    libraries=["rnnoise"],  # Link against the rnnoise library
    library_dirs=[rnnoise_lib_dir],  # Directory where the rnnoise library is located
    include_dirs=[numpy.get_include(), rnnoise_include_dir],  # Include dirs for numpy and rnnoise headers
)

setup(
    name='pyrnnoise',
    version='0.1',
    author='Ma5onic',
    description='Python wrapper for RNNoise using Cython',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jagger2048/rnnoise-windows/',
    packages=find_packages(),
    ext_modules=cythonize([wrapper_extension], annotate=True, compiler_directives={'language_level' : "3"}),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
    ],
    python_requires='>=3.7',
    install_requires=[
        'numpy',
        'Cython',
    ],
)