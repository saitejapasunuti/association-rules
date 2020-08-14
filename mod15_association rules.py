################# Association rules ##############

############# books dataset ###############

import pandas as pd
#pandas is used for data manipulation,analysis,cleaning
#pip install  mlxtend
#machine learning extensions(mlxtend) is a python library of useful tools for the day to day data science tasks
import mlxtend
from mlxtend.frequent_patterns import apriori,association_rules

import numpy as np
books = []
with open("D:/360digiTMG/unsupervised/mod15 association rules/Datasets (3)/book.csv") as f:
    books = f.read()

#splitting data into seperate transactions using seperator as '\n'
books=books.split("\n")
books_list=[]
for i in books:
    books_list.append(i.split(","))

all_books_list=[i for item in books_list for i in item]

from collections import Counter,OrderedDict
#ordered dict are just like regular dict they just remember the order that the items were inserted
#collections in python are used to store the collection of data like dict,list,set,tupple
#Counter is used to store the count values of dictionaries

item_frequencies=Counter(all_books_list)
#after sorting
item_frequencies=sorted(item_frequencies.items(),key=lambda x:x[1])

#sorting frequencies and items in seperate variable
frequencies=list(reversed([i[1] for i in item_frequencies]))
items=list(reversed([i[0]for i in item_frequencies]))



# Creating Data Frame for the transactions data 

books_series  = pd.DataFrame(pd.Series(books_list))
books_series = books_series.iloc[:2001,:] # removing the last empty transaction

books_series.columns = ["transactions"]

# creating a dummy columns for the each item in each transactions ... Using column names as item name
X = books_series['transactions'].str.join(sep='*').str.get_dummies(sep='*')

frequent_itemsets = apriori(X, min_support=0.07, max_len=3,use_colnames = True)

# Most Frequent item sets based on support 
import matplotlib.pyplot as plt
frequent_itemsets.sort_values('support',ascending = False,inplace=True)
plt.bar(list(range(1,4)),height= frequent_itemsets.support)
plt.xlabel('item-sets');plt.ylabel('support')

rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
rules.head()
rules.sort_values('lift',ascending = False).head(10)

