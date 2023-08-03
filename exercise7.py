from collections.abc import Callable
from typing import Any, Generic, TypeVar

class Car:
    def __init__(self, kleur):
        self.colour = kleur

class Exercise7():
    """
    Exercise 7: Functions.
    
    Internal note: 
        An exercise class must be the same name as the file but with a capital first letter and must always contain a tests, runExercise and checkResults.
        The array output of tests should always be able to be used as input for checkResults
    """

    def runExercise(self) -> list[bool]:
        # So efficient! Are you enjoying this?
        # 
        # In this task we will make use of the function functionality.
        #
        # Task:
        # - Shorten this code by making a function without breaking the program.

        resultList: list[bool] = []

        # ALTER CODE BELOW

        myCar = Car('rood')

        if (myCar.colour == 'geel'):
            resultList.append(True)
        else:
            resultList.append(False)

        myCar.colour = 'blauw'

        if (myCar.colour == 'geel'):
            resultList.append(True)
        else:
            resultList.append(False)

        myCar.colour = 'geel'

        if (myCar.colour == 'geel'):
            resultList.append(True)
        else:
            resultList.append(False)

        # ALTER CODE ABOVE

        return resultList
        

    def tests(self) -> list[list[bool]]:
        return [self.runExercise()]

    def checkResults(self, exerciseResults: list[list[bool]]):
        print('with the colours changing to rood, blauw, geel:')
        print('expected outcome: [False, False, True]')
        print(f'your result: {exerciseResults[0]}\n')
        