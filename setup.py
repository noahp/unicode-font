# -*- coding: utf-8 -*-

"""
Package setup.

Set me up with `python setup.py bdist_wheel --universal`
"""
import io
import json
import os

from setuptools import setup

# Get long description from readme
with io.open("README.md", "rt", encoding="utf8") as readmefile:
    README = readmefile.read()

setup(
    name="unicode-font",
    version="0.1.0",
    description="Fancy fonts",
    author="Noah Pendleton",
    author_email="noahp@users.noreply.github.com",
    url="https://github.com/noahp/unicode-font",
    project_urls={
        "Code": "https://github.com/noahp/unicode-font",
        "Issue tracker": "https://github.com/noahp/unicode-font/issues",
    },
    long_description=README,
    long_description_content_type="text/markdown",
    install_requires=["click"],
    # using markdown as pypi description:
    # https://dustingram.com/articles/2018/03/16/markdown-descriptions-on-pypi
    setup_requires=["setuptools>=38.6.0", "wheel>=0.31.0", "twine>=1.11.0"],
    py_modules=["unicode_font"],
    entry_points={"console_scripts": ["unicode-font = unicode_font:main"]},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
)
