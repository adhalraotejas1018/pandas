# series- series is one diamensional array
#which store one row or column

import pandas as pd
list = [1,2,3,4,5]                       ## a simple int list
sr = pd.Series(list)                   # create series form a int list
print("printing series sr \n ",sr)

#another way to  create seires
sr1=pd.Series([1,2,3,4,5,6,7,8,9])
print("type of series sr -> ",type(sr))
print("printing series sr \n ",sr1)

#creating the series
list1=[1,2,3,4]                                     #creating the list
s1=pd.Series(data=list1)                             #creating series syntax data=list,array,dict
print(s1)
# print("data type of s1 ",s1.dtype)                  #printing the type of series

#create serires with index
labels = ['a','b','c']                               #create index name what u want
my_list = [10,20,30]
s2=pd.Series(data=my_list,index=labels)
print(s2)


#create a series with dictonary
d = {'a':10,'b':20,'c':30}                           #creating the dictionary
s3=pd.Series(d)                                       #series
print(s3)