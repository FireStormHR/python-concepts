from utilities.task import importExecuteExercise
from utilities.tryc import tryc

exerciseNumberAsStr = input(
    'Which exercise do you want to run? Enter a number.\n\
        Options:\n\
            1: Variables and conditions\n\
            2: Data types\n\
            3: Scope\n\
            4: for-loop\n\
            5: Classes/objects\n\
            6: Objects are references\n\
            7: Functions\n\
            8: Function parameters\n\
            9 WIP: Commenting and in-file documentation\n\
            10 WIP: statically typed vs dynamically typed\n\
            \n')

inputIsIntAndInRange = lambda : int(exerciseNumberAsStr) < 9

# if input can be parsed and value is within range
if(tryc(inputIsIntAndInRange, False)):
    print(f'executing exercise {exerciseNumberAsStr} ...\n')
    importExecuteExercise(f'exercise{exerciseNumberAsStr}')
else:
    print("Input not recognised as a valid exercise number.")

input('Press enter to close application...\n\n')
