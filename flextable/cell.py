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

from typing import Union, Optional

from flextable.align import Align


class Cell(object):
    """
    This class represents a table cell in a text-based table layout. It stores the cell's content,
    which can be of various data types (string, integer, float, or boolean), and its alignment.
    The alignment can be set automatically or explicitly specified using the `Align` enumeration.
    The `Cell` class provides properties and setters to access and modify the cell's value and
    alignment.
    """

    def __init__(
        self,
        value: Optional[Union[str, int, float, bool]] = "",
        align: Align = Align.AUTO,
    ):
        self.value: Optional[Union[str, int, float, bool]] = value
        self.align: Align = align

    # * ****************************************************************************************** *

    @property
    def value(self) -> Optional[Union[str, int, float, bool]]:
        return self._value

    @value.setter
    def value(self, value: Optional[Union[str, int, float, bool]]) -> None:
        if value is None:
            value = "NONE"
        elif isinstance(value, bool):
            value = str(value).upper()
        else:
            value = str(value)

        self._value = value

    # * ****************************************************************************************** *

    @property
    def align(self) -> Align:
        return self._align

    @align.setter
    def align(self, align: Align) -> None:
        self._align = align
