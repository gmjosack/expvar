#!/usr/bin/env python

import setuptools
from distutils.core import setup

expvar = __import__('expvar')

kwargs = {
    "name": "expvar",
    "version": str(expvar.__version__),
    "packages": ["expvar"],
    "description": "Store and retrieve TOTP secrets/tokens.",
    # PyPi, despite not parsing markdown, will prefer the README.md to the
    # standard README. Explicitly read it here.
    "long_description": open("README").read(),
    "author": "Gary M. Josack",
    "maintainer": "Gary M. Josack",
    "author_email": "gary@byoteki.com",
    "maintainer_email": "gary@byoteki.com",
    "license": "MIT",
    "url": "https://github.com/gmjosack/expvar",
    "download_url": "https://github.com/gmjosack/expvar/archive/master.tar.gz",
    "classifiers": [
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
}

setup(**kwargs)
