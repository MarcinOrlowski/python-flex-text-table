####################################################################################################
#
# Flex Text Table
# Fast and flexible Pyhon library for text tables.
#
# Copyright ©2023-2024 Marcin Orlowski <mail [@] MarcinOrlowski.com>
# https://github.com/MarcinOrlowski/python-flex-text-table/
#
####################################################################################################

from typing import Dict, Union

from flextable.base_container import BaseContainer
from flextable.row import Row


class RowsContainer(BaseContainer[Row]):
    def __init__(self, items: Dict[Union[str, int], Row] = None):
        super().__init__(items, Row)
