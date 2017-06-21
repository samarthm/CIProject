# find if two numbers are the same but have a switch
def isSame(x, y):
    b = str(x)
    new = []

    for digit in b:
        new.append(int(digit))

    d = str(y)
    comp = []

    for digit in d:
        comp.append(int(digit))

    num_switches = 0
    index = 0
    score = 0

    if (len(new) > 5):
        max_typos = int(len(new) % 5) + 1
    else:
        max_typos = 1

    if (len(new) == len(comp)):
        for x in new:
            if (index == 0):
                if (new[index] == comp[index]):
                    score += 0
                elif (new[index] == comp[index + 1]):
                    score += 5
                    num_switches += 1
                else:
                    score += 15
            elif (index == len(new) - 1):
                if (new[index] == comp[index]):
                    score += 0
                elif (new[index] == comp[index - 1]):
                    score += 5
                    num_switches += 1
                else:
                    score += 20
            else:
                if (new[index] == comp[index]):
                    score += 0
                elif (new[index] == comp[index + 1]):
                    score += 5
                    num_switches += 1

                elif (new[index] == comp[index - 1]):
                    score += 5
                    num_switches += 1
                else:
                    score += 20

            index += 1

    return score


# return the score of two numbers to check if theres a typo
def isTypo(x, y):
    score = 0
    index = 0
    b = str(x)
    new = []
    for digit in b:
        new.append(int(digit))
    d = str(y)
    comp = []
    for digit in d:
        comp.append(int(digit))

    for x in new:
        if (new[index] == comp[index]):
            score += 0
        elif (new[index] == comp[index] + 1 or new[index] == comp[index] - 1):
            score += 10
        else:
            score += 20
        index += 1

    return score


# return boolean for if the value is bogus
def isWeirdNumber(x, y):
    b = str(x)
    new = []
    sum1 = 0
    index1 = 1
    for digit in b:
        new.append(int(digit))

    for z in new:
        if (new[0] == new[index1]):
            sum1 += 1

    if (sum1 > len(new) - 2):
        return True

    elif len(set(new).intersection([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) == y:
        return True

    elif len(x) is not y:
        return True

    return False
