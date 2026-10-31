#datatypes
intv=10
fltv=10.11
strn="hi  Ai"
lst=[1,2,3]
tuplev=(4,5,6,3)
dist={"amma","thaththa"}
boolv=True

print(intv,"\n",fltv,strn,"\n",lst,"\n",tuplev,"\n",dist,"\n",boolv)
print("\n---------------\n")

#conditions
if intv>0:
    print("positive")
elif intv==0:
    print("zero")
else:
    print("negative")
print("\n---------------\n")

if intv>0:
    if intv>9:
        print("grater than 9")
    else:
        print("less than 9")
elif intv==0:
    print("zero")
else:
    print("negative")
print("\n---------------\n")

#loops
for num in lst:
    print(num)
print("\n---------------\n")

#with range
for i in range(5):
    print(i)
print("\n---------------\n")

#while loop
count=5
while count>0:
    print(count)
    count -=1
print("\n---------------\n")
for i in range(10):
    if i==5:
        break
    print(i)
print("\n---------------\n")
for i in range(10):
    if i==5:
        continue
    print(i)