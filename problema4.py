#achando os números primos para n
n = int(input())
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?


L = [2]
j = 2
a = True
b = True
l = []

for i in range(3,n+1):
  while j < i:
    if i % j !=0:
      a = True
      j += 1
    else:
      b = False
      j += 1
  if a == True and b == True:
        L.append(i)
        j = 2
  else:
    j = 2
    a = True
    b = True
        
for i in range(len(L)):
  if n % L[i] == 0:
    l.append(L[i])
print(l)


#forma otimizada
n = int(input())

def is_prime(n):
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      return False
  return True

for i in range(2, n+1):
  if is_prime(i) and n % i == 0:
    print(i)
