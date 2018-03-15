from setuptools.extension import Extension
from setuptools import setup, find_packages

extensions = []
extensions.append( Extension( "clustertree",
                              [ "clustertree/clustertree.pyx"]))
#                                "src/cluster.c"], ) )

setup(version='0.1.0',
	  name='clustertree',
      description="Kanwei Li's clustertree code",
      long_description="Kanwei Li's clustertree code from bx-python",
      author="Kanwei Li (Maintainer=Endre Bakken Stovner)",
      author_email="endrebak85@gmail.com",
      # package_dir = { '': 'lib' },
      packages=find_packages(),
      setup_requires=['cython'],
      ext_modules=extensions,
      test_suite='nose.collector',
      tests_require='nose',
)
