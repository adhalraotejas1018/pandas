# method is used when the index label of a data frame is something other than numeric series of 0, 1, 2, 3…
# The iloc property gets, or sets, the value(s) of the specified indexes.
# iloc[] - in ilic we search only using index numbers
import pandas as pd

data = [[2, 4],
        [3, 9],
        [4, 16]]

df = pd.DataFrame(data)
print(df.iloc[1, 0])