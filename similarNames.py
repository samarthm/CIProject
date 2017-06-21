import pandas
import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def typoDetect(x, y):
    if fuzz.ratio(x, y) > 75:
        return True
    else:
        return False

df = pandas.read_csv('names.csv', error_bad_lines=False)

arr = df.name1.tolist()

def isSameName(x, y):
    if x.lower() in arr:
        z = arr.index(x)
        if y.lower() in df.loc[z, :].tolist():
            return True
        return False
    elif y.lower() in arr:
        z = arr.index(y)
        if x.lower() in df.loc[z, :].tolist():
            return True
        return False
