#concadinate
#fst="Hello"
#seo="World"
#res=fst+" "+seo

#print(res)

#split
#tst="Python pro"
#print(tst[0:6])
#print(tst[-9:])

#sent="I love python"
#words=sent.split() #break sentence into words
#print(words)

#up_sent = "|".join(words) #join the words
#print(up_sent)

#rep=sent.replace("python","ML") #replace the words
#print(rep)

#tst="    Hello World!   "
#mt=tst.strip() #remove the spaces 
#print(tst)
#print(mt)


#regular expressions
#import re
#txt="Contact me: 011-451-6379"

#dgt=re.findall(r"\d+",txt)
#print(dgt)

#uptxt=re.sub(r"\d","X",txt)
#print(uptxt)

import re

user=input("Enter the string here: ")

def cleaned(text):
#remove punctuation
    text=re.sub(r"[^\w\s]","",text)

    #remove extra spaces
    text=" ".join(text.split())

    #convert to lover case
    return text.lower()

#print(f"cleaned text: {cleaned(user)}")
#print(f"\ncleaned text: {cleaned(user).upper()}")

#check palindrome
def is_pal(text):
    text="".join(char.lower() for char in text if char.isalnum())
    return text==text[::-1]

if is_pal(user):
    print(f"{user} is palindrome")
else:
    
    print(f"{user} is not palindrome")