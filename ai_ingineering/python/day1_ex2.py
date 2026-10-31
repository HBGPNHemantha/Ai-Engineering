import math
def add (a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b !=0:
        return a/b
    else:
        print("Unable to divide by Zero")
while True:

    print("\nMenu\n:")
    print('''
    1.Addition
    2.Substraction
    3.Division
    4.Multiplication
    5.Exit
    ''')
    cho=input("Select the Operation: ")
    
    if cho=='5':
        print("Operation Terinated..")
        break

    if cho in ['1','2','3','4']:
        num1=float(input("Enter the num1: "))
        num2=float(input("Enter the num2: "))
        
        if cho=='1':
            print(f"{num1} + {num2} = {add(num1,num2)}")
        elif cho=='2':
            print(f"{num1} - {num2} = {sub(num1,num2)}")
        elif cho=='3':
            print(f"{num1} / {num2} = {div(num1,num2)}")
        elif cho=='4':
            print(f"{num1} * {num2} = {mul(num1,num2)}")
    else:
         print("Invalid Choosen,Please try again")