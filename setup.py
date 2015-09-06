#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import re
import os

def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, 'ec2snap')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


version = get_version('ec2snap')

setup(
    name='ec2snap',
    version=version,
    packages=get_packages('ec2snap'),
    package_data=get_package_data('ec2snap'),
    scripts=['ec2snap/ec2snap'],
    author="Pierre Mavro",
    author_email="deimos@deimos.fr",
    description="Simple solution to backup ec2 instances using snapshots",
    install_requires=[
        'boto>=2.34.0'
    ],
    include_package_data=True,
    url='https://github.com/enovance/ec2_snapshot',
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Environment :: Console",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Communications",
    ]
)
