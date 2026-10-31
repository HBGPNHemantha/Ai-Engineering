#[expression for item in iterable if condition]

#create a listh of squares
#squares=[x**2 for x in range(10)]
#print (squares)

#filter even numbers

#even = [x for x in range(10) if x % 2 ==0]
#print(even)

#lambda fuction
#lambda argument expression
#add=lambda x,y:x+y
#print(add(3,4))

#mapping
#num=[1,2,3,4]
#squ=map(lambda x:x**2,num)
#print(list(squ))

#filter
#evenlist =filter(lambda x:x % 2 ==0,num)
#print(list(evenlist))

#rediuse
#from functools import reduce
#product=reduce(lambda x,y:x*y,num)
#print(product)


#os and sys module
import os
print(os.getcwd())
#os.mkdir("test.txt")
#os.remove("test.txt")

import sys
print(sys.argv)
print(sys.version)