from collections.abc import Callable
from typing import Any, Generic, TypeVar

class Exercise3():
    """
    Exercise 3: Scope.
    
    Internal note: 
        An exercise class must be the same name as the file but with a capital first letter and must always contain a tests, runExercise and checkResults.
        The array output of tests should always be able to be used as input for checkResults
    """

    def runExercise(self, a: int) -> int:
        # Like 2 colleagues but on a different floor?
        # 
        # In this task we will see how scope can effect our program. This is not really an excersice but more of a show and tell.
        #
        # Task:
        # - Run the program and view how the a gets set multiple times
        # - Create a variable inside the if named 'a' with number 8 as value 
        # - See how your variable a will be the result everytime instead of the a defined earlier



        a = a # the program will run multiple times and fill this a with many numbers

        if(True):
            # ALTER CODE BELOW


            
            # ALTER CODE ABOVE

            # return a
        return a
        

    def tests(self) -> list[int]:
        return [self.runExercise(11), self.runExercise(-62), self.runExercise(73), self.runExercise(2000)]

    def checkResults(self, exerciseResults: list[int]):
        print('with a being 11:')
        print('expected outcome: \'8\'')
        print(f'your result: {exerciseResults[0]}\n')
        
        print('with a being -62:')
        print('expected outcome: \'8\'')
        print(f'your result: {exerciseResults[1]}\n')
        
        print('with a being 73:')
        print('expected outcome: \'8\'')
        print(f'your result: {exerciseResults[2]}\n')
        
        print('with a being 2000:')
        print('expected outcome: \'8\'')
        print(f'your result: {exerciseResults[3]}\n')
