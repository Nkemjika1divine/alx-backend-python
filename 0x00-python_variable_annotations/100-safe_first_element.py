#!/usr/bin/env python3
'''Sequence function'''
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns first element of an input sequence"""
    if lst:
        return lst[0]
    else:
        return None
