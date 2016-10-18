#!/usr/bin/env python

#from distutils.core import setup
#from setuptools import find_packages

"""setup(name='DjangoModelTracker',
      version='0.2',
      description='Track Django Model Objects over time',
      author='Mohamed El-Kalioby',
      author_email='mkalioby@mkalioby.com',
      url='https://github.com/mkalioby/ModelTracker/',
      packages=('ModelTracker','ModelTracker.migrations'),

   )"""

from setuptools import find_packages, setup

setup(
    name='DjangoModelTracker',
    version='0.6.0',
    description='Track Django Model Objects over time',
    author='Mohamed El-Kalioby',
    author_email = 'mkalioby@mkalioby.com',
    url = 'https://github.com/mkalioby/ModelTracker/',

    download_url='https://github.com/mkalioby/ModelTracker/',
    license='MIT',
    packages=find_packages(exclude=('TestApp.*', 'TestApp', 'example')),
    install_requires=[
        'Django>=1.7',
      ],
    include_package_data=True,
      zip_safe=False, # because we're including static files
)
