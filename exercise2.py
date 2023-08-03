from collections.abc import Callable
from typing import Any, Generic, TypeVar

class Exercise2():
    """
    Exercise 2: Data types.
    
    Internal note: 
        An exercise class must be the same name as the file but with a capital first letter and must always contain a tests, runExercise and checkResults.
        The array output of tests should always be able to be used as input for checkResults
    """

    def runExercise(self, a: str) -> int:
        # But when I'm writing on paper they ARE the same!
        # 
        # In this task we will encounter that theres more to a variable then just the value its holding.
        # You can already use variable a. No need to create.
        #
        # Task:
        # - Create a variable which holds a number/int version of the string in a
        # - If the type-changing wasnt possible, return -5

        # CREATE CODE BELOW





        # CREATE CODE ABOVE

        

    def tests(self) -> list[int]:
        return [self.runExercise('1'), self.runExercise('46'), self.runExercise('hello there')]

    def checkResults(self, exerciseResults: list[int]):
        print(f'expected outcome: 1\n\
              your result: {exerciseResults[0]}')
        print(f'expected outcome: 46\n\
              your result: {exerciseResults[1]}')
        print(f'expected outcome: -5\n\
              your result: {exerciseResults[2]}')
