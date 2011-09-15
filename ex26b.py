"""  
A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with denominators 2 to 10
are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring
cycle in its decimal fraction part.

"""

def ex(limit):
    n=1.0
    largest=['',0]
    for i in range(2,limit+1,1):
        d=float(i)
        res=float(n/d)
        print str(n)+'/'+str(d), '0.'+period(res) 
        if len(largest[0])<=len(period(res)):
            largest[0]=period(res)
            largest[1]=i
    print largest

def period(s):
    mod=''
    s=str(long(s*(10**17)))
    
    while s[-1]=='0':
        s=s[:-1]
    print s
    for i in range(0,len(s)-1,1):
      #test('mod',mod) #
      if s[i]==s[i+1]:
          s=s[:i]+'('+s[i]+')'
          break
      if s[i:].count(s[i])>1:
          mod=s[i:s[i:].index(s[i])]
          if s.count(mod+mod)>0:
              s=s[:s.index(mod)]+'('+mod+')'
              break
      
 #     if mod==s[i+1:i+1+len(mod)]:
 #         s=s. +'('+str(mod)+')'
 #         break
     # test('i',i) #
     # test('s',s) #
    return s
