import pandas as pd
# implace=True- we chnage the data frame temporary
# if you want to save the changes permonantly
# write implace=True
#if you dont want to save changes write iplace=False


df = pd.DataFrame({'col1':[1,2,3,4],
                   'col2':[444,555,666,444],
                   'col3':['abc','def','ghi','xyz']})

a=df[(df['col1']>2)]              #retun a all rows in which column1 have values more than 2

B=[(df['col2']==444)]            #return the all rows in which column3 have values eaqal to 444

#____________apply a function on dataframe values
def double_123(x):
    return x*2
c=df['col1'].apply(double_123)    #applying the double function on column1 values


d=df['col3'].apply(len)           #applying the len() functions on column3

del df['col1']                    #delelting the column1

e=df.sort_values(by='col2',ascending=True,inplace=False)                 #sorting the column values

f=df.isnull()                    #return the true if there is null value otherwise return False

