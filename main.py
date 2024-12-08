import os
import sys

import pytest
from fildapi.config import Cfg


def update_config():
    api_token = os.environ.get('SAMPLE_API_TEST_TOKEN')

    if api_token:
        Cfg.App.token = api_token


def run_tests():
    """
    Pytest exit codes:
      EXIT_OK = 0
      EXIT_TESTSFAILED = 1
      EXIT_INTERRUPTED = 2
      EXIT_INTERNALERROR = 3
      EXIT_USAGEERROR = 4
      EXIT_NOTESTSCOLLECTED = 5
    """
    args = [
        './tests', '-s', '--junitxml', './test-report.xml',
        '--disable-warnings',
    ]
    exit_code = pytest.main(args)

    if exit_code not in (0, 1,):
        exit_code = 1

    sys.exit(exit_code)


def main():
    update_config()
    run_tests()


if __name__ == '__main__':
    main()
