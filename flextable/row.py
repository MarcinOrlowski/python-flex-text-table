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

from typing import Optional, Union, Dict

from flextable.align import Align
from flextable.cell import Cell
from flextable.cells_container import CellsContainer


class Row(object):
    def __init__(self, cells: Optional[Dict] = None):
        self.container = CellsContainer()

        if cells is not None:
            self.add_cells(cells)

    def __len__(self):
        """Returns number of elements in container."""
        return len(self.container)

    # * ****************************************************************************************** *

    _container: CellsContainer

    @property
    def container(self) -> CellsContainer:
        return self._container

    @container.setter
    def container(self, value: CellsContainer) -> None:
        if not isinstance(value, CellsContainer):
            raise TypeError(f"container must be CellsContainer, {type(value)} given.")
        self._container = value

    def add_cell(
        self,
        column_key: Union[str, int],
        cell: Union[Cell, str, float, int],
        align: Align = Align.AUTO,
    ) -> "Row":
        if not isinstance(cell, Cell):
            cell = Cell(cell, align)
        self.container.add_cell(column_key, cell)

        return self

    def add_cells(self, cells: Dict) -> "Row":
        if not isinstance(cells, Dict):
            raise TypeError(f"The cells must be Dict, {type(cells)} given.")

        for column_key, cell in cells.items():
            self.add_cell(column_key, cell)

        return self

    # * ****************************************************************************************** *

    def items(self) -> Dict:
        return self.container.items()

    def visible_items(self):
        return {key: cell for key, cell in self.container.items() if cell.visible}

    # * ****************************************************************************************** *
