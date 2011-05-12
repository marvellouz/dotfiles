import os, sys

import stat
from shutil import *
from stat import *

HOME_DIR = os.environ['HOME']
ETC_DIR = "/etc/"
SCRIPT_DIR = os.path.join(HOME_DIR, "dotfiles")

dotfiles = [
    os.path.join(HOME_DIR, '.vimrc'),
    os.path.join(HOME_DIR, '.Xdefaults'),
    os.path.join(HOME_DIR, '.vim/'),
    os.path.join(ETC_DIR, 'rc.conf'),
    os.path.join(ETC_DIR, 'fstab'),
    os.path.join(ETC_DIR, 'inittab'),
    ]

