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

pd.set_option('display.max_rows', None)
# Print the result(without 'new' column)

print(df[['University name', 'Overall score', 'Entry standards', 'Student satisfaction', 'Research quality',
          'Research intensity', 'Graduate prospects']])



