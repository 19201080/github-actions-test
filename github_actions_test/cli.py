"""Console script for github_actions_test."""
from datetime import datetime
import logging
import os
import random
import sys

import click

logger = logging.getLogger(__name__)
LOG_FORMAT = ('%(asctime)-15s [%(levelname)-7s]: '
              '%(message)s (%(filename)s:%(lineno)s)')
ROOT_DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST_DIRECTORY = 'files'
LOG_FILE = 'log.log'


def get_path_from_root(tail, root=ROOT_DIRECTORY):
    return os.path.join(root, tail)


def log_stuff(warning):
    levels = [logging.INFO, logging.DEBUG]
    if warning:
        levels.append(logging.WARNING)
    for _ in range(10):
        logger.log(levels[random.randint(0, len(levels) - 1)], 'message')


def create_file(message=None):
    # now = datetime.now().isoformat().split('.')[0]
    now = 'test_file'
    dir_path = get_path_from_root(DEST_DIRECTORY)
    logger.info(f'dir path location: {dir_path}')

    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

    with open(get_path_from_root(now, dir_path), 'w') as f:
        f.write(now + '\n')
        if message:
            f.write(message)


@click.command()
@click.option('--warning/--no-warning', '-w', default=False)
def main(warning):
    if os.path.exists(log_path := get_path_from_root(LOG_FILE)):
        os.remove(log_path)
    logging.basicConfig(
        format=LOG_FORMAT,
        level=logging.DEBUG,
        # filename=get_path_from_root(LOG_FILE),
        handlers=[logging.FileHandler(get_path_from_root(LOG_FILE)), logging.StreamHandler()])
    logger.info(f'log file location: {get_path_from_root(LOG_FILE)}')
    log_stuff(warning)
    message = 'warning on' if warning else 'warning off'
    create_file(message)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
