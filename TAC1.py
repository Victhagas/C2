def findpolymers(DNA):
  DNA = DNA.upper()
# Criação da lista dos Homopolímeros
  polymers_list = []
  inside_poly = False
  i = 0 

  for x in DNA:
    if not inside_poly:
      try:
        if x == DNA[i+1] and x  == DNA[i+2] and x in 'GCAT':
          inside_poly = True
          polysummary = i+1
          polylength = 1
     
      except:
        break
        
    else:
      if x == DNA[i-1]:
        polylength = polylength + 1 
      else:
        inside_poly = False
        polymers_list.append(((DNA[i-1]), polylength , polysummary))
    i = i+1
  if inside_poly:
    polymers_list.append(((DNA[i-1]), polylength , polysummary)) #ordena o retorno que vai ter, primeiro onde do DNA a sequencia esta, etc.
   

  return polymers_list #Retornar a função que esta dentro do print

print(findpolymers('AAAACCTTTTGGTGGATATATACCTGATATACTAGG'))
print(findpolymers(''))
