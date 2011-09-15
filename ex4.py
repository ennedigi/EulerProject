#Exercise 4
#A palindromic number reads the same both ways.
#The largest palindrome made from the product
#of two 2-digit numbers is 9009 = 91  99.

#Find the largest palindrome made from the product of two 3-digit numbers.


class ex4():

    def __init__(self):
        self.two_digits=100
        self.three_digits=1000
        self.four_digits=10000

    def isPalidrome(self,num):
        '''Check whether a num or string (num) is palidrome'''

        num=str(num)
        half=int(len(num)/2)

        for i,j in enumerate(range(-1,(half*-1)-1,-1)):
          #print '\tposizioni', i,j
          #print '\t',num[i],num[j]
          if not num[i]==num[j]:
            return False
        return True
            
    def maxPal(self,n):
        '''Retrieve the biggest palidrome number given a number of digits'''
        n_pal_max=(0,0,0)
        for i in range(1,n+1,1):
          for j in range(1,n+1,1):
            if self.isPalidrome(i*j)==True:
                n_pal=i*j
                if not n_pal<n_pal_max[0]:
                    n_pal_max=(n_pal,i,j)
        
        return n_pal_max 



    def maxPal_OPTIMIZED(self,n):
        '''Retrieve the biggest palidrome number given a number of digits'''
        for i in range(n-1,1,-1):
          for j in range(n-1,1,-1):
            if self.isPalidrome(i*j)==True:
                print i,j
                return i*j 

a=ex4()
print a.maxPal(a.three_digits)

#print a.maxPal_OPTIMIZED(a.three_digits)
