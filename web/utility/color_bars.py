from collections import Set
from typing import List, Tuple


def parse_set_string(cb_set: str) -> Tuple[List[int], List[int]]:
    """ Converts a textual representation of color bars demonstration and permutation to a set representation

    :param cb_set: textual representation
    :return: lists of color bars to show and to store
    """
    to_show, permutation = (list(map(int, (bar for bar in part.split('_') if bar))) for part in cb_set.split('__'))
    return to_show, permutation


def join_set_string(to_show: List[int], permutation: List[int]) -> str:
    """ Converts a list representation of color bars to show and to store to a string representation

    :param to_show:
    :param permutation:
    :return:
    """
    return '__'.join('_'.join(map(str, part)) for part in (to_show, permutation))


def exclude_from(s: Set, v) -> Set:
    """ Removes an element from the set and returns modified set

    :param s: set of elements
    :param v: on of elements
    :return: set without an element
    """
    result = s.copy()
    result.remove(v)
    return result
