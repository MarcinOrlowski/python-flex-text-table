####################################################################
#
# Flex Text Table
# Fast and flexible Pyhon library for text tables.
#
# Copyright ©2023-2024 Marcin Orlowski <mail [@] MarcinOrlowski.com>
# https://github.com/MarcinOrlowski/python-flex-text-table/
#
####################################################################
from flextable.renderers.fancy_renderer import FancyRenderer
from flextable.renderers.ms_dos_renderer import MsDosRenderer
from flextable.renderers.plus_minus_renderer import PlusMinusRenderer
from tests.base_test_case import BaseTestCase


class RendererTest(BaseTestCase):

    def test_ascii_renderer_charset(self) -> None:
        self.assertEqual('| ', PlusMinusRenderer.ROW_FRAME_LEFT)
        self.assertEqual(' | ', PlusMinusRenderer.ROW_FRAME_CENTER)
        self.assertEqual(' |', PlusMinusRenderer.ROW_FRAME_RIGHT)
        self.assertEqual('-', PlusMinusRenderer.SEGMENT_ROW_FILL)
        self.assertEqual('+-', PlusMinusRenderer.SEGMENT_FIRST_ROW_LEFT)
        self.assertEqual('-+-', PlusMinusRenderer.SEGMENT_FIRST_ROW_CENTER)
        self.assertEqual('-+', PlusMinusRenderer.SEGMENT_FIRST_ROW_RIGHT)
        self.assertEqual('+-', PlusMinusRenderer.SEGMENT_ROW_LEFT)
        self.assertEqual('-+-', PlusMinusRenderer.SEGMENT_ROW_CENTER)
        self.assertEqual('-+', PlusMinusRenderer.SEGMENT_ROW_RIGHT)
        self.assertEqual('+-', PlusMinusRenderer.SEGMENT_LAST_ROW_LEFT)
        self.assertEqual('-+-', PlusMinusRenderer.SEGMENT_LAST_ROW_CENTER)
        self.assertEqual('-+', PlusMinusRenderer.SEGMENT_LAST_ROW_RIGHT)

    def test_ms_dos_renderer_charset(self) -> None:
        self.assertEqual('║ ', MsDosRenderer.ROW_FRAME_LEFT)
        self.assertEqual(' ║ ', MsDosRenderer.ROW_FRAME_CENTER)
        self.assertEqual(' ║', MsDosRenderer.ROW_FRAME_RIGHT)
        self.assertEqual('═', MsDosRenderer.SEGMENT_ROW_FILL)
        self.assertEqual('╔═', MsDosRenderer.SEGMENT_FIRST_ROW_LEFT)
        self.assertEqual('═╦═', MsDosRenderer.SEGMENT_FIRST_ROW_CENTER)
        self.assertEqual('═╗', MsDosRenderer.SEGMENT_FIRST_ROW_RIGHT)
        self.assertEqual('╠═', MsDosRenderer.SEGMENT_ROW_LEFT)
        self.assertEqual('═╬═', MsDosRenderer.SEGMENT_ROW_CENTER)
        self.assertEqual('═╣', MsDosRenderer.SEGMENT_ROW_RIGHT)
        self.assertEqual('╚═', MsDosRenderer.SEGMENT_LAST_ROW_LEFT)
        self.assertEqual('═╩═', MsDosRenderer.SEGMENT_LAST_ROW_CENTER)
        self.assertEqual('═╝', MsDosRenderer.SEGMENT_LAST_ROW_RIGHT)

    def test_fancy_renderer_charset(self) -> None:
        self.assertEqual('│ ', FancyRenderer.ROW_FRAME_LEFT)
        self.assertEqual(' │ ', FancyRenderer.ROW_FRAME_CENTER)
        self.assertEqual(' │', FancyRenderer.ROW_FRAME_RIGHT)
        self.assertEqual('─', FancyRenderer.SEGMENT_ROW_FILL)
        self.assertEqual('┌─', FancyRenderer.SEGMENT_FIRST_ROW_LEFT)
        self.assertEqual('─┬─', FancyRenderer.SEGMENT_FIRST_ROW_CENTER)
        self.assertEqual('─┐', FancyRenderer.SEGMENT_FIRST_ROW_RIGHT)
        self.assertEqual('├─', FancyRenderer.SEGMENT_ROW_LEFT)
        self.assertEqual('─┼─', FancyRenderer.SEGMENT_ROW_CENTER)
        self.assertEqual('─┤', FancyRenderer.SEGMENT_ROW_RIGHT)
        self.assertEqual('└─', FancyRenderer.SEGMENT_LAST_ROW_LEFT)
        self.assertEqual('─┴─', FancyRenderer.SEGMENT_LAST_ROW_CENTER)
        self.assertEqual('─┘', FancyRenderer.SEGMENT_LAST_ROW_RIGHT)

    # * ****************************************************************************************** *
