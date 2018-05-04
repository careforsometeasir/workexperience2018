import csv
import matplotlib.pyplot as plt


def switcheroo(s):
    s = s.replace('/', '')
    s = sorted(s)
    if len(s) == 2:
        s.insert(1, '/')
    return s


def count(filepath):
    items = {
        'total':0
    }
    percentages = {}
    with open(filepath) as file:
        data = csv.reader(file, delimiter='\t')
        rowgo = False
        for row in data:
            cellgo = False
            if rowgo:
                for cell in row:
                    if cellgo:
                        if switcheroo(cell) in items:
                            items[switcheroo(cell)] += 1
                        else:
                            items[switcheroo(cell)] = 1
                        items['total'] += 1
                    else:
                        cellgo = True
            else:
                rowgo = True
    for key, value in items.items():
        percentages[key] = (value/items['total'])*100
    return percentages


explode = []

c = count('for_richard.txt')
for v in list(c.values())[1:]:
    if v < 2:
        explode.append(0.2)
    else:
        explode.append(0)
explode = tuple(explode)
print(explode)
fig, ax1 = plt.subplots()
ax1.pie(list(c.values())[1:],explode=explode, labels=tuple(c.keys())[1:], startangle=90)
ax1.axis('equal')
ax1.legend()
plt.show()
print(c)
