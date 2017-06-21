import pandas
# import numberManipulator

colnames = ['EnterpriseID', 'LAST', 'FIRST', 'MIDDLE', 'SUFFIX', 'DOB', 'GENDER', 'SSN', 'ADDRESS1', 'ADDRESS2', 'ZIP',
            'MOTHERS_MAIDEN_NAME', 'MRN', 'CITY', 'STATE', 'PHONE', 'PHONE2', 'EMAIL', 'ALIAS']
data = pandas.read_csv('males.csv', names=colnames)

SSN1 = data.SSN.tolist()
SSN = []
index = 1
index1 = 1

for x in SSN1:
    if type(x) is not float:
        SSN.append(x.replace('-', ''))


# for x in SSN:
#     for y in SSN:
#         if x and y is not 'SSN':
#             if not numberManipulator.isWeirdNumber(SSN[index], 9) and not numberManipulator.isWeirdNumber(SSN[index1], 9):
#                 print(x + ' ' + y)
#                 if numberManipulator.isSame(SSN[index], SSN[index1]) + numberManipulator.isTypo(SSN[index], SSN[index1]) < 30:
#                     break
#         index1 += 1
#     index += 1
#     index1 = 0
