'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

#Procurando a solução por força bruta

for a in range(1,1000):
    for b in range(a+1, 1000):
        for c in range(b+1, 1000):
            if a + b + c == 1000 and a**2 + b**2 == c**2:
                print(f'a = {a}, b = {b}, c = {c}')

#Uma melhora
'''Podemos usar um pouco de matemática para conseguir um resultado melhor. vemos que na solução buscada
c=1000−a−b,
portanto não precisamos percorrer todos os valores de c. Issso sugere a seguinte modificação:'''

for a in range(1, 1000):
    for b in range(a+1, 1000):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print(f'a = {a}, b = {b}, c = {c}')

#Mais matemática
'''Isso é bem mais eficiente, mas ainda não acabamos com as possibilidades da matemática do problema. Lembramos que
a**2+b**2=c**2, e substituindo a expressão c=1000−a−b, chegamos a a**2+b**2=(1000−a−b)2, que desenvolve para
a**2+b**2=10002+a**2+b**2−2000a−2000b+2ab, que simplifica para 0=10002−2000a−2000b+2ab. Isolando b temos:
2000b−2ab=1000**2−2000a, ou b=1000(1000−2a)/2(1000−a)=500(1000−2a)/(1000−a). O que precisamos agora é apenas achar um valor
de a<1000 para o qual o valor de b calculado acima é inteiro, o que sugere o seguinte código:'''

for a in range(1, 1000):
    b = 500 * (1000 - 2 * a) / (1000 - a)
    if int(b) == b:
        b = int(b)
        break
print(f'a = {a}, b = {b}, c = {1000 - a - b}')

#E o problema da precisão
'''Essa versão funciona pois os inteiros pequenos envolvidos aqui tëm representação exata em número de ponto flutuante. Podemos
evitar o risco de problemas de precisão evitando o uso de ponto flutuante nas operações:'''

for a in range(1, 1000):
    b = (500 * (1000 - 2 * a)) // (1000 - a)
    c = 1000 - a - b
    if a ** 2 + b ** 2 == c ** 2:
        break
print(f'a = {a}, b = {b}, c = {c}')


