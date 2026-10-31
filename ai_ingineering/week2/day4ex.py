import pandas as pd
import numpy as np

#create sample dataset
data={
    "name":['Alice','Bob',np.nan,"david"],
    "Age":[23,np.nan,30,32],
    "score":[85,90,np.nan,88]
}
df=pd.DataFrame(data)
#print("Original:\n",df)

df['Age']=df['Age'].fillna(df['Age'].mean())
df['score']=df['score'].interpolate()
#print(df)
df=df.rename(columns={"name":"Student_Name"})
print(df)


df1=pd.DataFrame({
    "ID":[1,2,3],
    "Name":["Aba","Raba","Kaba"],
    "Color":["Red","Green","Blue"],
    "Age":[34,24,32]
})
df2=pd.DataFrame({
    "ID":[1,2,3],
    "Score":[89,78,79]
})
merged=pd.merge(df1,df2,how='inner',on="ID")
print(merged)
merged['score_presentage']=(merged['Score']/200)*100
print(merged)

dfd=merged[merged["score_presentage"]>=39]
dfd=pd.get_dummies(dfd,columns=["Color"],dtype=int)
print(dfd)