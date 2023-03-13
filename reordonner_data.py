f = open('datastrip.csv','r')
f2 = open('good_data.csv','w')

while True:
    line = f.readline()
    pline = line[:len(line)-3]
    gline = pline.replace("]","],")
    fline = gline +"]]"
    f2.write(fline+'\n')

    if not line:
        break
    
f.close()
f2.close()