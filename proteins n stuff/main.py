# Function for peptide() - getting protein name from fasta format
def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.rindex(last)
        return s[start:end]
    except ValueError:
        return ""


#peptide will read a fasta file of proteins and then return the peptides
def peptide(inputfile: str, outputfile: str, *, fileoutput = True, returnoutput = False) -> dict:
    with open(inputfile) as file:
        lines = file.readlines()
        #print(lines)
        info = []
        data = {}
        for i in range(len(lines)):
            lines[i] = lines[i].rstrip('\n')
            if lines[i][0] == ">":
                info.append(i)

    for i in range(len(info)):
        name = find_between(lines[info[i]], "|", "|")
        try:
            data[name] = "".join(lines[info[i]+1:info[i+1]])
        except IndexError:
            data[name] = "".join(lines[info[i]+1:])
    #print(info)
    #print(data)
    data2 = {}
    for k, v in data.items():
        temp = ""
        for i in range(len(v)):
            char = v[i]
            try:
                nxt = v[i+1]
            except IndexError:
                nxt = ""
            if (char == "R" or char == "K") and nxt != "P":
                temp = temp + char + ","
            else:
                temp = temp + char
        data2[k] = temp.split(",")
    if fileoutput:
        with open(outputfile, "w") as file:
            file.write('Protein\tPeptide N\tPeptide\n')
            for k, v in data2.items():
                counter = 0
                for p in v:
                    counter += 1
                    file.write(k+'\t'+str(counter)+'\t'+p+'\n')
    if returnoutput:
        return data2


peptide("test.fasta", "outputs/out.tsv")
