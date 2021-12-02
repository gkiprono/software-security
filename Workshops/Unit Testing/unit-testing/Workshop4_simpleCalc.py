##################################################################
#Gabriel Kiprono
#September 24
#Workshop4_simpleCalc.py
#
##################################################################
def multiplyNumbers(a,b):
    #convert a
    try:
        argA = int(a)
    except ValueError:
        argA = float(a)
    except ValueError:
        return "wrong input"
    
    #convert b
    try:
        argB = int(b)
    except ValueError:
        ArgB = float(b)
    except ValueError:
        return "wrong input"

    return argA*argB


def divideTwoNums(a,b):
    #convert a
    try:
        argA = int(a)
    except ValueError:
        argA = float(a)
    except ValueError:
        return "wrong input"

    #convert b
    try:
        argB = int(b)
    except ValueError:
        ArgB = float(b)
    except ValueError:
        return "wrong input"
    quotient = 0
    try:
        quotient = argA/argB
        return quotient
    except ZeroDivisionError:
        return "Error, Division by zero!"

    