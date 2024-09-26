####################################################################
#
# Flex Text Table
# Fast and flexible Pyhon library for text tables.
#
# Copyright ©2023-2024 Marcin Orlowski <mail [@] MarcinOrlowski.com>
# https://github.com/MarcinOrlowski/python-flex-text-table/
#
####################################################################

import unittest

# noinspection PyPackageRequirements
from faker import Faker


class BaseTestCase(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.faker = Faker()

    # * ****************************************************************************************** *
