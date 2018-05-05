# By Ryszard Wypijewski 2018
import csv
#  CSV module is used for various delimiter separated files


# ~~ the comments following PEP8 - comments should start with '# ' - are actual comments
# the rest is code that's been commented out ~~

# Here's the main function for processing a file
def pedigree(filepath: str, *, delimiter='\t') -> dict:
    file = open(filepath)
    read = csv.reader(file, delimiter=delimiter)
    data = list(read)
    file.close()
    #print(data)
    # This is a nice key to swap the various symbols for one that mean the same thing
    key = {
        'x': 'x',
        '*': ' x ',
        '/': ' x ',
        '(': '(',
        '[': '(',
        '{': '(',
        ']': ')',
        ')': ')',
        '}': ')'
    }

    # This dictionary will contain the formatted data
    stuff = {}

    # If you're going to run this on a pedigree with 3 columns, the first being line numbers, uncomment the next 2 lines, or comment them to run a pedigree with 2.
    #for row in data:
        #del row[0]
    #print(data)
    #print('---------------')

    # This for loop replaces substrings in the data using the key
    for row in data:
        for k, v in key.items():
            row[1] = row[1].replace(k, v)
        #print(row[1])

        # Here an unknown cross is replaced with an empty string
        row[1] = row[1].replace('Unknown cross', '')

        # This is the mess that replaces substrings for other strings, for the eval() function
        pre = '[\'' + row[1].replace(' x ', '\', \'') + '\']'
        #print(pre)
        nxt = pre.replace(')\'', '\']').replace("\'(", '[\'').replace("\'(", '[\'').replace(') \'', '\']').replace(')\'', '\']')
        #if nxt.count('[') > nxt.count(']'):
            #nxt = nxt + ']'
        #elif nxt.count(']') > nxt.count('['):
            #nxt = '[' + nxt
        #print(nxt)

        # Here the program TRIES to evaluate ( eval() ) the string
        try:
            stuff[row[0]] = eval(nxt)
        # if it's unable to then it sets it to UNABLE TO PARSE
        except SyntaxError:
            stuff[row[0]] = ['UNABLE TO PARSE']
        #print(stuff[row[0]])
        #print('---------------')
    # final product is returned
    return stuff


# I couldn't think of a name for this function
# It is a recurring function that changes the parents so that all of the children have parents like 'name, name'
def badoodle(d: dict, counter=0) -> dict:
    # Making a copy of the dictionary to modify, so that I don't modify a dictionary while looping through it
    stuff2 = d.copy()
    for k in d.keys():
        val = d[k]
        for i in val:
            if type(i) is list:
                counter += 1
                index = d[k].index(i)
                stuff2[k][index] = 'x' + str(counter)
                stuff2['x' + str(counter)] = i
            # This is quite inefficient but it loops through the list to see if it contains a list
            # and then sends it off to itself
            for x in i:
                if type(i) is list:
                    stuff2 = badoodle(stuff2, counter)
    # returns the result
    return stuff2


# COPIED FROM woah.py
def helium(d: dict) -> str:
    temp = ""
    for key in d.keys():
        temp2 = ""
        for x in d[key]:
            temp2 = temp2 + '\t' + x
        temp = temp + key + temp2 + '\n'
    return temp


p = badoodle(pedigree('pedigrees2.txt'))
print(p)

# Helium:
#print(helium(p))

# from Ryszard :)
