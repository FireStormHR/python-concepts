from collections.abc import Callable
from typing import Any, Generic, TypeVar

# ALTER CODE BELOW








# ALTER CODE ABOVE

class Exercise5():
    """
    Exercise 5: Classes/objects.
    
    Internal note: 
        An exercise class must be the same name as the file but with a capital first letter and must always contain a tests, runExercise and checkResults.
        The array output of tests should always be able to be used as input for checkResults
    """

    def runExercise(self, inputColour: str) -> str:
        # Missing the blueprint!
        # 
        # In this task we will get to know the blueprint of a class.
        # Variables colour is already. No need to create.
        #
        # Task:
        # - Create a class which works with the code below. NOTE Where to code in this exercise!

        myCar = Car(inputColour)

        myCar.doNothing()

        return myCar.colour
        

    def tests(self) -> list[str]:
        return [self.runExercise('rood'), self.runExercise('groen'), self.runExercise('blauw'), self.runExercise('neon race geel')]

    def checkResults(self, exerciseResults: list[str]):
        print('with inputColour being \'rood\':')
        print('expected outcome: \'rood\'')
        print(f'your result: {exerciseResults[0]}\n')
        
        print('with inputColour being \'groen\':')
        print('expected outcome: \'groen\'')
        print(f'your result: {exerciseResults[1]}\n')
        
        print('with inputColour being \'blauw\':')
        print('expected outcome: \'blauw\'')
        print(f'your result: {exerciseResults[2]}\n')
        
        print('with inputColour being \'neon race geel\':')
        print('expected outcome: \'neon race geel\'')
        print(f'your result: {exerciseResults[3]}\n')
