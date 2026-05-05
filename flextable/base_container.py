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

from abc import ABC
from typing import Dict, TypeVar, Union, Type, Optional, Generic

T = TypeVar("T")  # noqa: WPS111


class BaseContainer(Generic[T], ABC):
    def __init__(
        self,
        items: Optional[Dict[Union[str, int], T]] = None,  # noqa: WPS234
        data_type: Type[T] = None,
    ) -> None:
        if data_type is None:
            raise TypeError("data_type argument must be provided")

        self._data_type: Type[T] = data_type
        self.container = {}

        if items is not None:
            for key, value in items.items():
                self.__setitem__(key, value)

    # * ****************************************************************************************** *

    @property
    def container(self) -> Dict:
        return self._container

    @container.setter
    def container(self, value: Dict) -> None:
        self._container = value

    # * ****************************************************************************************** *

    def keys(self):
        return self._container.keys()

    def values(self):
        return self._container.values()

    def items(self):
        return self._container.items()

    # * ****************************************************************************************** *
    # To make it act as dict

    def __len__(self):
        """
        Implement the __len__ method to get the size of the dictionary
        """
        return len(self._container)

    def __getitem__(self, index: Union[str, int]) -> T:
        """
        Implement the __getitem__ method to access items using keys
        """
        return self._container[index]

    def __setitem__(self, key: Union[str, int], value: T):
        """
        Implement the __setitem__ method to set items using keys
        """
        if not isinstance(value, self._data_type):
            raise TypeError(f"Provided row must be '{T}' subclass, got {type(value)}")
        self._container[key] = value

    def __delitem__(self, key: Union[str, int]):  # noqa: WPS603
        """
        Implement the __delitem__ method to delete items using keys
        """
        del self._container[key]

    def __iter__(self):
        """
        Implement the __iter__ method to make the class iterable
        """
        return iter(self._container)

    def __contains__(self, key: Union[str, int]):
        """
        Implement the __contains__ method to check if a key exists
        """
        return key in self._container
