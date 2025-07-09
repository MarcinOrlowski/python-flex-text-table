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

from typing import Final

from flextable.renderers.ascii_table_renderer import AsciiTableRenderer


class PlusMinusRenderer(AsciiTableRenderer):
    ROW_FRAME_LEFT: Final[str] = "| "
    ROW_FRAME_CENTER: Final[str] = " | "
    ROW_FRAME_RIGHT: Final[str] = " |"

    SEGMENT_ROW_FILL: Final[str] = "-"
    SEGMENT_FIRST_ROW_LEFT: Final[str] = "+-"
    SEGMENT_FIRST_ROW_CENTER: Final[str] = "-+-"
    SEGMENT_FIRST_ROW_RIGHT: Final[str] = "-+"
    SEGMENT_ROW_LEFT: Final[str] = "+-"
    SEGMENT_ROW_CENTER: Final[str] = "-+-"
    SEGMENT_ROW_RIGHT: Final[str] = "-+"
    SEGMENT_LAST_ROW_LEFT: Final[str] = "+-"
    SEGMENT_LAST_ROW_CENTER: Final[str] = "-+-"
    SEGMENT_LAST_ROW_RIGHT: Final[str] = "-+"
