f = open('data.csv','r')
f2 = open('datastrip.csv','a')

while True:
    line = f.readline()
    line_without_coma = line.replace(',','')
    f2.write(line_without_coma)

    if not line:
        break
f.close()
f2.close()