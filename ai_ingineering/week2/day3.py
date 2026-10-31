import pandas as pd
s=pd.Series([10,20,30],index=['a','b','c'])
#print(s)

data = {"Name":["Ali","Bob"],"Age":[13,24]}
#print(data)
df = pd.DataFrame(data)
#print(df)

#read data from csv file
#df=pd.read_csv('data.csv')
#read data from excel
#df=pd.read_excel('data.xlsx')

#save data into csv file
df.to_csv("data.csv",index = False)
dd=pd.read_csv("data.csv")
#print(dd)


#basic dataframe operations
#print(dd.head()) #display 1st 5 records
#print(dd.tail(3)) #display last tree records
#print(dd.describe()) #display statistical summary
#print(dd[["Name"]]) #display only wanted columns

#print(df[df["Age"]>15])#filter rows

#selecting by perticular position
print(dd.iloc[0])#first row by the posiition
print(dd.iloc[:,0])#first column by position