'''A look at mypy and the typing module

The mypy cheatsheet is super helpful here

https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html#cheat-sheet-py3
'''
from typing import Dict, List


def list_of_strs_repeated(string_to_repeat: str, num_repeats: int) -> List[str]:
    """Returns a list containing string repeated N times

    >>> list_of_strs_repeated('Hello!', 3)
    ['Hello!', 'Hello!', 'Hello!']
    """
    return [string_to_repeat] * num_repeats