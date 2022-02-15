#!/usr/bin/env python

# from distutils.core import setup
# from setuptools import find_packages
#
# setup(name='DjangoModelTracker',
#       version='0.2',
#       description='Track Django Model Objects over time',
#       author='Mohamed El-Kalioby',
#       author_email='mkalioby@mkalioby.com',
#       url='https://github.com/mkalioby/ModelTracker/',
#       packages=('ModelTracker','ModelTracker.migrations'),
#
#    )

from setuptools import find_packages, setup

setup(
    name='django-model-tracker',
    version='1.7.1',
    description='Track Django Model Objects over time',
    author='Mohamed El-Kalioby',
    author_email = 'mkalioby@mkalioby.com',
    url = 'https://github.com/mkalioby/ModelTracker/',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",

    download_url='https://github.com/mkalioby/ModelTracker/',
    license='MIT',
    packages=find_packages(exclude=('TestApp.*', 'TestApp', 'example')),
    install_requires=[
        'Django>=1.7',
        'jsonfield',
        'simplejson'
      ],
    include_package_data=True,
      zip_safe=False, # because we're including static files
        python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.7",
        "Framework :: Django :: 1.8",
        "Framework :: Django :: 1.9",
        "Framework :: Django :: 1.10",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
],

)
