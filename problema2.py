#para este exercicio devemos notar que a eficiência do código importa bastante,
#pois para N = 4000000 um algoritmo recursivo não chega nem perto do tempo de execução
#de um interativo, tanto é que para a recursão acaba nem executando o código

prim = 1
seg = 2
soma = 0

while seg <= 4000000:
  if seg % 2 == 0:
    soma += seg
  prim, seg = seg, prim + seg
print(soma) 
