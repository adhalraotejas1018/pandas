import pandas as pd

dict1={
    'a':[1,2,0,4,5,0],
    'b':[6,7,0,8,9,0],
    'c':[1,2,3,4,10,18]
}

df=pd.DataFrame(dict1)
# print(df)

v=df.drop_duplicates(subset=['a'] ,keep='first')   #it drop the rows in column a which have duplicate values keep only first record

a=df['a'].isnull()                                 #in column a id f there is null value it return True and othewise it return false

c=df.shape                                         #shows shape of data frame (row,column)

b=df.info()                                        #inforamation columnes name,class name


