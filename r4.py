import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],                                #creating the dataframes with indexes
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],                                #creating the dataFrames by indexs
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4,5,6,7])


a=pd.concat([df1,df2])                #add two table rows means add table vertically
b=pd.concat([df1,df2],axis=1)        #add two table columns means add table horizontally


#-------------------------------------******************************------------------------------------
v1 = pd.DataFrame({'sr_no': ['K0', 'K1', 'K2', 'K3', 'K4'],
                      'A': ['A0', 'A1', 'A2', 'A3', 'A4'],
                      'B': ['B0', 'B1', 'B2', 'B3', 'B4']})

v2 = pd.DataFrame({'sr_no': ['K0', 'K1', 'K2', 'K3', 'K5'],
                       'C': ['C0', 'C1', 'C2', 'C3', 'C5'],
                       'D': ['D0', 'D1', 'D2', 'D3', 'D5']})

c=pd.merge(v1,v2, how = 'inner')                              #merge the two tables


