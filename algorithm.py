import pandas
import re
import compareMethods

tempName = []

colnames = ['EnterpriseID', 'LAST', 'FIRST', 'MIDDLE', 'SUFFIX', 'DOB', 'GENDER', 'SSN', 'ADDRESS1', 'ADDRESS2', 'ZIP',
            'MOTHERS_MAIDEN_NAME', 'MRN', 'CITY', 'STATE', 'PHONE', 'PHONE2', 'EMAIL', 'ALIAS']

data = pandas.read_csv('males.csv', names=colnames, low_memory=False, header=0)

f = open("sameSSN.txt", "w+")

SSN = data.SSN.tolist()

FIRST = data.FIRST.tolist()

LAST = data.LAST.tolist()

EID = data.EnterpriseID.tolist()

########################
########################CODE FOR EXACT SSN DATA --> TXT FILE FOR SEARCH
########################
outer = 0
inner = 0
for i in SSN:
    f.write(str(EID[outer]) + " ")
    print(str(EID[outer]) + " " + str(outer))
    for j in SSN:
        if outer is not inner:
            if SSN[inner] == SSN[outer] and (EID[outer] is not EID[inner]):
                f.write(str(EID[inner]) + " ")
                print(str(EID[inner]) + " ")
        inner += 1
    f.write("\n")
    print("\n")
    outer += 1
    inner = 0

f.close()



g = open("similarSSN.txt", "w+")


