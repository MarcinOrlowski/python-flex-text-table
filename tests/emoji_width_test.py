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

from wcwidth import wcswidth

from flextable.align import Align
from flextable.renderers.fancy_renderer import FancyRenderer
from flextable.table import FlexTable
from tests.base_test_case import BaseTestCase


class EmojiWidthTest(BaseTestCase):
    """
    Regression tests for ticket #4: cell width must be measured in terminal
    columns (display width), not Python `len()`. Emoji like 🟢 occupy two
    columns but len() == 1; CJK ideographs like 漢 also occupy two columns.
    """

    def assert_lines_equal_width(self, lines):
        widths = [wcswidth(line) for line in lines]
        self.assertNotIn(-1, widths, f"wcswidth could not measure: {lines}")
        self.assertEqual(
            1,
            len(set(widths)),
            f"rendered lines do not have equal display width: {list(zip(widths, lines))}",
        )

    def test_emoji_in_first_column_aligns_borders(self) -> None:
        # GIVEN a table mirroring the example from ticket #4.
        table = FlexTable(["", "Day", "Type"])
        table.add_row(["🟢", "Mon", "Wejscie"])
        table.add_row(["🔴", "Tue", "Wyjscie"])
        table.add_row(["", "Wed", "???"])

        # WHEN
        rendered = table.render(renderer=FancyRenderer()).splitlines()

        # THEN every line is the same number of terminal columns wide.
        self.assert_lines_equal_width(rendered)

        expected = [
            "┌────┬─────┬─────────┐",
            "│    │ Day │ Type    │",
            "├────┼─────┼─────────┤",
            "│ 🟢 │ Mon │ Wejscie │",
            "│ 🔴 │ Tue │ Wyjscie │",
            "│    │ Wed │ ???     │",
            "└────┴─────┴─────────┘",
        ]
        self.assertEqual(expected, rendered)

    def test_emoji_only_column_width(self) -> None:
        table = FlexTable(["Status"])
        table.add_row(["🟢"])
        table.add_row(["🔴"])
        table.add_row(["ok"])

        rendered = table.render(renderer=FancyRenderer()).splitlines()

        self.assert_lines_equal_width(rendered)
        expected = [
            "┌────────┐",
            "│ Status │",
            "├────────┤",
            "│ 🟢     │",
            "│ 🔴     │",
            "│ ok     │",
            "└────────┘",
        ]
        self.assertEqual(expected, rendered)

    def test_cjk_ideographs(self) -> None:
        table = FlexTable(["Name", "Lang"])
        table.add_row(["漢字", "JP"])
        table.add_row(["ascii", "EN"])

        rendered = table.render(renderer=FancyRenderer()).splitlines()

        self.assert_lines_equal_width(rendered)
        expected = [
            "┌───────┬──────┐",
            "│ Name  │ Lang │",
            "├───────┼──────┤",
            "│ 漢字  │ JP   │",
            "│ ascii │ EN   │",
            "└───────┴──────┘",
        ]
        self.assertEqual(expected, rendered)

    def test_emoji_truncation_uses_display_width(self) -> None:
        # GIVEN a column whose max_width is hard-capped narrower than the data.
        table = FlexTable(["Status"])
        table.add_row(["🟢🟢🟢"])
        table.set_column_max_width("Status", 4)

        # WHEN
        rendered = table.render(renderer=FancyRenderer()).splitlines()

        # THEN the body row must be exactly as wide as the borders.
        self.assert_lines_equal_width(rendered)

    def test_right_align_with_emoji(self) -> None:
        table = FlexTable(["Tag", "Count"])
        table.set_column_align("Tag", Align.RIGHT)
        table.add_row(["🟢", 1])
        table.add_row(["ok", 2])

        rendered = table.render(renderer=FancyRenderer()).splitlines()

        self.assert_lines_equal_width(rendered)

    def test_center_align_with_emoji(self) -> None:
        table = FlexTable(["Status"])
        table.set_column_align("Status", Align.CENTER)
        table.add_row(["🟢"])
        table.add_row(["running"])

        rendered = table.render(renderer=FancyRenderer()).splitlines()

        self.assert_lines_equal_width(rendered)

    def test_emoji_wider_than_header(self) -> None:
        # Header is 1 char wide; the emoji body cell is 2 cols wide and must
        # widen the column.
        table = FlexTable(["s"])
        table.add_row(["🟢"])

        rendered = table.render(renderer=FancyRenderer()).splitlines()

        self.assert_lines_equal_width(rendered)
        expected = [
            "┌────┐",
            "│ s  │",
            "├────┤",
            "│ 🟢 │",
            "└────┘",
        ]
        self.assertEqual(expected, rendered)
