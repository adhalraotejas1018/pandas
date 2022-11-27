#creating the dataFrames
# dataFrames- it is two diamensioanal data structure with column and rows
# it like a xl sheet
#which store rows and one or more column

import pandas as pd
dict1={                                                            #creating the dictoonary
    "names":["RutVik","ViRat"],
    "marks":[10,18],
    "city":["pune","mumbai"]
     }
df=pd.DataFrame(dict1)                                             # DataFrame -> convert the data into data frame,(means like a xL sheet ,table format)
print("printing the table df  \n ",df)


#another way to create a dataframe with index
df1=pd.DataFrame({'Name':['Tom', 'nick', 'krish', 'jack'],
        '         Age':[20, 21, 19, 18]},
                  index=["first","second","third","fourth"])                 #setting the index to dataframe
print("printing the table df1 \n ",df1)


#another way to create a dataFrames
dict123={"Virat":[1,2,3,4],
         "RutVik":[1,0,1,8]}
df2=pd.DataFrame(data=dict123)
print("printing the table df2 \n ",df2)