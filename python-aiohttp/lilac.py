#!/usr/bin/env python3

import fileinput

from lilaclib import *

build_prefix = 'extra-x86_64'
depends = ['python-multidict-git', 'python-async_timeout']

def pre_build():
  pypi_pre_build(
    depends = ['python-chardet', 'python-multidict', 'python-async_timeout'],
    depends_setuptools = False,
    makedepends = ['cython'],
    arch = ['i686', 'x86_64'],
  )

post_build = pypi_post_build

if __name__ == '__main__':
  single_main()
