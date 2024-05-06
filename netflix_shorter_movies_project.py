import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the .csv in a Pandas DF
df = pd.read_csv('netflix_data.csv')
print(df.head())

# Check the length of the dataset
print(len(df))
print(df.shape)

# Filter only on Movies and keeping the relevant columns
netflix_subset = df.loc[df['type'] == 'Movie']
netflix_movies = df.loc[df['type'] == 'Movie', ['title', 'country', 'genre', 'release_year', 'duration']]

# Are there genres that tend to be shorter?
short_movies = netflix_movies[netflix_movies['duration'] < 60]

print(short_movies['genre'].value_counts())

'''
Documentaries           151
Children                107
Stand-Up                 72
'''

# Let's iterate through the df and assign a color to those specific genres
colors = []
for label, row in netflix_movies.iterrows():
  if row['genre'] == 'Children':
    colors.append('red')
  elif row['genre'] == 'Documentaries':
    colors.append('yellow')
  elif row['genre'] == 'Stand-Up':
    colors.append('green')
  else:
    colors.append('black')

# Let's plot the whole thing
fig = plt.figure(figsize=(12,8))

plt.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors)
plt.xlabel('Release Year')
plt.ylabel('Duration in minutes')
plt.title('Movie Duration by Year of Release')
plt.show()