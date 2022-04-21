#para 3 dígitos
def prod_number(dig):
  L = []
  for i in range(999,101,-1):
    for j in range(999,101,-1):
      c = i*j
      if is_pal(c):
        L.append(c)
  return max(L)
  

def is_pal(number):   
  number = str(number)
  copy = number[::-1]

  if number == copy:
    return True
    
print(prod_number(3))
