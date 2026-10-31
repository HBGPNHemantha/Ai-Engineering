import pandas as pd

#load dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
#print(f"first 5 rows: \n{df.head()}")
#print(f"last 5 rows: \n{df.tail()}")
#print({df.info()})
#print(df.describe())

select_columns =df["species"] 
#print(select_columns)
sel2=df["species"][df["sepal_width"]>3.4]
print(sel2)
