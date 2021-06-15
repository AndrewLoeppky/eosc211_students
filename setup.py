#!/usr/bin/env python

# Setup script for PyPI; use CMakeFile.txt to build extension modules

from setuptools import setup, find_packages


setup(
    name='eosc211',
    packages=find_packages(include=['e211_lib']),
    classifiers=[
        'License :: OSI Approved :: BSD License'
    ],
    entry_points={
          'console_scripts': [
              'image_extract = e211_lib.image_extract:main',
              'build_notebook = e211_lib.build_notebook:main'
          ]
    },
    install_requires=['pillow','python-pptx','jupytext'],
    keywords='image powerpoint',
    long_description="""extract powerpoint images""")
