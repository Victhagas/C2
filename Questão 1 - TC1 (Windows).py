refArquivo = open("C:\Users\Paulo(Cesar Victor)\Downloads\proteina.fasta")
sequencia = ""
gene = 'TcCLB.506717.80'  # digite o nome do gene
while refArquivo:  # looping de leitura
   linha = refArquivo.readline()
   if linha[1:16] == gene:  # sequencia de AA
       linha = refArquivo.readline()  # ler a line da proteina
       while linha[0] != '>':  # enquanto o primeiro elemento da linha nao for o > ele fara o statement
           sequencia = sequencia + linha.replace('\n', '')  # Tirando os newlines (importante)
           linha = refArquivo.readline()
       print(gene, '\t', sequencia)  # tabulacao
   if linha == '':
       break
refArquivo.close()  # rodar sem, obvio