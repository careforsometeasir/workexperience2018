import csv
import matplotlib.pyplot as plt
from numpy import arange


# here is a nice function that switches some base thingies
def switcheroo(s):
    s = s.replace('/', '')
    s = sorted(s)
    if len(s) == 2:
        s.insert(1, '/')
    out = ''
    for i in s:
        out += i
    return out


def process(filepath, roundpercentages = 5,delimiter='\t'):
    with open(filepath) as file:
        read = csv.reader(file, delimiter=delimiter)
        data = {'markers': {}, 'totals': {'total': 0, 'missing': 0}, 'percentages': {}}
        current = ''
        go = False
        for row in read:
            marker = True
            if go:
                for cell in row:
                    if marker:
                        data['markers'][cell] = {'bases': {}, 'missing': 0}
                        current = cell
                        marker = False
                    else:
                        switched = switcheroo(cell)
                        if switched == '-':
                            data['markers'][current]['missing'] += 1
                            data['totals']['missing'] += 1
                        elif switched not in data['markers'][current]['bases']:
                            data['markers'][current]['bases'][switched] = 1
                        else:
                            data['markers'][current]['bases'][switched] += 1
                        if switched not in data['totals'] and switched != '-':
                            data['totals'][switched] = 1
                        elif switched != '-':
                            data['totals'][switched] += 1
                        data['totals']['total'] += 1
            else:
                go = True
        for i, v in data['totals'].items():
            data['percentages'][i] = round((v/data['totals']['total'])*100, roundpercentages)
    return data


data = process('for_richard.txt')
nps = len(data['percentages'])-1
values = list(data['percentages'].values())[1:]
labels = list(data['percentages'].keys())[1:]
fig, ax = plt.subplots()
index = arange(nps)
bar_width = 0.7
bars = ax.bar(index, values, bar_width, color='b')
ax.set_xlabel('Base')
ax.set_ylabel('Percentage')
ax.set_title('Percentages of bases in data sample')
ax.set_xticks(index)
ax.set_xticklabels(labels)
for i, v in enumerate(values):
    if v > 5:
        ax.text(i, v-0.2, str(round(v, 3))+'%', color='white', fontweight='bold', rotation=90, ha='center', va='top')
    else:
        ax.text(i, v + 0.25, str(round(v, 3))+'%', color='blue', fontweight='bold', rotation=90, ha='center', va='bottom')
plt.show()
print(data)
file = open('outputs n stuff/data.json', 'w')
file.write(str(data))
file.close()
