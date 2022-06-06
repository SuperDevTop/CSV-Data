import pandas as pd

df = pd.read_csv('uni_dataset.csv')
df = df.drop('Index',axis=1)

# Remove the last letter(%), convert string to int
df['Student satisfaction'] = df['Student satisfaction'].str.slice(0, -1, 1).astype(int)

# The result of Sorting algorithm
temp = df.sort_values(['Student satisfaction'], ascending=False)

univesity = input('Enter the name of university you\'re finding:')

# Flag for existence
bFound = False

for i in range(40):
    if temp.iloc[i].values[0]== univesity:
        print("Found: Order {0}".format(i + 1))
        bFound = True

if bFound is False:
    print("Not Found")