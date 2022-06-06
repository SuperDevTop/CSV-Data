import pandas as pd

df = pd.read_csv('uni_dataset.csv')
df = df.drop('Index',axis=1)

df['Student satisfaction'] = df['Student satisfaction'].str.slice(0, -1, 1).astype(int)

# print(df)
temp = df.sort_values(['Student satisfaction'], ascending=False)
print(temp.head(40))
# for i in range(len(df)):
#       temp = df.iloc[i].values[3]
#       print(temp)
# lst = []
# print(len(df))
# for x in range(len(df) - 1):
#   lst.append(tuple(df.iloc[x].values))


# labels = df.columns.values
# print(lst[10])


# print(df.head(40))
# print(df.sort_values(['Student satisfaction']))
