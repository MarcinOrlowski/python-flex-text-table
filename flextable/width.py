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

from wcwidth import wcswidth, wcwidth

from flextable.align import Align


def display_width(value: str) -> int:
    """
    Returns the number of terminal columns occupied by `value`.

    Falls back to character count if wcswidth cannot measure the string
    (it returns -1 for control characters and a few unassigned code points).
    """
    width = wcswidth(value)
    if width < 0:
        return len(value)
    return width


def truncate_to_width(value: str, max_width: int, ellipsis: str = "…") -> str:
    """
    Truncates `value` so it fits within `max_width` terminal columns, appending
    `ellipsis` when truncation occurs. Width is measured by display_width(),
    not len(), so emoji and CJK characters are accounted for correctly.
    """
    if display_width(value) <= max_width:
        return value

    ellipsis_w = display_width(ellipsis)
    budget = max_width - ellipsis_w
    if budget <= 0:
        return ellipsis[:max_width]

    out = ""
    used = 0
    for char in value:
        char_w = wcwidth(char)
        if char_w < 0:
            char_w = 1
        if used + char_w > budget:
            break
        out += char
        used += char_w
    return out + ellipsis


def pad_to_width(value: str, width: int, align: Align) -> str:
    """
    Pads `value` with spaces so it occupies exactly `width` terminal columns.
    Truncates with an ellipsis if `value` is too wide for the column.
    """
    value = truncate_to_width(value, width)
    deficit = width - display_width(value)
    if deficit <= 0:
        return value

    if align in {Align.LEFT, Align.AUTO}:
        return value + " " * deficit
    if align == Align.RIGHT:
        return " " * deficit + value
    if align == Align.CENTER:
        # Match the prior renderer's CENTER bias exactly: when deficit is 1
        # the lone padding space goes on the right; otherwise mirror Python's
        # str.center bias rule (CPython: marg//2 + (marg & width & 1)).
        if deficit == 1:
            left, right = 0, 1
        else:
            left = deficit // 2 + (deficit & width & 1)
            right = deficit - left
        return " " * left + value + " " * right
    raise ValueError(f"Unsupported align: {align}")
