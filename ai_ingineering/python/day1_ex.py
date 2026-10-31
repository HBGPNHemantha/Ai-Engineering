import math
num=int(input('Enter the number: '))
if num>1:
    for i in range(2,int(math.sqrt(num))+1):
        if num % i==0:
            print("Not a prime")
            break
    else:
        print("prime")
else:
    print("not a prime")
    
