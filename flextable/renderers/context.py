####################################################################################################
#
# █▀▀▀ ▀█                ▀▀█▀▀            █       ▀▀█▀▀      █    ▀█
# █▀▀   █  ▄▀▀▄ █  █       █   ▄▀▀▄ █  █ ▀█▀        █   ▄▀▀▄ █▀▀▄  █  ▄▀▀▄
# █     █  █▀▀  ▄▀▀▄       █   █▀▀  ▄▀▀▄  █         █    ▄▄█ █  █  █  █▀▀
# █    ▄█▄ ▀▄▄▀ █  █       █   ▀▄▄▀ █  █  ▀▄▀       █   ▀▄▄▀ █▄▄▀ ▄█▄ ▀▄▄▀
#
# Fast and flexible Pyhon library for text tables.
#
# Copyright ©2023-2025 Marcin Orlowski <mail [@] MarcinOrlowski.com>
# https://github.com/MarcinOrlowski/python-flex-text-table/
#
####################################################################################################

from typing import Union


class RendererContext(object):
    """
    A context object that provides information about the state of the table renderer.

    Attributes:
        table (FlexTable): The table being rendered.
    """

    def __init__(self, table: "FlexTable"):
        """
        Constructs a new RendererContext object.

        Args:
            table: The table being rendered.
        """
        self.table = table
        self._table_row_idx = 0
        self._rendered_row_idx = 0

    # * ****************************************************************************************** *

    @property
    def table_row_idx(self) -> int:
        """
        Gets the index of the current row in the table.

        Returns:
            The index of the current row in the table.
        """
        return self._table_row_idx

    def inc_table_row_idx(self) -> "RendererContext":
        """
        Increments the index of the current row in the table.

        Returns:
            The current RendererContext object.
        """
        self._table_row_idx += 1
        return self

    # * ****************************************************************************************** *

    @property
    def rendered_row_idx(self) -> int:
        """
        Gets the index of the current row being rendered.

        Returns:
            The index of the current row being rendered.
        """
        return self._rendered_row_idx

    def inc_rendered_row_idx(self) -> "RendererContext":
        """
        Increments the index of the current row being rendered.

        Returns:
            The current RendererContext object.
        """
        self._rendered_row_idx += 1
        return self

    # * ****************************************************************************************** *

    def is_first_visible_column(self, column_key: Union[str, int]) -> bool:
        """
        Returns whether the specified column is the first visible column in the table.

        Args:
            column_key: The key of the column to check.

        Returns:
            True if the specified column is the first visible column in the table, otherwise False.
        """
        for key, column in self.table.columns.items():
            if column.visible:
                return key == column_key
        return False

    def is_last_visible_column(self, column_key: Union[str, int]) -> bool:
        """
        Returns whether the specified column is the last visible column in the table.

        Args:
            column_key: The key of the column to check.

        Returns:
            True if the specified column is the last visible column in the table, otherwise False.
        """
        last_visible_column_key = None
        for key, column in self.table.columns.items():
            if not column.visible:
                continue
            last_visible_column_key = key
        return last_visible_column_key == column_key

    def is_first_visible_row(self) -> bool:
        """
        Returns whether the current row being rendered is the first visible row in the table.

        Returns:
            True if the current row being rendered is the first visible row in the table,
            otherwise False.
        """
        return self.rendered_row_idx == 0

    def is_last_visible_row(self) -> bool:
        """
        Returns whether the current row being rendered is the last visible row in the table.

        Returns:
            True if the current row being rendered is the last visible row in the table,
            otherwise False.
        """
        return self.table_row_idx == self.table.row_count
