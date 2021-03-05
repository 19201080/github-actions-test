#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


LOG_FORMAT = ('%(asctime)-15s [%(levelname)-7s]: '
              '%(message)s (%(filename)s:%(lineno)s)')
ROOT_DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST_DIRECTORY = 'files'
LOG_FILE = 'log.log'


def get_path_from_root(tail, root=ROOT_DIRECTORY):
    return os.path.join(root, tail)
