from math import sqrt
import random
import numpy as np
import sys
import string

import pandas as pd

sys.setrecursionlimit(10**6)
ungroup = []
identifiers = list(string.ascii_letters)
n = 0
#print(identifiers)
#reading the data source into a list.
read = open("inputs/a.in", "r")
for line in read:
    row = list(map(int, line.strip().split(" ")))
    n = len(row)
    ungroup.append(row)

print("The Ungrouped array")
print(np.array(ungroup))
a = np.array(ungroup)

ungroup_Dataframe = pd.DataFrame( np.array(ungroup), dtype=float, index=identifiers[:n], columns=identifiers[:n], )

#row_order = [1, 2, 1]
#ungroup.sort(key=row_order)
row_order = []
column_order = {}

#rows
for i in ungroup_Dataframe.values:
    #print(i, max(i))
    row_order.append(max(i))
    

ungroup_Dataframe["row_order"] = row_order



#columns
for y in ungroup_Dataframe.columns:
    if y != "row_order":
        column = ungroup_Dataframe[y].tolist()
        column_order[y] = max(column)
        #print(column, max(column))
# for i in ungroup_Dataframe.columns:
#     print(ungroup_Dataframe[i])
#ungroup.identity(2, dtype = float)
ungroup_Dataframe["column_order"] = column_order

print(ungroup_Dataframe)

#scolumn = sorted(list(column_order.items), key=lambda x:x[1], reverse=True)
scolumn = {k: v for k, v in sorted(column_order.items(), key=lambda x: x[1], reverse=True)}
print(scolumn)
c_order = [z[0] for z in scolumn]

print("Sorting and Rearranging Rows")
ungroup_Dataframe = ungroup_Dataframe.sort_values(by=["row_order"], ascending=False)
print(ungroup_Dataframe)

print("Sorting and Rearranging Columns")
ungroup_Dataframe = ungroup_Dataframe[c_order]
print(ungroup_Dataframe)




""" n = 2
df = pd.DataFrame(np.random.rand(10,15))
old_cols = df.columns.tolist()
old_index = df.index.tolist()

# Prepend rows: Create n rows and append existing df to this
df1 = pd.DataFrame(np.zeros(shape=(n, df.shape[1])),
             index=[chr(97+x) for x in (range(n))],
             columns=old_cols)
df1 = df1.append(df)

# This was slower
#df2 = pd.DataFrame(np.zeros(shape=(df1.shape[0],n)),
#             index=df1.index,
#             columns=[chr(97+x) for x in (range(n))])
#df_final = pd.concat([df2,df1], axis=1)

# Create n columns and set to zeros
for i in range(n):
    df1[chr(97+i)] = 0

# Reindex coluns in correct order
df1 = df1[[chr(97+x) for x in (range(n))] + old_cols]

# Assign identity to the top left corner
df1.iloc[:n,:n] = np.identity(n)

print(df1) """