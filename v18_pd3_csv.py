# csv file- csv stand for COMMA SEPRATED VALUES
# store dataFrames in csv file

import pandas as pd
dict1={                                                         #creating the dictoonary
    "names":["RutVik","ViRat","Sneha"],
    "marks":[10,18,21],
    "city":["pune","mumbai","Nagpur"]
     }

df=pd.DataFrame(dict1)                                          #creating the dataFrame
print(df)

df.to_csv("z1.csv")                                            #create student.csv file and stored df  in it data
# df.to_csv("z1.csv",index=False)                        #remove the index from csv file