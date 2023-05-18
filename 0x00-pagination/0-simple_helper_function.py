#!/usr/bin/env python3
""" a function named index_range that takes two integer arguments """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ return the start and end index of some pages
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
