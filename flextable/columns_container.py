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
from flextable.column import Column
from flextable.exceptions import DuplicateColumnKeyError


class ColumnsContainer(BaseContainer[Column]):
    def __init__(self, items: Dict[Union[str, int], Column] = None):
        super().__init__(items, Column)

    # Implement the __setitem__ method to set items using keys
    def __setitem__(self, column_key: str, column: Column) -> None:
        """
        Sets the item in the container using the given column_key and column. Raises an error if the
        column_key is a duplicate or if the column is not an instance of the Column class.

        :param column_key: The key to be used for the column.
        :param column: The Column instance to be added to the container.
        """
        if column_key in self:
            raise DuplicateColumnKeyError.for_column_key(column_key)
        if not isinstance(column, Column):
            raise TypeError(f'column_val must be Column, {type(column)} given.')

        self._container[column_key] = column

        self._container[column_key].update_max_width(len(column.title))

    # Implement the __getitem__ method to access items using keys
    def __getitem__(self, key: Union[str, int]) -> Column:
        """
        Retrieves the item in the container using the given key. Supports indexing by key (str) or
        by index (int).

        :param key: The key or index to be used to access the column.
        :return: The Column instance corresponding to the given key or index.
        """
        # if it's int then it is INDEX not a key!
        if isinstance(key, int):
            keys = list(self._container.keys())
            return self._container[keys[key]]

        return self._container[key]

    # * ****************************************************************************************** *

    def get_key_by_index(self, index: int) -> str:
        """
        Retrieves the key corresponding to the given index.

        :param index: The index to be used to access the key.
        :return: The key corresponding to the given index.
        """
        return list(self.container.keys())[index]

    def keys(self):
        """
        Returns the keys of the container.

        :return: An iterable view of the container's keys.
        """
        return self.container.keys()

    def visible_items(self) -> Dict[str, Column]:
        """
        Retrieves the visible items in the container.

        :return: A dictionary containing the visible key-column pairs in the container.
        """
        return {key: column for key, column in self.container.items() if column.visible}
