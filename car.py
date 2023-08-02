class car:
    def __init__(self, kleur):
        self.colour = kleur


def checkColour(inputColour: str) -> int:
    '''
    Check if the string colour is yellow
    '''
    if (inputColour == 'geel'):
        print('kleur conditie klopte')
        return 1
    else:
        print(f'henks autos kleur is {inputColour =}')
        return 0
