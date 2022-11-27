#setting the rows and column names
import pandas as pd
dict1 = {                                           #creating the dictionary
    "Rutvik": [10, 2, 3, 4, 5],
    "ViRat": [4, 5, 6, 7, 8],
    "Swaraj": [2, 3, 1, 4, 5],
    "ViRaj": [2, 8, 9, 9, 8],
    "ViRu": [1, 0, 1, 8, 0]
}

df = pd.DataFrame(data=dict1)                       # creating the dataFrame

df.index = [1, 2, 3, 4, 5]                          # setting rows name 1,2,3,4,5
df.columns = ['a', 'b', 'c', 'd', 'e']              # setting column name a,b,c,d

print(df['b'][4])                              # b colume 4th row value
print(df)
