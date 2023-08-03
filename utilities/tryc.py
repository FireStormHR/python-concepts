from collections.abc import Callable
from typing import Any, TypeVar

T = TypeVar('T')

def tryc(func: Callable[[], T], catchReturnVal: T):
    """
    Tries to run `func` and return its result. If `func` throws an exception return `catchReturnVal`
    """
    try:
        return func()
    except Exception as e:
        return catchReturnVal