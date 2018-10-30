#!/usr/bin/env python

from setuptools import find_packages
from setuptools import setup

setup_requires = []
install_requires = [
    'svgpathtools',
]

setup(
    name='svglabel',
    version='0.0.1',
    description='',
    author='Affonso-Gui',
    author_email='affonso@jsk.imi.i.u-tokyo.ac.jp',
    url='https://github.com/Affonso-Gui/svglabel',
    license='MIT License',
    packages=find_packages(),
    zip_safe=False,
    setup_requires=setup_requires,
    install_requires=install_requires,
)
