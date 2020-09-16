import csv
with open('C:\Users\Paulo(Cesar Victor)\Downloads\codigo5.csv') as csvfile:
    refArquivo = csv.reader(csvfile, delimiter = ',')
    for data in refArquivo:
        if data[3].upper().rstrip() == 'BIRD':
            print(data)




