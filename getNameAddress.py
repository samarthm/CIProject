import pandas
import re

tempName = []

address_endings = ['ave', 'avenue', 'st', 'street', 'lane', 's', 'a', 'road', 'rd', 'r', 'pl', 'place', 'circle', 'cts',
                   'court', 'concourse', 'plaza', 'plz', 'boulevard', 'blvd', 'highway', 'ln', ]

colnames = ['EnterpriseID', 'LAST', 'FIRST', 'MIDDLE', 'SUFFIX', 'DOB', 'GENDER', 'SSN', 'ADDRESS1', 'ADDRESS2', 'ZIP',
            'MOTHERS_MAIDEN_NAME', 'MRN', 'CITY', 'STATE', 'PHONE', 'PHONE2', 'EMAIL', 'ALIAS']
data = pandas.read_csv('males.csv', names=colnames, low_memory=False)

addresses = data.ADDRESS1.tolist()

return_list = []

name = []


# find the name portion of an address "XYZ 13th Street --> 13th" "212 03 75TH AVENUE APT 26 --> 75th"
def getName():
    spot = -1
    for i in addresses:
        if type(i) is str:
            tempName = re.sub("[^\w]", " ", i).split()
            for x in tempName:
                if x.lower() in address_endings:
                    loc = tempName.index(x)
                    return_list.append([tempName[loc - 1], spot])

        spot += 1
    return return_list

def getSecondary(x):
    name = re.sub("[^\w]", " ", addresses[x+1]).split()
    print(name)
    for y in name:
        if y.isdigit():
            return y
