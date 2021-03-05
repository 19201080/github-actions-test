#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import logging
import os

from github_actions_test.utils import get_path_from_root, DEST_DIRECTORY

logger = logging.getLogger(__name__)


def create_file(message=None):
    now = datetime.now().isoformat().split('.')[0]
    dir_path = get_path_from_root(DEST_DIRECTORY)
    logger.info(f'dir path location: {dir_path}')

    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

    with open(get_path_from_root(now, dir_path), 'w') as f:
        f.write(now + '\n')
        if message:
            f.write(message)
