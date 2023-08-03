from collections.abc import Callable
from typing import Any, Generic, TypeVar

class Car:
    def __init__(self, kleur):
        self.colour = kleur

class Exercise8():
    """
    Exercise 8: Function parameters.
    
    Internal note: 
        An exercise class must be the same name as the file but with a capital first letter and must always contain a tests, runExercise and checkResults.
        The array output of tests should always be able to be used as input for checkResults
    """

    def runExercise(self) -> list[bool]:
        # Break free of the scope! Break free of states!
        # 
        # In this task we will learn how to create a function which is less dependant on outer scope.
        #
        # Task:
        # - Make sure the function doesnt use the myCar varable directly.
        # - Try and also stop using the resultList inside the def. 
        #   When done both you should be able to cut and paste the def at line three, you are now free to use the func in every class.

        resultList: list[bool] = []

        # ALTER CODE BELOW

        myCar = Car('rood')

        def checkColour():
            if (myCar.colour == 'geel'):
                resultList.append(True)
            else:
                resultList.append(False)

        checkColour()

        myCar.colour = 'blauw'

        checkColour()

        myCar.colour = 'geel'

        checkColour()

        # ALTER CODE ABOVE

        return resultList
        

    def tests(self) -> list[list[bool]]:
        return [self.runExercise()]

    def checkResults(self, exerciseResults: list[list[bool]]):
        print('with the colours changing to rood, blauw, geel:')
        print('expected outcome: [False, False, True]')
        print(f'your result: {exerciseResults[0]}\n')
        