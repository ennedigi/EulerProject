#EX6
import math

def sqr1(limit):
    tot=tot2=0
    i=1
    while i<=limit:
        tot+=i**2
        tot2+=i
        i+=1
    tot2=tot2**2
    print tot,tot2
    return tot2-tot

