#!/usr/bin/env python3

import setuptools
from distutils.core import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="solaredge_setapp",
    version="0.0.5",
    description="SolarEdge SetApp protocol buffers parser library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT License",
    author="nmakel",
    author_email="",
    url="https://github.com/nmakel/solaredge_setapp",
    packages=["solaredge_setapp"],
    install_requires=[
        "protobuf>=3.6.1",
        "requests>=2.12.4"
    ],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License"
    ]
)
