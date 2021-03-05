"""Console script for github_actions_test."""
import logging
import os
import sys

import click

from github_actions_test.log.stuff_logger import log_stuff
from github_actions_test.utils import get_path_from_root, LOG_FILE, LOG_FORMAT
from github_actions_test.file_creator import create_file

logger = logging.getLogger(__name__)


@click.command()
@click.option('--warning/--no-warning', '-w', default=False)
@click.option('--file/--no-file', ' /-n', default=True)
def main(warning, file):
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
    if file:
        create_file(message)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
