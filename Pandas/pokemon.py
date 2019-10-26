# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
import pandas as pd

df = pd.read_csv('pokemon_data.csv')

df.head(5)


# %%
df[['Name', 'HP', 'Speed']][0:4]


# %%
df.iloc[3]


# %%
df.iloc[2,1]


# %%
df.loc[df['Type 1'] == "Fire"]


# %%
df.describe()

# %% [markdown]
# # Sorting Data

# %%
df.sort_values('Name', ascending = False)


# %%
df.sort_values(['HP','Name'], ascending = [0,1])  #[false, true]

# %% [markdown]
# # Making Changes in Data

# %%
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

df.sort_values(['Total'] , ascending = False)


# %%
df = df.drop(columns= ['Total'])

df.head(5)


# %%
df['Total'] = df.iloc[:, 4:10].sum(axis = 1)


cols = list(df.columns)
# df = df[cols[0:4] + [cols[-1]] + cols[4:12]] 
# running this multiple time will be a mess 

df.head(7)


# %%
df.to_csv('modified.csv', index = False)
df.to_csv('modified.txt', index = False, sep ='\t')

df

# %% [markdown]
# # Filtering

# %%
new_df = df.loc[(df['Type 1'] == 'Fire') & (df['Type 2'] == 'Flying') | (df['HP'] > 200)]

new_df.reset_index(drop = 1, inplace = True)

new_df


# %%
df.loc[~df['Name'].str.contains('Mega')]


# %%
import re

df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]


# %%
df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]

# %% [markdown]
# # Conditional Changes

# %%
df.loc[(df['Total']>600) & (df['Legendary']==True),  'Legendary'] = 'Hell Yeah True'

df.loc[df['Legendary'] == 'Hell Yeah True']

# %% [markdown]
# # Aggregate Statics

# %%
df.groupby(['Type 1']).mean().sort_values('HP', ascending = False)


# %%
df.groupby(['Type 1']).count()['#']

# %% [markdown]
# 
# # Working With Large Files

# %%
for df in pd.read_csv('pokemon_data.csv', chunksize = 10):
    print("\nChunk DF\n")
    print(df)


# %%


