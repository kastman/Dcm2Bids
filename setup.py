#!/usr/bin/env python
# -*- coding: utf-8 -*-


description = """Reorganising NIfTI files from dcm2niix into the Brain Imaging Data Structure"""

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

import glob
from setuptools import setup


DISTNAME = "dcm2bids"
DESCRIPTION = description
VERSION = "1.1.8"
AUTHOR = "Christophe Bedetti"
AUTHOR_EMAIL = "christophe.bedetti@umontreal.ca"
URL = "https://github.com/cbedetti/Dcm2Bids"
DOWNLOAD_URL = URL + "/archive/" + VERSION + ".tar.gz"


if __name__ == "__main__":
    setup(
            name=DISTNAME,
            version=VERSION,
            description=description,
            long_description=long_description,
            author=AUTHOR,
            author_email=AUTHOR_EMAIL,
            url=URL,
            download_url=DOWNLOAD_URL,
            packages=['dcm2bids'],
            scripts=glob.glob('scripts/dcm2bids*'),
            install_requires=['future'],
            )
