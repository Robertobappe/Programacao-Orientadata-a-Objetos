#Smallest multiple
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def divisivel(n):
  L = [i for i in range(1,21)]
  for i in range(20):
    if n % L[i] != 0:
      return False
  return True

n = 1

while True:
  if divisivel(n):
    break
  n += 1

print(n)
