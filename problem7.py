#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
#that the 6th prime is 13.
#What is the 10 001st prime number?

n = 3
L = []

def is_prime(n):
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      return False
  return True

while len(L) < 10000:
  for i in range(2, 1000000):
    if not is_prime(i):
      continue
      n +=1
    else:
      L.append(i)
      n +=1

print(L[10000])
