refArquivo = open('C:\Users\Paulo(Cesar Victor)\Downloads\proteina.fasta')
gene = ''
sequencia = ''
for lines in refArquivo.readlines():
    if '>' in lines:
        if sequencia != '':
            print(gene)
            print(sequencia)
            gene = lines.strip('\n')
    else:
        sequencia = sequencia + lines.strip('\n')
print(sequencia)
print(gene)
