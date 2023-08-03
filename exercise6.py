from collections.abc import Callable
from typing import Any, Generic, TypeVar

class Car():
    def __init__(self, colour: str):
        self.colour = colour
    

class Exercise6():
    """
    Exercise 6: Objects are references.
    
    Internal note: 
        An exercise class must be the same name as the file but with a capital first letter and must always contain a tests, runExercise and checkResults.
        The array output of tests should always be able to be used as input for checkResults
    """

    def runExercise(self) -> list[Car]:
        # How did we end up both having our car sprayed?
        # 
        # In this task we will notice, following Exercise 1 its tip metaphor, there is a second cabinet with documents.
        # As verbally explained, when a variable holds a class, they in fact hold a reference to that other cabinet instead of the actual value.
        # 
        #
        # Task:
        # - First run the program to see the problem occuring with this code
        # - Make sure the variables are not related to each other

        
        # ALTER CODE BELOW

        myCar = Car('rood')

        yourCar = myCar
        
        yourCar.colour = 'geel'

        # ALTER CODE ABOVE
        
        return [myCar, yourCar]

        

    def tests(self) -> list[list[Car]]:
        return [self.runExercise()]

    def checkResults(self, exerciseResults: list[list[Car]]):
        print('starting problematic outcome:\n  myCar.colour=geel, yourCar.colour=geel:')
        print('desired outcome:\n  myCar.colour=rood, yourCar.colour=geel\n')
        print(f'your result:\n myCar.colour={exerciseResults[0][0].colour}, yourCar.colour={exerciseResults[0][1].colour}')
        print(f'your class instance references:\n myCar={exerciseResults[0][0]}, yourCar={exerciseResults[0][1]}\n')
        
