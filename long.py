f = open('117.txt')
t = f.read()
t = t.split('>')
t = t[1:]
dna = []
for i in range(len(t)):
    dna.append(t[i])
    dna[i] = dna[i].replace('\n','')
    dna[i] = dna[i][13 :]
print(dna)
superstr = dna.pop(0)
while dna != []:
    print(dna)
    t = len(dna[0]) // 2
    temp = dna[0][0:t]
    r = superstr.rfind(temp)
    f = superstr.find(dna[0][-t:])
    if r != -1:
        if dna[0][:len(superstr) - r] == superstr[r:]:
            superstr = superstr + dna[0][len(superstr) - r:]
            dna.pop(0)
    elif f != -1:
        if dna[0][- t - f:] == superstr[:t + f]:
            superstr = dna[0][:- t - f] + superstr
            dna.pop(0)
    else:
        dna.append(dna.pop(0))
print(superstr)


