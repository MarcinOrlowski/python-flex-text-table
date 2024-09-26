# Flex Text Table

```ascii
#####.##....#####.##...##...######.#####.##...##.######...######...#....#####..##....#####
##....##....##.....##.##......##...##.....##.##....##.......##....###...##..##.##....##...
##....##....##......###.......##...##......###.....##.......##...##.##..##..##.##....##...
####..##....####.....#........##...####.....#......##.......##..##...##.#####..##....####.
##....##....##......###.......##...##......###.....##.......##..#######.##..##.##....##...
##....##....##.....##.##......##...##.....##.##....##.......##..##...##.##..##.##....##...
##....#####.#####.##...##.....##...#####.##...##...##.......##..##...##.#####..#####.#####
```

Fast and flexible Pyhon library for text tables.

[![PyPI version](https://badge.fury.io/py/flex-text-table.svg)](https://badge.fury.io/py/flex-text-table)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/flex-text-table?style=plastic)](https://pypi.org/project/flex-text-table/)
[![Python Version](https://img.shields.io/pypi/pyversions/flex-text-table.svg)](https://pypi.org/project/flex-text-table/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

There's also [PHP version of ths library](https://github.com/MarcinOrlowski/php-text-table).

---

## Features

1. Simple API, easy to use,
2. Lightweight (no additional dependencies),
3. Production ready.

---

## Usage example

Simplest possible usage:

```python
from flextable.table import FlexTable       # Import FlexTable root class

table = FlexTable(['ID', 'NAME', 'SCORE'])  # Define table with 3 columns
table.add_rows([
    [1, 'John', 12],                        # Add 2 rows, 3 columns each
    [2, 'Tommy', 15],
])
print(table.render())                       # Render table as string and print
```

would produce nice text table:

```ascii
┌────┬───────┬───────┐
│ ID │ NAME  │ SCORE │
├────┼───────┼───────┤
│ 1  │ John  │ 12    │
│ 2  │ Tommy │ 15    │
└────┴───────┴───────┘
```

See more usage examples in [project docs](https://github.com/MarcinOrlowski/python-flex-text-table/).

---

## License

* Written and copyrighted &copy;2023-2024 by Marcin Orlowski <mail (#) marcinorlowski (.) com>
* Flex Text Table is open-sourced software licensed under
  the [MIT license](http://opensource.org/licenses/MIT)
