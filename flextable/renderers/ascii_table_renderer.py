####################################################################################################
#
# Flex Text Table
# Fast and flexible Pyhon library for text tables.
#
# Copyright ©2023-2024 Marcin Orlowski <mail [@] MarcinOrlowski.com>
# https://github.com/MarcinOrlowski/python-flex-text-table/
#
####################################################################################################

from abc import ABC
from typing import List, Union, Optional

from flextable.align import Align
from flextable.cell import Cell
from flextable.separator import Separator
from flextable.columns_container import ColumnsContainer
from flextable.exceptions import NoVisibleColumnsError
from flextable.renderers.context import RendererContext
from flextable.renderers.contracts import RendererContract
from flextable.row import Row


class AsciiTableRenderer(RendererContract, ABC):
    """Abstract base class for all ASCII table renderers."""

    def render_as_list(self, table: 'FlexTable') -> List:
        """
        Renders the FlexTable object as a list of strings with separators, header, and data rows.
        If there are no visible columns, it raises a NoVisibleColumnsError. The result variable
        holds the list of rendered rows, which are returned at the end of the function.

        :param 'FlexTable' table: Table to render
        :return: List of strin representation of table rows.
        """
        ctx = RendererContext(table)

        if ctx.table.visible_column_count == 0:
            raise NoVisibleColumnsError()

        result = [
            self.render_top_separator(ctx),
            self.render_header(ctx),
            self.render_separator(ctx),
        ]

        if table.row_count > 0:
            for row in table.rows.values():
                if isinstance(row, Separator):
                    result.append(self.render_separator(ctx))
                else:
                    result.append(self.render_data_row(ctx, row))
                ctx.inc_rendered_row_idx()
                ctx.inc_table_row_idx()
        else:
            result.append(self.render_no_data_row(ctx, table.get_no_data_label()))
            ctx.inc_rendered_row_idx()

        result.append(self.render_bottom_separator(ctx))
        ctx.inc_rendered_row_idx()

        return result

    # * ****************************************************************************************** *

    ROW_FRAME_LEFT: str = '?'
    ROW_FRAME_CENTER: str = '?'
    ROW_FRAME_RIGHT: str = '?'

    def render_no_data_row(self, ctx: RendererContext, label: str = 'NO DATA') -> str:
        """
        Renders a row of text that indicates that there are no data rows available for rendering.
        The label string "NO DATA" is centered and surrounded by the row frame characters, which
        are defined as constants in the class. The resulting string is returned.

        :param RendererContext ctx: Rendering context that holds information about the current
                                    rendering process.
        :param str label: Label to render.
        :return: List of string representation of table without data rows.
        """
        total_table_width = self.get_table_total_width(ctx.table)
        if len(label) > total_table_width:
            label = label[:total_table_width - 3] + '…'
        else:
            label = label.center(total_table_width)

        return f'{self.ROW_FRAME_LEFT}{label}{self.ROW_FRAME_RIGHT}'

    # * ****************************************************************************************** *

    def render_data_row(self, ctx: RendererContext, row: Row) -> str:
        """
        Renders a data row by iterating over the columns and their corresponding cells. For each
        visible column, it retrieves the corresponding cell from the row and pads its value to fit
        the column width. It also applies the cell alignment to the padded value before appending
        it. The resulting string is then returned.

        :param RendererContext ctx: Rendering context that holds information about the current
                                    rendering process.
        :param Row row: Row to render.
        :return: A string representing the row data..
        """
        result = ''

        columns = ctx.table.columns
        cells = row.container
        for column_key, column in columns.items():
            if not column.visible:
                continue

            if column_key in cells:
                cell = cells.get_cell(column_key)
            else:
                cell = Cell()

            if ctx.is_first_visible_column(column_key):
                result += self.ROW_FRAME_LEFT

            # Using default column align
            if cell.align == Align.AUTO:
                align = self.get_column_align(columns, column_key)
            else:
                align = cell.align

            result += self.pad(columns, column_key, cell.value, align)

            result += self.ROW_FRAME_RIGHT if ctx.is_last_visible_column(
                column_key) else self.ROW_FRAME_CENTER

        return result

    # * ****************************************************************************************** *

    def render_header(self, ctx: RendererContext) -> str:
        """
        Renders the table header by iterating over the columns, and for each visible column,
        it appends the corresponding column title to the resulting string. It also applies the
        title alignment to each column's title before appending it.

        :param RendererContext ctx: Rendering context that holds information about the current
                                    rendering process.
        :return: A string representing the table header.
        """
        columns = ctx.table.columns

        result = ''
        for column_key, column in columns.items():
            if not column.visible:
                continue

            if ctx.is_first_visible_column(column_key):
                result += self.ROW_FRAME_LEFT

            title = column.title if column.title_visible else ''
            result += self.pad(columns, column_key, title, column.title_align)
            result += self.ROW_FRAME_RIGHT if ctx.is_last_visible_column(
                column_key) else self.ROW_FRAME_CENTER

        ctx.inc_rendered_row_idx()

        return result

    # * ****************************************************************************************** *

    SEGMENT_ROW_FILL: str = '?'
    SEGMENT_FIRST_ROW_LEFT: str = '?'
    SEGMENT_FIRST_ROW_CENTER: str = '?'
    SEGMENT_FIRST_ROW_RIGHT: str = '?'
    SEGMENT_ROW_LEFT: str = '?'
    SEGMENT_ROW_CENTER: str = '?'
    SEGMENT_ROW_RIGHT: str = '?'
    SEGMENT_LAST_ROW_LEFT: str = '?'
    SEGMENT_LAST_ROW_CENTER: str = '?'
    SEGMENT_LAST_ROW_RIGHT: str = '?'

    def render_bottom_separator(self, ctx: RendererContext) -> str:
        """
        Renders the bottom separator row of the table, consisting of the segment characters for the
        bottom edges of the table.

        :param RendererContext ctx: Rendering context that holds information about the current
                                    rendering process.
        :return: A string representing the bottom separator row of the table.
        """
        result = self.SEGMENT_LAST_ROW_LEFT
        for column_key, column in ctx.table.columns.items():
            if not column.visible:
                continue

            result += self.SEGMENT_ROW_FILL * column.width
            if ctx.is_last_visible_column(column_key):
                result += self.SEGMENT_LAST_ROW_RIGHT
            else:
                result += self.SEGMENT_LAST_ROW_CENTER

        return result

    def render_top_separator(self, ctx: RendererContext) -> str:
        """
        Renders the top separator row of the table, consisting of the segment characters for the top
        edges of the table.

        :param RendererContext ctx: Rendering context that holds information about the current
                                    rendering process.
        :return: A string representing the top separator row of the table.
        """
        result = self.SEGMENT_FIRST_ROW_LEFT
        for column_key, column in ctx.table.columns.items():
            if not column.visible:
                continue

            result += self.SEGMENT_ROW_FILL * column.width
            if ctx.is_last_visible_column(column_key):
                result += self.SEGMENT_FIRST_ROW_RIGHT
            else:
                result += self.SEGMENT_FIRST_ROW_CENTER

        ctx.inc_rendered_row_idx()

        return result

    def render_separator(self, ctx: RendererContext) -> str:
        """
        Renders a separator row that visually separates the header row from the data rows or two
        data rows in the table. The separator row consists of horizontal lines (e.g., dashes)
        and corner/intersection characters.

        :param RendererContext ctx: Rendering context that holds information about the current
                                    rendering process.

        :return: A string representing the separator row.
        """
        columns = ctx.table.columns
        result = ''

        # check if table is empty (otherwise is_last_visible_row() will return true as row 0 is the
        # last of 0 row dataset, rendering last closing table row characters instead of first
        # row characters) which is visible for any non-symetric blocks (i.e. MsDos style blocks)
        if ctx.table.row_count > 0:
            if ctx.is_last_visible_row():
                is_first_row = False
                is_last_row = True
            elif ctx.is_first_visible_row():
                is_first_row = True
                is_last_row = False
            else:
                is_first_row = False
                is_last_row = False
        else:
            is_first_row = False
            is_last_row = False

        for column_key, column in columns.items():
            if not column.visible:
                continue

            if is_first_row:
                segment = self.SEGMENT_FIRST_ROW_LEFT
            elif is_last_row:
                segment = self.SEGMENT_LAST_ROW_LEFT
            else:
                segment = self.SEGMENT_ROW_LEFT

            if ctx.is_first_visible_column(column_key):
                result += segment

            result += self.SEGMENT_ROW_FILL * column.width

            if ctx.is_last_visible_column(column_key):
                if is_first_row:
                    segment = self.SEGMENT_FIRST_ROW_RIGHT
                elif is_last_row:
                    segment = self.SEGMENT_LAST_ROW_RIGHT
                else:
                    segment = self.SEGMENT_ROW_RIGHT
            else:
                if is_first_row:
                    segment = self.SEGMENT_FIRST_ROW_CENTER
                elif is_last_row:
                    segment = self.SEGMENT_LAST_ROW_CENTER
                else:
                    segment = self.SEGMENT_ROW_CENTER

            result += segment

        ctx.inc_rendered_row_idx()

        return result

    # * ****************************************************************************************** *

    def pad(self, columns: ColumnsContainer, column_key: Union[str, int], value: str,
            align: Optional[Align] = None) -> str:
        """
        Pads given $value to fit column allowed width. If `$value` exceeded max allowed width, it
        will be truncated to fit. Returns aligned string.

        :param ColumnsContainer columns: Table column definition container.
        :param str|int column_key: Column key we are going to populate.
        :param str value: Value to pad
        :param Optional[Align] align: Requested text alignment. If None, column's alignment is used.
        """
        align = self.get_column_align(columns, column_key) if align is None else align
        max_width = self.get_column_width(columns, column_key)

        str_len = len(value)
        if str_len > max_width:
            value = value[:max_width - 1] + '…'

        if align in {Align.LEFT, Align.AUTO}:
            result = value.ljust(max_width)
        elif align == Align.RIGHT:
            result = value.rjust(max_width)
        elif align == Align.CENTER:
            # Can't use center() directly, as it seems to lean towards adding more paddings on the
            # left side of the string, which in case of odd padding characters, makes it look oddly
            # aligned.
            # TODO: this should depend on locale to support RTL langs (if anyone misses that now).
            if max_width - len(value) == 1:
                value = f'{value} '  # Mind trailing space!
            result = value.center(max_width)
        else:
            raise ValueError(f'Unsupported align: {align}')

        return result

    # * ****************************************************************************************** *

    def get_column_width(self, columns: ColumnsContainer, column_key: Union[str, int]) -> int:
        return columns[column_key].max_width

    def get_column_align(self, columns: ColumnsContainer, column_key: Union[str, int]) -> Align:
        return columns[column_key].cell_align

    def get_column_title_align(self, columns: ColumnsContainer,
                               column_key: Union[str, int]) -> Align:
        return columns[column_key].title_align

    # * ****************************************************************************************** *

    def get_table_total_width(self, table: 'FlexTable') -> int:
        """
        Calculates the total width of the table, including the visible columns' widths and the width
        of the separator characters between them.

        :param FlexTable table: The table for which the total width will be calculated.
        :return: An integer representing the total width of the table.
        """
        total_width = sum(column.width for column in table.columns.values() if column.visible)
        total_width += (table.visible_column_count - 1) * len(self.SEGMENT_ROW_CENTER)
        return total_width
