#!/usr/bin/env python3

from setuptools import setup, Extension

setup(
	name = "orca",
	version = "1.0",
	ext_modules = [Extension("orca", ["bind.cpp", "liborca.cpp"])]
	);
