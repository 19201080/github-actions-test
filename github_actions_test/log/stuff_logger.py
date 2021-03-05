#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import random

logger = logging.getLogger(__name__)


def log_stuff(warning):
    levels = [logging.INFO, logging.DEBUG]
    if warning:
        levels.append(logging.WARNING)
    for _ in range(10):
        logger.log(levels[random.randint(0, len(levels) - 1)], 'message')
