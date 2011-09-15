#ex 7
import math

def prim(n):
	lista_prim=[2]
	j=1
	p=3

	while j<n:
	  prime=True
	  for t in range(3,p,1):
	    if not p%t:
	      prime=False
	      break
	  if prime:
	    lista_prim.append(p)
	    j+=1
	  p+=2
	return lista_prim[-1]

