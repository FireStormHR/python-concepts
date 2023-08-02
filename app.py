from car import car, checkColour

x = 5
y = 'hoi'

henksAuto = car('rood')


checkColour(henksAuto.colour)

henksAuto.colour = 'blauw'
checkColour(henksAuto.colour)

henksAuto.colour = 'geel'
result = checkColour(henksAuto.colour)

"""
variables
conditions
data-types
classes/objects
objects are references (stored in heap insted of stack)
functions
function parameters
commenting and in-file documentation (Docstrings)
statically typed vs dynamically typed
"""

exerciseNumber = input(
    'Which exercise do you want to run? Enter a number.\n\
        Options:\n\
            1: Variables and conditions\n\
            a\n')

match exerciseNumber:
    case "1":
        ""
    case "2":
        ""
    case "3":
        ""
    case "4":
        ""
    case "5":
        ""
    case "6":
        ""
    case _:
        print("Input not recognised as a valid exercise number")

input('application closing after input\n')
