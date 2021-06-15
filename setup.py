#!/usr/bin/env python

from setuptools import setup, find_packages
from setuptools_scm import get_version

setup(
    name='eosc211',
    version=get_version(),
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
    keywords='image powerpoint',
    long_description="""e211 course conversion""")
