import csv
with open('data.csv', 'rt') as inp, open(r'males.csv', 'a') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
        if row[6].lower() == 'male' or row[6].lower() == 'm':
                writer.writerow(row)
