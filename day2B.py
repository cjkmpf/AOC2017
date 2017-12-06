def divide_row(row):
    for n in range(0, len(row)):
        for i in range(n+1, len(row)):
            if n == i:
                continue
            if row[n] % row[i] == 0:
                return row[n]/row[i]
            if row[i] % row[n] == 0:
                return row[i]/row[n]

sheet = []

with open('day2input.txt', 'r') as f:
    for line in f:
        x = line
        if x.endswith('\n'):
            x = x[0:len(x)-1]
        sheet.append(x.split(' '))

int_sheet = []
for row in sheet:
    int_sheet.append([ int(x) for x in row ])

total = 0
for row in int_sheet:
    total += divide_row(row)

print total
