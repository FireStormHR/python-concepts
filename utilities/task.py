import importlib

def importExecuteExercise(exerciseName: str):
    """
        Does three steps:
        1. Dynamically imports an exercise module. (if done traditionally, a module is not allowed to contain compile errors, which is what we want in this case)
        2. Gets the exercise class (same-name as module but with capital)
        3. Execute exercise and check result

        Parameters
        ----------
        @param exerciseName Lowercase name of the exercise. Used for importing module and getting class. Example: `exercise1`

    """

    capitalExerciseName = exerciseName.capitalize()

    # import module
    importedModule = importlib.import_module(exerciseName)

    # get class and instantiate
    exerciseStaticClass = getattr(importedModule, capitalExerciseName)
    exerciseClass = exerciseStaticClass()

    # execute
    results = exerciseClass.tests()
    exerciseClass.checkResults(results)
