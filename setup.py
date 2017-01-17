"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='FastaIndex',
      version='0.11rc7',
      description='',
      long_description=long_description,
      author='Leszek Pryszcz',
      author_email='l.p.pryszcz+distutils@gmail.com',
      url='https://github.com/lpryszcz/FastaIndex',
      license='GPLv2',
      
      py_modules=['FastaIndex', "fasta_stats"],

      entry_points = {"console_scripts":
                      ["FastaIndex = FastaIndex:main", 
                       "fasta_stats = fasta_stats:main"]
                     }, 
      
      classifiers=[
          # How mature is this project? Common values are  3 - Alpha 4 - Beta 5 - Production/Stable
          'Development Status :: 4 - Beta',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
      ],

      keywords='FastA indexing stats N50 N90',
      
     )
