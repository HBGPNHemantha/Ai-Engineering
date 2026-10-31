#with open ("sample.txt","w") as file:
    #content=file.readlines()
    #print(content)
  #  file.write("Hello, world")
   # file.writelines([" kasun","akas","dasun"])

#with open("sample.txt","r") as file:
 #   print(file.readlines())
    
#basic handliing for file exception
#try:
 #   with open ("sample1.txt","r") as file:
#        print(file.readlines())
#except:
 #   print("Not Found File")


#exersize  count the No of lines and words in the file
def count_words_and_lines(filename):
    try:
        with open(filename,"r") as file:
            lines=file.readlines()
            line_count=len(lines)
            word_count=sum(len(line.split()) for line in lines)

            print(f"num of lines: {line_count}")
            print(f"num of words: {word_count}")
    except:
        print(f"not found the {filename}")
count_words_and_lines("sample.txt")


#exersize 2 read from the list
def write_item(filename,items):
    with open(filename,"w") as file:
        for item in items:
            file.write(item+"\n")
def read_item(filename):
    try:
        with open (filename,"r") as file:
            items=file.read()
            print(items)
    except:
        print("File not found")

fruits=["apple", "bababa","mango","grapes"]
write_item("fruits.txt",fruits)
read_item("fruits.txt")