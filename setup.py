#!/usr/bin/env python

from setuptools import find_packages
from setuptools import setup

setup_requires = []
install_requires = [
    'svgpathtools',
    'pillow',
]

setup(
    name='svglabel',
    version='0.0.1',
    description='Scripts for converting annotation files between svg and json',
    author='Affonso-Gui',
    author_email='affonso@jsk.imi.i.u-tokyo.ac.jp',
    url='https://github.com/Affonso-Gui/svglabel',
    license='MIT License',
    packages=find_packages(),
    zip_safe=False,
    scripts=['json2svg', 'svg2json'],
    setup_requires=setup_requires,
    install_requires=install_requires,
)
