from collections.abc import Callable
from typing import Any, Generic, TypeVar

class Exercise4():
    """
    Exercise 4: for-loop.
    
    Internal note: 
        An exercise class must be the same name as the file but with a capital first letter and must always contain a tests, runExercise and checkResults.
        The array output of tests should always be able to be used as input for checkResults
    """

    def runExercise(self, amountOfRows: int) -> str:
        # Building a real pyramid is easier!
        # 
        # In this task we will create a pyramid, but its dynamic and centered!
        # You must use variable amountOfRows. No need to create.
        # This is a hard task and will take some time.
        # TIP: an enter in a string is represented as \n
        #
        # Example result 1 with amountOfRows being 2:
        # {space}x
        # xxx
        #
        # Example result 2 with amountOfRows being 3:
        # {space}{space}x
        # {space}xxx
        # xxxxx
        #
        # Task:
        # - Using the amountOfRows, create a text/string which looks like a pyramid.
        # - You will need a for-statement

        # ALTER CODE BELOW


        return 'x'



        # ALTER CODE ABOVE

        

    def tests(self) -> list[str]:
        return [self.runExercise(1), self.runExercise(2), self.runExercise(3), self.runExercise(4)]

    def checkResults(self, exerciseResults: list[int]):
        print('with amountOfRows being 1:')
        print('expected outcome:\nx')
        print(f'your result:\n{exerciseResults[0]}\n')
        
        print('with amountOfRows being 2:')
        print('expected outcome:\n x\nxxx')
        print(f'your result:\n{exerciseResults[1]}\n')
        
        print('with amountOfRows being 3:')
        print('expected outcome:\n  x\n xxx\nxxxxx')
        print(f'your result:\n{exerciseResults[2]}\n')
        
        print('with amountOfRows being 4:')
        print('expected outcome:\n   x\n  xxx\n xxxxx\nxxxxxxx')
        print(f'your result:\n{exerciseResults[3]}\n')
