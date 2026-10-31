#handling missing values
import pandas as pd
data={
    "Name":['Kasun','Dasun','Pasun','Masun','Sasun'],
    "Age":[23,34,24,32,28],
    "Marks":[67,55,76,87,75],
    "Address":['Kurunegala','Jaffna','','Vavuniya','Anuradapura']
}
df=pd.DataFrame(data)
#print(df)
df.to_csv("student.csv",index=False)
#print(df.head())#remove rows with missing val
df = df.dropna(axis=1)#remove col with missing val
#print(df)

#df["column_name"] = df["column_name"].fillna(0)#fill missing val using 0
df.ffill()#fill missing val using before value the missing val
df.ffill()#fill missing val using after val 
#df['column_name']=df["column_name"].interpolate()#fill missing val after cal culating (60,-,80 then missing is 70)

#data transformations
#renaming columns
df = df.rename(columns={"Age":"Student_Age"})#oldname : newname
print(df.columns)
#df['Marks']=df['Marks'].astype("float")
print(df.dtypes)
#df['column_name']=pd.to_datetime(df['column_name'])#convert datatype into date time

#changing data types#creating or modifing columns
df['Sci_marks']=df['Marks']*2-80#df['new_col']=df['existing_col']*2 aluth col ekk haduwa parana ekakata aluth val dala
#print(df)


combined = pd.concat([df1,df2],axis=0)#row widiyata combined karanaw
combined = pd.concat([df1,df2],axis=1)#col widiyata combined karanawa
merged = pd.merge(df1,df2,on="common_column")#common colmuun eken join karanawa
merged=pd.merge(f1,df2,how ="left",on='common_column')
merged = pd.merge(df1,df2,how="inner",on="common_column")
joined = df1.join(df2,how='inner')