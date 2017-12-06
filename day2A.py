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
    total += max(row) - min(row)

print total
