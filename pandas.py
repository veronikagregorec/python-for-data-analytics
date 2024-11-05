# Pandas

# Reading in Files
import pandas as pd

df = pd.read_csv(r"C:\....csv", index=False)
df

df = pd.read_table(r"C:\....txt")
df

df2 = pd.read_excel(r"C:\....xlsx", sheet_name = 'Sheet2')
df2

df2.info()
df2.shape
df2.head(10)
df2.tall(10)
df2.iloc[224]
df2.loc('Rank')

df = pd.read_json(r"C:\....json")
df

pd.set_option('display.max.rows', 235)
pd.set_option('display.max.columns', 40)

# Filtering and orders
df = pd.read_csv(r'C:\....csv')
df[df['Rank'] <= 10]

specific_countries = ['Brazil', 'Moscow']
df[df['Country'].isin(specific_countries) ]

df[df['Country'].str.contains('United') ]

df2 = df.set_index('Country')
df2.filter(items = ['Continent', 'CCA3'], axis = 0)
df.loc['United States']
df.iloc[3]

df[df['Rank'] < 10].sort_values(by=['Continent', 'Country'], ascending=[False, True])

# Indexing
df = pd.read_csv(r"C:\....csv", index_col='Country')
df

df.reset_index(inplace=True)
df

df.set_index('Country')
df.iloc[8]

df.reset_index(inplace = True)
df.set_index(['Continent','Country'],inplace = True)
df.sort_index()
pd.set_option('display.max.columns', 235)
df.loc('Africa', 'Angola')

# Group by and Aggregating
df = pd.read_csv(r"C:\....csv", index_col='Country')
df

df.groupby('Base Flavor').mean()
df.groupby('Base Flavor').count()
df.groupby('Base Flavor').min()
df.groupby('Base Flavor').max()
df.groupby('Base Flavor').sum()
df.groupby('Base Flavor').agg({'Flavor Riting': ['mean','max','count','sum']})

df.groupby(['Base Flavor', 'Liked']).agg({'Flavor Riting': ['mean','max','count','sum']})

df.groupby('Base Flavor').describe()

# Merge and Concatenate
df1 = pd.read_csv(r"C:\....csv")
df1

df2 = pd.read_csv(r"C:\....csv")
df2

df1.merge(df2, how = 'inner', on = ['FellowshipID', 'Firstname'])
df1.merge(df2, how = 'outer')
df1.merge(df2, how = 'left')
df1.merge(df2, how = 'right')
df1.merge(df2, how = 'cross')

pd.concat([df1,df2], join = 'inner', axis =1)

# Visualization
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\....csv")
df.set_index('Date')
df

print(plt.style.available)
plt.style.use('classic')

df.plot(kind = 'line', title = 'Ice Cream Ratings', xlabel = 'Daily Ratings', ylabel = 'Scores')
df['Flavor Rating'].plot(kind = 'bar', stacked = True)
df.plot.barh(stacked = True)
df.plot.scatter(x = 'Texture Rating', y = 'Overall Rating', s = 500, c = 'Yellow')
df.plot.hist(bins = 20)
df.boxplot()
df.plot.area(figsize = (10,5))
df.plot.pie(y='Flavor Rating', figsize = (10,10))

# Data Cleaning
df = pd.read_excel(r"C:\....xlsx")
df.drop_duplicates()
df

df.drop(columns = 'Not_Column')
df

df['Last_Name'].str.strip("123._/")
df

df['Phone_Number'].str.replace('[^a-zA-Z0-9]', '')
df['Phone_Number'].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:9])
df['Phone_Number'].str.replace('nan--', ' ')
df['Phone_Number'].str.replace('Na--', ' ')

df[['StreetAddress', 'State', 'Zip_Code' ]] = df['Address'].str.split(',',2,expand = True)

df['Paying Customer'].str.replace('Yes', 'Y')
df['Paying Customer'].str.replace('No', 'N')

df = df.fillna('')
df

# blank rowws
for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == 'Y':
        df.drop(x, inplace=True)

df

df.reset_index(drop=True)
df