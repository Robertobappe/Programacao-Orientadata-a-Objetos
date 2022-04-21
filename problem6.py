#The sum of the squares of the first ten natural numbers is,
# 1²+2²+...+10² = 385
#T1he square of the sum of the first ten natural numbers is,
#(1+2+...+10)² = 55² = 3025
#Hence the difference between the sum of the squares of the first
#ten natural numbers and the square of the sum is
#3025 - 385 = 2640.

#Find the difference between the sum of the squares of the first one
#hundred natural numbers and the square of the sum.

n = int(input())
a = 0
b = 0

for i in range(1, n+1):
  a += i
  b += i**2
a = a**2

c = a - b

print(c)
