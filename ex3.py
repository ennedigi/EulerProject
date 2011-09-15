##### EX3
#Find the largest prime factor of a composite number.

# Get the prime numbers less than a given num
def prim(x):
  l=[]
  for i in range(2,x,1):
    for j in range(1,x,1):
      prime=True
      if not i%j and not (j==1 or j==i):
         prime=False
         break
    if prime: l.append(i)
  return l

# Get the prime factors of a given number

def primeFact(x):
  l=[]
  for i in prim(x):
    if not x%i: l.append(i)
  return l


###########WHILE version

# Get the prime numbers less than a given numdef prim(x):
  l=[]
  i=2
  j=1

  while i < x:
    while j <x:
      prime=True
      if not i%j and not (j==1 or j==i):
         prime=False
         break
      j+=1
    if prime: l.append(i)
    i+=1
  return l

# Get the prime factors of a given number

def primeFact(x):
      l=0
      for i in prim(x):
        if not x%i: l=i
      return l

