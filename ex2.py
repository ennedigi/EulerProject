# By considering the terms in the Fibonacci sequence whose values do not exceed four    
# million, find the sum of the even-valued terms.

def fib(x):
    if x==0: return 1
    elif x==1: return 1
    else: return fib(x-2)+fib(x-1)

s=[fib(i) for i in range(35) if fib(i)<4000000 and (fib(i)%2)==0]

sum=0

for i in s:
    sum+=i



