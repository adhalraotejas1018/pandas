import pandas as pd

dict1={'col1':[1,2,3,4],
       'col2':[444,555,666,444],
       'col3':['abc','def','ghi','xyz']
       }

df = pd.DataFrame(dict1)

a=df['col1'].nunique()   #return a number of  totoal unique values
b=df['col1'].unique()    #retirn the unique numbers

x=df.dropna()                     #drop NA values row in the table

y=df.dropna(axis=1)               #drop NA values column in table

c=df.fillna(value=1018)             #fill all NA values as 1018

d=df['col1'].mean()                   #find the mean of the a column