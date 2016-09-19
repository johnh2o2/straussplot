#!/use/bin/env python

from distutils.core import setup

setup(name='straussplot',
      version='0.1.0',
      description='Strauss plot for visualizing sparse and dense data simultaneously',
      long_description=open('README.txt').read(),
      author='John Hoffman',
      author_email='jah5@princeton.edu',
      url='github.com/johnh2o2/straussplot',
      packages=[ 'strauss_plot' ],
      install_requires=[
	"numpy >= 1.0.0",
	"matplotlib >= 1.5.0"
     ],
     license='COPYING.txt'

     )
