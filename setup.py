#!/usr/bin/env python

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
#
# python -m venv venv
# pip install wheel twine
#
# vi flextable/const.py
#
# source venv/activate.fish
# python setup.py sdist bdist_wheel
# twine upload dist/*2.7.0*
#
# pip install --upgrade dist/flex_text_table-2.7.0-py3-none-any.whl

from flextable.const import Const
from setuptools import setup, find_packages

with open("README-pypi.md", "r") as fh:
    logo_url = "https://raw.githubusercontent.com/MarcinOrlowski/python-flex-text-table/master/artwork/flex-text-table-logo.png"
    readme = fh.read().replace(
        r"![flex-text-table logo](artwork/flex-text-table-logo.png)",
        f"![flex-text-table logo]({logo_url})",
        1,
    )

    setup(
        name=Const.APP_NAME,
        version=Const.APP_VERSION,
        packages=find_packages(),
        python_requires=">=3.8",
        install_requires=[
            "wcwidth>=0.2.5",
        ],
        author="Marcin Orlowski",
        author_email="mail@marcinOrlowski.com",
        description=Const.APP_SUMMARY,
        long_description=readme,
        long_description_content_type="text/markdown",
        url=Const.APP_URL,
        keywords="text table ascii command line console shell cli utf8 unicode",
        project_urls={
            "Bug Tracker": "https://github.com/MarcinOrlowski/python-flex-table/issues/",
            "Documentation": "https://github.com/MarcinOrlowski/python-flex-table/",
            "Source Code": "https://github.com/MarcinOrlowski/python-flex-table/",
        },
        # https://choosealicense.com/
        license="MIT License",
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
    )
