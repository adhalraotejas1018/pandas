#reading the csv file or  change dataframes

import pandas as pd
a=pd.read_csv("z2.csv")
print("printing the csv file \n",a)

print("printitng the marks column only -> \n ",a["Runs"])                               #printing only single column with name

# a["marks"][0]=1018                                                                    #changing ther value of marks column which is at 0th position

# a.index=["first","second","third","fouth","fifth"]                                    #setting the index values as first,second,third

print("printing first two rows\n",a.head(2))                                            #print or shows starting 1 rows
print("printing last two rows \n",a.tail(2))                                            #print or shows ending  1 rows

print("describing the numberical column\n",a.describe())                                #shows mean,mode,min max etc. of numberical column in data frame
