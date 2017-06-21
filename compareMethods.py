import numberManipulator


#compare SSN and return boolean

def matchSSN(x, y):

    if type(x) is str and type(y) is str:
        x = ''.join(e for e in x if e.isalnum())
        y = ''.join(e for e in y if e.isalnum())

        if (len(x) == len(y)):
            if not (numberManipulator.isWeirdNumber(x, 9)) and not numberManipulator.isWeirdNumber(y, 9):
                if numberManipulator.isSame(x, y) < 11 or numberManipulator.isTypo(x, y) < 11:
                    return True
            else:
                return False

        return False
    else:
        return False


#compare DOB and return boolean

def matchDOB(x, y):

    x = x.split('/')
    y = y.split('/')

    if len(x) == 3 and len(y) == 3:
        if x[0] == y[0] and x[1] == y[1] and x[2] == y[2]:
            return True
        elif x[2] == y[2] and x[0] == y[1] and x[1] == y[0]:
            return True
        else:
            return False

    return False




print(matchDOB('4/3/16', '3/4/16'))