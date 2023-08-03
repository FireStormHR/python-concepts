from collections.abc import Callable
from typing import Any, Generic, TypeVar

class Exercise1():
    """
    Exercise 1: Variables and conditions.
    
    Internal note: 
        An exercise class must be the same name as the file but with a capital first letter and must always contain a tests, runExercise and checkResults.
        The array output of tests should always be able to be used as input for checkResults
    """

    def runExercise(self, a: int, b: int) -> int:
        # Looks like math!
        # 
        # In this task we will assign some variables for the first time and even create an if!
        # You can already use variables a and b. No need to create.
        #
        # Task:
        # - Create a variable {a nice name} with value 5 
        # - Create an if-statement that only enters its block when the sum of the a,b,{a nice name} variables is equal or less than 30. Fill in that sum behind the 'return'

        # ALTER CODE BELOW



        if ():
            return 
        # ALTER CODE ABOVE
        else:
            return -46
        

    def tests(self) -> list[int]:
        return [self.runExercise(1, 1), self.runExercise(-2, -3), self.runExercise(20, 5), self.runExercise(20, 6)]

    def checkResults(self, exerciseResults: list[int]):
        print(f'expected outcome: \'7\'\n\
              your result: {exerciseResults[0]}')
        print(f'expected outcome: \'0\'\n\
              your result: {exerciseResults[1]}')
        print(f'expected outcome: \'30\'\n\
              your result: {exerciseResults[2]}')
        print(f'expected outcome: \'-46\'\n\
              your result: {exerciseResults[3]}')
