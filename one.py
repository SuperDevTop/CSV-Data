
# student satisfaction 40 universities
import pandas as pd

df = pd.read_csv('uni_dataset.csv')
df = df.drop('Index',axis=1)

df['Student satisfaction'] = df['Student satisfaction'].str.slice(0, -1, 1).astype(int)

# print(df)
temp = df.sort_values(['Student satisfaction'], ascending=False)
print(temp.head(40))


#--------------------------------------------------------#
# where the specific college is among 40 universities
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


#-------------------------------------#
# how many universiteis have satisfaction of over 85%
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


#----------------------------------------#
# arrange universities by names
import pandas as pd

df = pd.read_csv('uni_dataset.csv')
df = df.drop('Index',axis=1)

# New column which is to save the names of universities by ignoring start with sth 
temp_list = []
temp_index = []

for i in range(len(df)):
    temp_index.append(i)

     # if the name of the university includes 'University of' and it dosen't come at the first position
    if df.iloc[i].values[0].find('University of') != -1 and df.iloc[i].values[0][0] == 'U':  
        temp_list.append(df.iloc[i].values[0][14:]) 
    else:       #if the name of the univesity doesn't include university of
        temp_list.append(df.iloc[i].values[0]) 

# Add new column
df['new'] = pd.Series(temp_list, temp_index)

# For upper-case
df['new'] = df['new'].str.upper()

# Sort data
df = df.sort_values('new')

# Print the result(without 'new' column)
print(df[['University name', 'Overall score', 'Entry standards', 'Student satisfaction', 'Research quality',
          'Research intensity', 'Graduate prospects']])



