# loc[]-> he loc() function is used to select the data
# which means that we have to pass the name of the row or column which we want to select
# also we pass the conditon to select the data
# also we change the values in dataframe using loc

#setting the values in the dataframe
import pandas as pd
mydf=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
mydf.columns=list("abc")                          #setting thhe columns name is a,b,c

 #lets learn the loc[]
mydf.loc[0,'a']=1018                              #changing rows 0th element and column 0th element is 1018
                                                  #this is right way to change values

# newdf=mydf.drop(1,axis=0)                         #drop second row(index number=1)

print(mydf.loc[[0,2],['b','c']])                 #printing 1,2 rows and b,c colume only
                                                 #select multiple rows and multiple column

v=mydf.loc[(mydf['a']>3)]                        #return only those rows and column which
                                                 # a column have greater than 3 value

print(mydf['b'][1])                              # b colume 1th row value

print(mydf.loc[:,:])                            #printing all rows and all values
