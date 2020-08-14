################# Association rules ##############

############# my movies dataset ###############

import pandas as pd
#pandas is used for data manipulation,analysis,cleaning
pip install  mlxtend
#machine learning extensions(mlxtend) is a python library of useful tools for the day to day data science tasks
import mlxtend
from mlxtend.frequent_patterns import apriori,association_rules

movies=[]
with open("D://360digiTMG/unsupervised/mod15 association rules/Datasets (3)/my_movies.csv") as f:
    movies=f.read()

#splitting the data into seperate transacction using seperator as "\n"
movies=movies.split("\n")
movies_list=[]
for i in movies:
    movies_list.append(i.split(","))
    
all_movies_list = [i for item in movies_list for i in item]
from collections import Counter,OrderedDict
#ordered dict are just like regular dict they just remember the order that the items were inserted
#collections in python are used to store the collection of data like dict,list,set,tupple
#Counter is used to store the count values of dictionaries

item_frequencies = Counter(all_movies_list)
# after sorting
item_frequencies = sorted(item_frequencies.items(),key = lambda x:x[1])

# Storing frequencies and items in separate variables 
frequencies = list(reversed([i[1] for i in item_frequencies]))
items = list(reversed([i[0] for i in item_frequencies]))

# barplot of top 10 

import matplotlib.pyplot as plt
#for data visualization

plt.bar(height = frequencies[0:11],x= list(range(0,11)),color='rgbkymc');plt.xticks(list(range(0,11),),items[0:11]);plt.xlabel("items")
plt.ylabel("Count");plt.xlabel("Items")


# Creating Data Frame for the transactions data 

movies_series  = pd.DataFrame(pd.Series(movies_list))
movies_series = movies_series.iloc[:2001,:] # removing the last empty transaction

movies_series.columns = ["transactions"]

# creating a dummy columns for the each item in each transactions - Using column names as item name
X = movies_series['transactions'].str.join(sep='*').str.get_dummies(sep='*')

frequent_itemsets = apriori(X, min_support=0.005, max_len=3,use_colnames = True)

# Most Frequent item sets based on support 
frequent_itemsets.sort_values('support',ascending = False,inplace=True)
plt.bar(x = list(range(1,11)),height = frequent_itemsets.support[1:11],color='rgmyk');plt.xticks(list(range(1,11)),frequent_itemsets.itemsets[1:11])
plt.xlabel('item-sets');plt.ylabel('support')

rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
rules.head(20)
rules.sort_values('lift',ascending = False).head(10)

