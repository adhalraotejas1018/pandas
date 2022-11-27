import pandas as pd

#creating the data frames
dict1={
    'maths':[98,99,82,91,78],
    'chemistry':[97,99,87,72,65],
    'physics':[97,82,98,68,55]}

df = pd.DataFrame(data=dict1)                #creating data frame
# print(df)                                    #printing the data frames
# print(df['maths'])                           #printitng maths colume only
# print(df[['maths','chemistry']])               #printing the aths and chemistry column

#creating a column totoal marks
# df["total_marks"]=df['maths']+df['chemistry']+df['physics']
df['names']=['Amit', 'Smith', 'Allen', 'Kathy', 'John']

#delelte a colume axis=1 for column
# df.drop('Total', axis=1)

#delete a row  axis=0 for rows
# df.drop(4,axis=0)



# df['marks]'>80 this condition apply in df[]
v=pd.DataFrame(df[df["maths"]>80])                 #return records which have 80+ marks in maths
print(v)
