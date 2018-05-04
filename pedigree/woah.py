import csv

# Here's the original
# Look at woah2.py for the whole thing!
# This one, however, outputs some text that can be pasted into a text editor
# All you have to do is add a description and column titles in the Helium format and boom!
# Actually I'll copy it into a function on woah2.py


def pedigree(filepath):
    file = open(filepath)
    read = csv.reader(file, delimiter='\t')
    data = list(read)
    file.close()
    stuff = {}
    for row in data:
        pre = '[\'' + row[1].replace(' x ', '\', \'') + '\']'
        nxt = pre.replace(')\'', '\']').replace("\'(", '[\'')
        stuff[row[0]] = eval(nxt)
    counter = 0
    stuff2 = stuff.copy()
    for k in stuff.keys():
        val = stuff[k]
        for i in val:
            if type(i) is list:
                counter += 1
                index = stuff[k].index(i)
                stuff2[k][index] = 'x' + str(counter)
                stuff2['x' + str(counter)] = i
    return stuff2


pedigrees = pedigree('pedigrees.txt')
print(pedigrees)
temp = ""
for key in pedigrees.keys():
    temp2 = ""
    for x in pedigrees[key]:
        temp2 = temp2 + '\t' + x
    temp = temp + key + temp2 + '\n'
print(temp)


