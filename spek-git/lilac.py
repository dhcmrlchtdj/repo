#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if 'git describe' in line:
            print(line.replace('|',' 2>/dev/null |'))
        elif 'makedepends' in line:
            print(line.replace(')',' \'intltool\')'))
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
  single_main(build_prefix)
