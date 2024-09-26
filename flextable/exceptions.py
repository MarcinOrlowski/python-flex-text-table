####################################################################################################
#
# Flex Text Table
# Fast and flexible Pyhon library for text tables.
#
# Copyright ©2023-2024 Marcin Orlowski <mail [@] MarcinOrlowski.com>
# https://github.com/MarcinOrlowski/python-flex-text-table/
#
####################################################################################################

from typing import Union, Any


class NoVisibleColumnsError(RuntimeError):
    def __init__(self):
        super().__init__('No visible columns in table. Enable some?')


class ColumnKeyNotFoundError(KeyError):
    @classmethod
    def for_column_key(cls, column_key: Union[str, int]) -> 'ColumnKeyNotFoundError':
        return cls(f'Column key not found: {column_key}')


class DuplicateColumnKeyError(KeyError):
    @classmethod
    def for_column_key(cls, column_key: Union[str, int]) -> 'DuplicateColumnKeyError':
        return cls(f'Duplicate column key: {column_key}')


class UnsupportedColumnTypeError(TypeError):
    @classmethod
    def for_column_key_val(cls, column_key: str, column_value: Any) -> 'UnsupportedColumnTypeError':
        return cls(f'Unsupported column type ({type(column_value)}: {column_key}')
