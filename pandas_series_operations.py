"""Pandas Series"""

import numpy as np
import pandas as pd

"""Pandas Series (Session 16)

Importing Pandas
"""

"""Series from Lists"""

# String
country = ['India', 'Pakistan', 'USA', 'Nepal', 'Sri Lanka']

pd.Series(country)

# Integers
runs = [13, 24, 35, 46, 57]

pd.Series(runs)

# Custom Index
marks = [12, 23, 34, 45, 56]
subjects = ['maths', 'hindi', 'english', 'science', 'sst']

pd.Series(marks, index=subjects)
pd.Series(marks, subjects)

# Both work

# Setting a name

pd.Series(marks, index=subjects, name='Student Marks')

"""Series from Dictionary"""

marks = {
    'maths': 12,
    'science': 23,
    'hindi': 34,
    'english': 45,
    'sst': 56
}

marks_series = pd.Series(
    marks,
    name='Student Marks from Dictionary'
)

marks_series

"""Series Attributes"""

# Size
marks_series.size

# Data type
marks_series.dtype

# Name
marks_series.name

# Check if values are unique
marks_series.is_unique

# Index
marks_series.index

# Values
marks_series.values

type(marks_series.values)

"""Series using read_csv"""

# With one column
subs = pd.read_csv('/content/subs.csv').squeeze()

subs

# type() shows Series when squeeze() is added,
# otherwise it shows DataFrame by default

# With two columns

vk = pd.read_csv(
    '/content/kohli_ipl.csv',
    index_col='match_no'
).squeeze()

vk

movies = pd.read_csv(
    '/content/bollywood.csv',
    index_col='movie'
).squeeze()

movies

# First 3 entries
vk.head(3)

# Last 5 entries
vk.tail(5)

# Random sample
movies.sample(5)

# Value counts
movies.value_counts()

# sort_values() -> inplace

# vk.sort_values()

# vk.sort_values(ascending=False).head(1).values[0]

# ascending=False = descending order
# head(1) = only top result
# values = gives result in array form
# [0] = gives only the value

# sort_values() does not change the original data by default

vk = vk.copy()

vk.sort_values(inplace=True)

vk

# sort_index() -> inplace

movies = movies.copy()

movies.sort_index(inplace=True)

movies

"""Series Mathematical Methods"""

# count()
# count() does not count missing values,
# that is how it is different from size

vk.count()

# sum() -> product()

subs.sum()

# subs.prod()

# mean -> median -> mode -> std -> var

subs.mean()

print(vk.median())

print(movies.mode())

print(subs.std())

print(vk.var())

# min / max

subs.min()

subs.max()

# describe()

print(subs.describe())

"""Series Indexing"""

# Integer indexing

x = pd.Series([12, 13, 14, 35, 46, 57, 58, 79, 9])

x[1]

# Negative indexing

x.iloc[-1]

# x[-1] will not work here

movies[0]

movies['Uri: The Surgical Strike']

movies[-1]

# Slicing

vk[5:16]

# Negative slicing

vk[-5:]

movies[-5:]

subs[::2]

# Fancy indexing

vk[[1, 3, 4, 5]]

# Indexing with labels -> Fancy indexing

movies['2 States (2014 film)']

"""Editing Series"""

# Using indexing

marks_series[1] = 100

marks_series

# If an index does not exist

marks_series['evs'] = 95

marks_series['physics'] = 68

marks_series['probability and statistics'] = 92

# This will add a new subject

marks_series

# Slicing

marks_series[2:4] = [11, 11]

marks_series

# Fancy indexing

marks_series[[0, 3, 4]] = [0, 0, 0]

marks_series

# Using index label

movies['2 States (2014 film)'] = 'Alia Bhatt'

movies

"""Series with Python Functionalities"""

# len() / type() / dir() / sorted() / max() / min()

print(len(subs))

print(type(subs))

print(dir(subs))

# sorted() stores sorted values in a list

print(sorted(subs))

print(max(subs))

print(min(subs))

# Type conversion

list(marks_series)

dict(marks_series)

"""Membership Operations"""

# 'in' checks index labels only, not values

'2 States (2014 film)' in movies

# Alia Bhatt is a value, not an index

'Alia Bhatt' in movies

# To search in values

'Alia Bhatt' in movies.values

"""Looping"""

# Loops work on values by default

for i in movies:
    print(i)

# For looping through index

# for i in movies.index:
#     print(i)

"""Arithmetic Operators (Broadcasting)"""

100 - marks_series

100 + marks_series

"""Relational Operators"""

vk >= 50

"""Boolean Indexing on Series"""

# Find number of 50s and 100s scored by Kohli

vk[vk >= 50].size

# Find number of ducks

vk[vk == 0].size

# Count number of days where subscribers were more than 200

subs[subs > 200].size

# Find actors who have done more than 20 movies

num_movies = movies.value_counts()

num_movies[num_movies > 20]

"""Plotting Graphs on Series"""

subs.plot()

movies.value_counts().head(20).plot(kind='bar')

movies.value_counts().head(20).plot(kind='pie')
