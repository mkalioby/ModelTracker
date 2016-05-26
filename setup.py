#!/usr/bin/env python

from distutils.core import setup
#from setuptools import find_packages

setup(name='DjangoModelTracker',
      version='0.1',
      description='Track Django Model Objects over time',
      author='Mohamed El-Kalioby',
      author_email='mkalioby@mkalioby.com',
      url='https://github.com/mkalioby/ModelTracker/',
      packages=('ModelTracker','ModelTracker.migrations'),
   )