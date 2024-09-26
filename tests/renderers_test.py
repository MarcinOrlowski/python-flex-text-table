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
        self.assertEquals('| ', PlusMinusRenderer.ROW_FRAME_LEFT)
        self.assertEquals(' | ', PlusMinusRenderer.ROW_FRAME_CENTER)
        self.assertEquals(' |', PlusMinusRenderer.ROW_FRAME_RIGHT)
        self.assertEquals('-', PlusMinusRenderer.SEGMENT_ROW_FILL)
        self.assertEquals('+-', PlusMinusRenderer.SEGMENT_FIRST_ROW_LEFT)
        self.assertEquals('-+-', PlusMinusRenderer.SEGMENT_FIRST_ROW_CENTER)
        self.assertEquals('-+', PlusMinusRenderer.SEGMENT_FIRST_ROW_RIGHT)
        self.assertEquals('+-', PlusMinusRenderer.SEGMENT_ROW_LEFT)
        self.assertEquals('-+-', PlusMinusRenderer.SEGMENT_ROW_CENTER)
        self.assertEquals('-+', PlusMinusRenderer.SEGMENT_ROW_RIGHT)
        self.assertEquals('+-', PlusMinusRenderer.SEGMENT_LAST_ROW_LEFT)
        self.assertEquals('-+-', PlusMinusRenderer.SEGMENT_LAST_ROW_CENTER)
        self.assertEquals('-+', PlusMinusRenderer.SEGMENT_LAST_ROW_RIGHT)

    def test_ms_dos_renderer_charset(self) -> None:
        self.assertEquals('║ ', MsDosRenderer.ROW_FRAME_LEFT)
        self.assertEquals(' ║ ', MsDosRenderer.ROW_FRAME_CENTER)
        self.assertEquals(' ║', MsDosRenderer.ROW_FRAME_RIGHT)
        self.assertEquals('═', MsDosRenderer.SEGMENT_ROW_FILL)
        self.assertEquals('╔═', MsDosRenderer.SEGMENT_FIRST_ROW_LEFT)
        self.assertEquals('═╦═', MsDosRenderer.SEGMENT_FIRST_ROW_CENTER)
        self.assertEquals('═╗', MsDosRenderer.SEGMENT_FIRST_ROW_RIGHT)
        self.assertEquals('╠═', MsDosRenderer.SEGMENT_ROW_LEFT)
        self.assertEquals('═╬═', MsDosRenderer.SEGMENT_ROW_CENTER)
        self.assertEquals('═╣', MsDosRenderer.SEGMENT_ROW_RIGHT)
        self.assertEquals('╚═', MsDosRenderer.SEGMENT_LAST_ROW_LEFT)
        self.assertEquals('═╩═', MsDosRenderer.SEGMENT_LAST_ROW_CENTER)
        self.assertEquals('═╝', MsDosRenderer.SEGMENT_LAST_ROW_RIGHT)

    def test_fancy_renderer_charset(self) -> None:
        self.assertEquals('│ ', FancyRenderer.ROW_FRAME_LEFT)
        self.assertEquals(' │ ', FancyRenderer.ROW_FRAME_CENTER)
        self.assertEquals(' │', FancyRenderer.ROW_FRAME_RIGHT)
        self.assertEquals('─', FancyRenderer.SEGMENT_ROW_FILL)
        self.assertEquals('┌─', FancyRenderer.SEGMENT_FIRST_ROW_LEFT)
        self.assertEquals('─┬─', FancyRenderer.SEGMENT_FIRST_ROW_CENTER)
        self.assertEquals('─┐', FancyRenderer.SEGMENT_FIRST_ROW_RIGHT)
        self.assertEquals('├─', FancyRenderer.SEGMENT_ROW_LEFT)
        self.assertEquals('─┼─', FancyRenderer.SEGMENT_ROW_CENTER)
        self.assertEquals('─┤', FancyRenderer.SEGMENT_ROW_RIGHT)
        self.assertEquals('└─', FancyRenderer.SEGMENT_LAST_ROW_LEFT)
        self.assertEquals('─┴─', FancyRenderer.SEGMENT_LAST_ROW_CENTER)
        self.assertEquals('─┘', FancyRenderer.SEGMENT_LAST_ROW_RIGHT)

    # * ****************************************************************************************** *
