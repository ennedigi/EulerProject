##2520 is the smallest number that can be divided by each of the
#numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly
#divisible by all of the numbers from 1 to 20?

def ex5(n):
    t=2
    
    while True:
        #consider that all the even numbers are div for 1 and 2 
      for i in range(3,n+1,1):
        if t%i: break
        else:
            if i==n: return t
      t+=2
      
print ex5(20)
