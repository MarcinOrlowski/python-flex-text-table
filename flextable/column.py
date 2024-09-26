####################################################################################################
#
# Flex Text Table
# Fast and flexible Pyhon library for text tables.
#
# Copyright ©2023 Marcin Orlowski <mail [@] MarcinOrlowski.com>
# https://github.com/MarcinOrlowski/python-flex-text-table/
#
####################################################################################################

from typing import Optional

from flextable.align import Align


class Column(object):
    """
    The Column class represents a single column within a table. It stores the column's title,
    alignment properties (for the title and cells), maximum width, visibility, and other related
    attributes. It also provides getter and setter methods for each attribute, along with a method
    to update the maximum width.
    """

    # * ****************************************************************************************** *

    def __init__(self, title: str,
                 align: Align = Align.AUTO,
                 max_width: int = 0,
                 cell_align: Optional[Align] = None,
                 title_align: Optional[Align] = None,
                 visible: bool = True,
                 title_visible: bool = True):
        self._title: str = title
        self._max_width: int = max_width

        self.align: Align = align
        self._cell_align: Align = cell_align if cell_align is not None else Align.AUTO
        self._title_align: Align = title_align if title_align is not None else Align.AUTO

        self._visible: bool = visible
        self._title_visible: bool = title_visible

    # * ****************************************************************************************** *

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        self._title = value

    # * ****************************************************************************************** *

    @property
    def align(self) -> Align:
        raise RuntimeError('This is not a real property. Query title or cell align instead.')

    @align.setter
    def align(self, value: Align) -> None:
        self.title_align = value
        self.cell_align = value

    # * ****************************************************************************************** *

    @property
    def title_align(self) -> Align:
        return self._title_align

    @title_align.setter
    def title_align(self, value: Align) -> None:
        self._title_align = value

    # * ****************************************************************************************** *

    @property
    def cell_align(self) -> Align:
        return self._cell_align

    @cell_align.setter
    def cell_align(self, value: Align) -> None:
        self._cell_align = value

    # * ****************************************************************************************** *

    @property
    def max_width(self) -> int:
        return self._max_width

    @max_width.setter
    def max_width(self, value: int) -> None:
        self._max_width = value

    @property
    def width(self) -> int:
        return self.max_width

    def update_max_width(self, width: int) -> None:
        if width > self.max_width:
            self.max_width = width

    # * ****************************************************************************************** *

    @property
    def visible(self) -> bool:
        return self._visible

    @visible.setter
    def visible(self, value: bool) -> None:
        self._visible = value

    @property
    def title_visible(self) -> bool:
        return self._title_visible

    @title_visible.setter
    def title_visible(self, value: bool) -> None:
        self._title_visible = value
