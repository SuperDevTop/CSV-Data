from itertools import count
import pandas as pd

df = pd.read_csv('uni_dataset.csv')
df = df.drop('Index',axis=1)

# counts of universities
count = 0

# Remove the last letter(%), convert string to int
df['Student satisfaction'] = df['Student satisfaction'].str.slice(0, -1, 1).astype(int)

# Sorting algorithm
for i in range(len(df)):
    if df.iloc[i].values[3] >= 85:
        count += 1

print("Count of universities that have satisfaction of over 85%: {0}".format(count))