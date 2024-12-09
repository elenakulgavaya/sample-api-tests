import argparse
import os
import sys

import pytest

from fildapi.config import Cfg


def update_config():
    api_token = os.environ.get('SAMPLE_API_TEST_TOKEN')

    if api_token:
        Cfg.App.token = api_token


def run_tests(xml_report=True):
    """
    Pytest exit codes:
      EXIT_OK = 0
      EXIT_TESTSFAILED = 1
      EXIT_INTERRUPTED = 2
      EXIT_INTERNALERROR = 3
      EXIT_USAGEERROR = 4
      EXIT_NOTESTSCOLLECTED = 5
    """
    args = ['./tests', '-s', '--disable-warnings']

    if xml_report:
        args.extend(['--junitxml', './test-report.xml'])

    exit_code = pytest.main(args)

    if exit_code not in (0, 1,):
        exit_code = 1

    sys.exit(exit_code)


def main():
    parser = argparse.ArgumentParser(description='Run pytest')
    parser.add_argument('--local', dest='is_local', action='store_true')
    parser.set_defaults(is_local=False)
    args = parser.parse_args()

    update_config()
    run_tests(xml_report=not args.is_local)


if __name__ == '__main__':
    main()
