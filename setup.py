#!/usr/bin/env python
"""
<Author>
  Jesús V.

<Start Date>
  April 24th, 2019

<Description>
    Basic setup

<Usage>
    Used when executing tests

"""
import os
import sys
from setuptools import setup

setup(
    name="urbvan_test",
    version="1.0.0",
    author="Jesús V.",
    description=("Backend test"),
    packages=["server"],
    install_requires=[],
)
