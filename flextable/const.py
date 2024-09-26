####################################################################################################
#
# Flex Text Table
# Fast and flexible Pyhon library for text tables.
#
# Copyright ©2023-2024 Marcin Orlowski <mail [@] MarcinOrlowski.com>
# https://github.com/MarcinOrlowski/python-flex-text-table/
#
####################################################################################################

from typing import List, Final


class Const(object):
    APP_NAME: Final[str] = 'flex-text-table'
    APP_VERSION: Final[str] = '2.7.0'
    APP_URL: Final[str] = 'https://github.com/MarcinOrlowski/python-flex-text-table/'
    APP_SUMMARY: Final[str] = 'Fast and flexible Pyhon library for text tables.'
    APP_INITIAL_YEAR: Final[int] = 2023

    APP_DESCRIPTION: Final[List[str]] = [
        f'{APP_NAME} v{APP_VERSION} * Copyright {APP_INITIAL_YEAR} by Marcin Orlowski.',
        f'{APP_SUMMARY}',
        f'{APP_URL}',
    ]
