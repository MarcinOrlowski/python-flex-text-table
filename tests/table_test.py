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

from typing import List

from flextable.align import Align
from flextable.cell import Cell
from flextable.column import Column
from flextable.renderers.ms_dos_renderer import MsDosRenderer
from flextable.table import FlexTable
from tests.base_test_case import BaseTestCase


class TestA(BaseTestCase):

    # * ****************************************************************************************** *

    def render_table(self, table: FlexTable, echo_table: bool = False) -> List[str]:
        renderer = MsDosRenderer()
        rendered = renderer.render_as_list(table)
        if echo_table:
            print(rendered)  # noqa: WPS421
        return rendered

    # * ****************************************************************************************** *

    def test_simple_table(self) -> None:
        table = FlexTable()
        table.add_columns(
            {
                "A": "A",
                "B": "B",
                "C": "C",
            }
        )
        table.add_row(
            {
                "A": "a",
                "B": "b",
                "C": "c",
            }
        )

        rendered_table = self.render_table(table)

        expected = [
            "╔═══╦═══╦═══╗",
            "║ A ║ B ║ C ║",
            "╠═══╬═══╬═══╣",
            "║ a ║ b ║ c ║",
            "╚═══╩═══╩═══╝",
        ]

        self.assertEqual(expected, rendered_table)

        # * ****************************************************************************************** *

    def test_column_title_visibility(self) -> None:
        table = FlexTable(["ID", Column("SCORE", title_visible=False)])
        table.add_rows(
            [
                {"ID": 1, "SCORE": 12},
            ]
        )

        rendered_table = self.render_table(table)

        expected = [
            "╔════╦═══════╗",
            "║ ID ║       ║",
            "╠════╬═══════╣",
            "║ 1  ║ 12    ║",
            "╚════╩═══════╝",
        ]

        self.assertEqual(expected, rendered_table)

    # * ****************************************************************************************** *

    def test_simple_table_via_ctor(self) -> None:
        table = FlexTable(
            # columns
            {
                "A": "A",
                "B": "B",
                "C": "C",
            },
            # data rows
            [
                {
                    "A": "a",
                    "B": "b",
                    "C": "c",
                },
                ["d", "e", "f"],
            ],
        )

        rendered_table = self.render_table(table)

        expected = [
            "╔═══╦═══╦═══╗",
            "║ A ║ B ║ C ║",
            "╠═══╬═══╬═══╣",
            "║ a ║ b ║ c ║",
            "║ d ║ e ║ f ║",
            "╚═══╩═══╩═══╝",
        ]

        self.assertEqual(expected, rendered_table)

    def test_simple_table_via_ctor_list(self) -> None:
        table = FlexTable(
            {
                "A": "A",
                "B": "B",
                "C": "C",
            },
            [["d", "e", "f"]],
        )

        rendered_table = self.render_table(table)

        expected = [
            "╔═══╦═══╦═══╗",
            "║ A ║ B ║ C ║",
            "╠═══╬═══╬═══╣",
            "║ d ║ e ║ f ║",
            "╚═══╩═══╩═══╝",
        ]

        self.assertEqual(expected, rendered_table)

    def test_simple_table_via_ctor_mixed_type_dataset(self) -> None:
        table = FlexTable(
            {
                "A": "A",
                "B": "B",
                "C": "C",
            },
            [
                {
                    "A": "a",
                    "B": "b",
                    "C": "c",
                },
                ["d", "e", "f"],
            ],
        )

        rendered_table = self.render_table(table)

        expected = [
            "╔═══╦═══╦═══╗",
            "║ A ║ B ║ C ║",
            "╠═══╬═══╬═══╣",
            "║ a ║ b ║ c ║",
            "║ d ║ e ║ f ║",
            "╚═══╩═══╩═══╝",
        ]

        self.assertEqual(expected, rendered_table)

    # * ****************************************************************************************** *

    def test_multi_row_table(self):
        table = FlexTable()
        table.add_columns(
            [
                "A",
                "B",
                "C",
            ]
        )
        row_cnt = self.faker.random_int(2, 10)

        expected = [
            "╔═══╦═══╦═══╗",
            "║ A ║ B ║ C ║",
            "╠═══╬═══╬═══╣",
        ]

        for _ in range(row_cnt):
            table.add_row(
                {
                    "A": "a",
                    "B": "b",
                    "C": "c",
                }
            )
            expected.append("║ a ║ b ║ c ║")
        expected.append("╚═══╩═══╩═══╝")

        rendered_table = self.render_table(table)

        self.assertEqual(expected, rendered_table)

    # * ****************************************************************************************** *

    def test_custom_column_keys(self):
        key1 = f"key1_{self.faker.word()}"
        key2 = f"key2_{self.faker.word()}"
        key3 = f"key3_{self.faker.word()}"

        table = FlexTable()
        table.add_columns(
            {
                key1: "A",
                key2: "B",
                key3: "C",
            }
        )
        table.add_row(
            {
                key1: "a",
                key2: "b",
                key3: "c",
            }
        )

        rendered_table = self.render_table(table)

        expected = [
            "╔═══╦═══╦═══╗",
            "║ A ║ B ║ C ║",
            "╠═══╬═══╬═══╣",
            "║ a ║ b ║ c ║",
            "╚═══╩═══╩═══╝",
        ]

        self.assertEqual(expected, rendered_table)

    # * ****************************************************************************************** *

    def test_custom_index(self):
        table = FlexTable(["ID", "NAME", "SCORE"])
        table.add_rows(
            [
                {"ID": 1, "SCORE": 12, "NAME": "John"},
                {"SCORE": 15, "ID": 2, "NAME": "Mary"},
            ]
        )

        rendered_table = self.render_table(table)

        expected = [
            "╔════╦══════╦═══════╗",
            "║ ID ║ NAME ║ SCORE ║",
            "╠════╬══════╬═══════╣",
            "║ 1  ║ John ║ 12    ║",
            "║ 2  ║ Mary ║ 15    ║",
            "╚════╩══════╩═══════╝",
        ]

        self.assertEqual(expected, rendered_table)

    # * ****************************************************************************************** *

    def test_row_cells_auto_assign(self):
        table = FlexTable(["ID", "NAME", "SCORE"])
        table.add_rows(
            [
                [1, "John", 12],
            ]
        )

        rendered_table = self.render_table(table)

        expected = [
            "╔════╦══════╦═══════╗",
            "║ ID ║ NAME ║ SCORE ║",
            "╠════╬══════╬═══════╣",
            "║ 1  ║ John ║ 12    ║",
            "╚════╩══════╩═══════╝",
        ]

        self.assertEqual(expected, rendered_table)

    # * ****************************************************************************************** *

    def test_table_column_auto_key(self):
        table = FlexTable(["ID", Column("SCORE")])
        table.add_rows(
            [
                {"ID": 1, "SCORE": 12},
            ]
        )

        rendered_table = self.render_table(table)

        expected = [
            "╔════╦═══════╗",
            "║ ID ║ SCORE ║",
            "╠════╬═══════╣",
            "║ 1  ║ 12    ║",
            "╚════╩═══════╝",
        ]

        self.assertEqual(expected, rendered_table)

    # * ****************************************************************************************** *

    def test_column_align(self):
        table = FlexTable(["ID", "NAME", "SCORE"])
        table.add_rows(
            [
                {"ID": 1, "SCORE": 12, "NAME": "John"},
                {"SCORE": 15, "ID": 2, "NAME": "Tommy"},
            ]
        )

        table.set_column_align("ID", Align.RIGHT)
        table.set_column_align("SCORE", Align.RIGHT)

        rendered_table = self.render_table(table)

        expected = [
            "╔════╦═══════╦═══════╗",
            "║ ID ║ NAME  ║ SCORE ║",
            "╠════╬═══════╬═══════╣",
            "║  1 ║ John  ║    12 ║",
            "║  2 ║ Tommy ║    15 ║",
            "╚════╩═══════╩═══════╝",
        ]

        self.assertEqual(expected, rendered_table)

    # * ****************************************************************************************** *

    def test_cell_column_align(self):
        table = FlexTable(
            [
                "ID",
                Column("NAME", max_width=20),
                "SCORE",
            ]
        )
        table.add_rows(
            [
                [1, Cell("John", Align.CENTER), 12],
            ]
        )

        rendered_table = self.render_table(table)

        expected = [
            "╔════╦══════════════════════╦═══════╗",
            "║ ID ║ NAME                 ║ SCORE ║",
            "╠════╬══════════════════════╬═══════╣",
            "║ 1  ║         John         ║ 12    ║",
            "╚════╩══════════════════════╩═══════╝",
        ]

        self.assertEqual(expected, rendered_table)

    # * ****************************************************************************************** *

    def test_custom_width(self):
        table = FlexTable(["ID", "NAME", "SCORE"])
        table.add_rows(
            [
                {"ID": 1, "SCORE": 12, "NAME": "John"},
                {"SCORE": 15, "ID": 2, "NAME": "Tommy"},
            ]
        )

        table.set_column_max_width("ID", 20)
        table.set_column_max_width("NAME", 5)
        table.set_column_max_width("SCORE", 25)

        rendered_table = self.render_table(table)

        expected = [
            "╔══════════════════════╦═══════╦═══════════════════════════╗",
            "║ ID                   ║ NAME  ║ SCORE                     ║",
            "╠══════════════════════╬═══════╬═══════════════════════════╣",
            "║ 1                    ║ John  ║ 12                        ║",
            "║ 2                    ║ Tommy ║ 15                        ║",
            "╚══════════════════════╩═══════╩═══════════════════════════╝",
        ]
        assert expected == rendered_table

    # * ****************************************************************************************** *

    def test_custom_width_and_utf(self):
        table = FlexTable(["ID", "NAME", "SCORE"])
        table.add_rows(
            [
                [1, "Foo", 12],
                [2, "PBOX POH Poříčí (Restaura)", 15],
            ]
        )

        table.set_column_max_width("ID", 10)
        table.set_column_max_width("NAME", 15)
        table.set_column_max_width("SCORE", 4)

        rendered_table = self.render_table(table)

        expected = [
            "╔════════════╦═════════════════╦══════╗",
            "║ ID         ║ NAME            ║ SCO… ║",
            "╠════════════╬═════════════════╬══════╣",
            "║ 1          ║ Foo             ║ 12   ║",
            "║ 2          ║ PBOX POH Poříč… ║ 15   ║",
            "╚════════════╩═════════════════╩══════╝",
        ]
        assert expected == rendered_table

    # * ****************************************************************************************** *

    def test_custom_width_and_utf_multicolumn(self):
        table = FlexTable(
            [
                Column("NAME", max_width=25),
            ]
        )

        table.add_rows(
            [
                ["Řídící depo Praha 704"],
                ["Oční optika M. Ečerová"],
                ["AKY chovatelské potřeby a krmiva"],
            ]
        )

        rendered_table = self.render_table(table)

        expected = [
            "╔══════════════════════════════════╗",
            "║ NAME                             ║",
            "╠══════════════════════════════════╣",
            "║ Řídící depo Praha 704            ║",
            "║ Oční optika M. Ečerová           ║",
            "║ AKY chovatelské potřeby a krmiva ║",
            "╚══════════════════════════════════╝",
        ]
        assert expected == rendered_table

    def test_custom_width_and_align_narrow(self):
        table = FlexTable(["ID", "NAME", "SCORE"])
        table.add_rows(
            [
                {"ID": 1, "SCORE": 12, "NAME": "John"},
                {"SCORE": 15, "ID": 2, "NAME": "Tommy"},
            ]
        )

        table.set_column_max_width("ID", 20)
        table.set_column_max_width("NAME", 5)
        table.set_column_max_width("SCORE", 25)

        table.set_column_align("ID", Align.RIGHT)
        table.set_cell_align("NAME", Align.CENTER)
        table.get_column("SCORE").cell_align = Align.RIGHT
        table.get_column("SCORE").title_align = Align.CENTER

        rendered_table = self.render_table(table)

        expected = [
            "╔══════════════════════╦═══════╦═══════════════════════════╗",
            "║                   ID ║ NAME  ║           SCORE           ║",
            "╠══════════════════════╬═══════╬═══════════════════════════╣",
            "║                    1 ║ John  ║                        12 ║",
            "║                    2 ║ Tommy ║                        15 ║",
            "╚══════════════════════╩═══════╩═══════════════════════════╝",
        ]
        assert expected == rendered_table

    def test_custom_width_and_align_wide(self):
        table = FlexTable(["ID", "NAME", "SCORE"])
        table.add_rows(
            [
                {"ID": 1, "SCORE": 12, "NAME": "John"},
                {"SCORE": 15, "ID": 2, "NAME": "Tommy"},
            ]
        )

        table.set_column_max_width("ID", 20)
        table.set_column_max_width("NAME", 10)
        table.set_column_max_width("SCORE", 25)

        table.set_column_align("ID", Align.RIGHT)
        table.set_cell_align("NAME", Align.CENTER)
        table.get_column("SCORE").cell_align = Align.RIGHT
        table.get_column("SCORE").title_align = Align.CENTER

        rendered_table = self.render_table(table)

        expected = [
            "╔══════════════════════╦════════════╦═══════════════════════════╗",
            "║                   ID ║    NAME    ║           SCORE           ║",
            "╠══════════════════════╬════════════╬═══════════════════════════╣",
            "║                    1 ║    John    ║                        12 ║",
            "║                    2 ║   Tommy    ║                        15 ║",
            "╚══════════════════════╩════════════╩═══════════════════════════╝",
        ]
        assert expected == rendered_table

    def test_custom_width_and_mixed_align(self):
        table = FlexTable(["ID", "NAME", "SCORE"])
        table.add_rows(
            [
                {"ID": 1, "SCORE": Cell(12, Align.CENTER), "NAME": "John"},
                {"SCORE": 15, "ID": 2, "NAME": "Tommy"},
            ]
        )

        table.set_column_max_width("ID", 10)
        table.set_column_max_width("NAME", 5)
        table.set_column_max_width("SCORE", 25)

        table.set_column_align("ID", Align.RIGHT)
        table.set_cell_align("NAME", Align.CENTER)
        table.get_column("SCORE").cell_align = Align.RIGHT
        table.title_align = Align.CENTER

        rendered_table = self.render_table(table)

        expected = [
            "╔════════════╦═══════╦═══════════════════════════╗",
            "║         ID ║ NAME  ║ SCORE                     ║",
            "╠════════════╬═══════╬═══════════════════════════╣",
            "║          1 ║ John  ║             12            ║",
            "║          2 ║ Tommy ║                        15 ║",
            "╚════════════╩═══════╩═══════════════════════════╝",
        ]
        assert expected == rendered_table

    def test_custom_width_clipping(self):
        max_length = self.faker.random_int(10, 20)
        long_name = self.faker.sentence(nb_words=max_length)

        clipped = long_name[: max_length - 1] + "…"

        key = "NAME"
        table = FlexTable([key])
        table.add_rows(
            [
                {
                    key: long_name,
                },
            ]
        )

        table.set_column_max_width("NAME", max_length)

        rendered_table = self.render_table(table)

        expected = [
            "╔═{0}═╗".format("═" * max_length),
            "║ {0} ║".format(key + (" " * (max_length - len(key)))),
            "╠═{0}═╣".format("═" * max_length),
            "║ {0} ║".format(clipped),
            "╚═{0}═╝".format("═" * max_length),
        ]
        assert expected == rendered_table

    # * ****************************************************************************************** *

    def test_no_data_label(self):
        table = FlexTable(["ID", Column("SCORE")])
        table.set_no_data_label("FOO BAR")

        rendered_table = self.render_table(table)

        expected = [
            "╔════╦═══════╗",
            "║ ID ║ SCORE ║",
            "╠════╬═══════╣",
            "║  FOO BAR   ║",
            "╚════╩═══════╝",
        ]

        self.assertEqual(expected, rendered_table)

    def test_custom_no_data_label(self):
        table = FlexTable(["ID", Column("SCORE")])
        table.set_no_data_label("FOO BAR")

        rendered_table = self.render_table(table)

        expected = [
            "╔════╦═══════╗",
            "║ ID ║ SCORE ║",
            "╠════╬═══════╣",
            "║  FOO BAR   ║",
            "╚════╩═══════╝",
        ]

        self.assertEqual(expected, rendered_table)

    # * ****************************************************************************************** *

    def test_separator(self):
        table = FlexTable(["ID", Column("SCORE")])
        table.add_row(
            [
                "10",
                "123",
            ]
        )
        table.add_separator()
        table.add_row(
            [
                "31",
                "5875",
            ]
        )

        rendered_table = self.render_table(table)

        expected = [
            "╔════╦═══════╗",
            "║ ID ║ SCORE ║",
            "╠════╬═══════╣",
            "║ 10 ║ 123   ║",
            "╠════╬═══════╣",
            "║ 31 ║ 5875  ║",
            "╚════╩═══════╝",
        ]

        self.assertEqual(expected, rendered_table)

    # * ****************************************************************************************** *

    def test_too_narow_empty_table(self) -> None:
        """
        Ensures narrow table with no data is correctly extended to fit "NO DATA" message
        """
        table = FlexTable(["ID", "NAME"])
        table.set_no_data_label("NO DATA LONG MESSAGE")

        rendered_table = self.render_table(table)

        expected = [
            "╔════╦═════════════════╗",
            "║ ID ║ NAME            ║",
            "╠════╬═════════════════╣",
            "║ NO DATA LONG MESSAGE ║",
            "╚════╩═════════════════╝",
        ]

        self.assertEqual(expected, rendered_table)
