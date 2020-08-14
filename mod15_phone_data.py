################# Association rules ##############

############# phone dataset ###############

pip install mlxtend

import pandas as pd
#pandas is used for data manipulation, analysis,cleaning
from mlxtend.frequent_patterns import apriori,association_rules

phone=[]

with open("D://360digiTMG/unsupervised/mod15 association rules/Datasets (3)/myphonedata.csv") as f:
    phone=f.read()


phone=phone.split("\n")
phone_list=[]
for i in phone:
    phone_list.append(i.split(","))


all_movies_list=[i for item in phone_list for i in item]

from collections import Counter,OrderedDict
#ordered dict are just like regular dict they just remember the order that the items were inserted
#collections in python are used to store the collection of data like dict,list,set,tupple
#Counter is used to store the count values of dictionaries

item_frequencies=Counter(all_movies_list)
item_frequencies=sorted(item_frequencies.items(),key= lambda x:x[1])

frequencies = list(reversed([i[1] for i in item_frequencies]))
items=list(reversed([i[0] for i in item_frequencies]))

import matplotlib.pyplot as plt
#for data visualization
plt.bar(x=list(range(0,11)),height=frequencies[0:11],color="rgbkymc");plt.xticks(list(range(0,11)),items[0:11])
plt.xlabel("items");plt.ylabel("Count")

phone_series  = pd.DataFrame(pd.Series(phone_list))
phone_series = phone_series.iloc[:12,:] # removing the last empty transaction
phone_series.columns = ["transactions"]

## creating a dummy columns for the each item in each transactions ... Using column names as item name
X = phone_series['transactions'].str.join(sep='*').str.get_dummies(sep='*')

frequent_itemsets = apriori(X, min_support=0.005, max_len=3,use_colnames = True)

# Most Frequent item sets based on support 
frequent_itemsets.sort_values('support',ascending = False,inplace=True)

plt.bar(x = list(range(1,11)),height = frequent_itemsets.support[1:11],color='rgmyk');plt.xticks(list(range(1,11)),frequent_itemsets.itemsets[1:11])
plt.xlabel('item-sets');plt.ylabel('support')

rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
rules.head(20)
rules.sort_values('lift',ascending = False).head(10)