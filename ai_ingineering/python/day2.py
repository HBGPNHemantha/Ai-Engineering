# function
# def hi():
    # v='Hello pasindu'
    # print(v)
# hi()
#print(v)#unable to print because its not global

# v2="Hey "
# def fun():
    # print(v2+"inside the function")
# fun()
# print(v2,"outside the function")#able to print v2 is global
#

#exersize1 fact
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fact(n-1)
def print_fact(n):
    res=fact(n)
    print(f"value :{res}")

