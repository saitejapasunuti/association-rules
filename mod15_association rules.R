######################### ASSOCIATION RULES ####################################

install.packages("arules")
library(arules)
#arules provides the infrastructure for representing,manipulating,analysing the  transaction data and patterns using frequent items and association rules.

############################# BOOK DATAFRAME ###############

#load data
book <- read.csv(file.choose())
View(book)

class(book)



install.packages("arulesViz")
library(arulesViz)
#for visualization of rules

#making rules using apriori algorithm
#keep changing support and confidence values for getting different rules.

#building rules using apriori algorithm
arules <- apriori(book,parameter = list(support=0.002,confidence=0.6,minlen=2))
arules
#set of 11242 rules

arules_b <- apriori(book,parameter = list(support=0.004,confidence=0.9,minlen=2))
arules_b

#no changes occured while using different support and confidence values

inspect(head(sort(arules,by="lift")))#inspect is used to view

#viewing rules based on lift values

#overall quality
head(quality(arules))

#differrnt ways of visualization of rules
plot(arules)

plot(arules,method = "grouped")
plot(arules[1:20],method = "graph")#for good visualization here i have plotted few rules


################################### MY MOVIES DATAFRAME ##########################

################LOAD DATASET ################
movies <- read.csv(file.choose())
View(movies)

class(movies)
summary(movies)

#load arulesViz
#making rules using apriori algorithm
#keep changing support and confidence values for getting different rules.

#building model using apriori algorithm
arules_m <- apriori(movies,parameter = list(support=0.002,confidence=0.6,minlen=2))
arules_m
#set of 1105062 rules for support 0.002 & conf=0.6

arules_m2 <- apriori(movies,parameter = list(support=0.075,confidence=0.95,minlen=2))
arules_m2
#set of 1083077 rules for support=0.002 &support=0.004  and confidence as 0.8

inspect(head(sort(arules_m,by="lift")))
inspect(head(sort(arules_m1,by="lift")))
#viewing rules based on lift value

#overall quality
head(quality(arules_m))
head(quality(arules_m2))

#different ways of visualizing the rules
plot(arules_m,method="grouped")
plot(arules_m2[1:30],method = "graph")


############################## MY PHONE DATASET ######################

######## LOAD DATASET ################

phone <- read.csv(file.choose())
View(phone)

summary(phone)

#load arulesViz
#making rules using apriori algorithm
#keep changing support and confidence values for getting different rules.

#building model using apriori algorithm
arules_p <- apriori(phone,parameter=list(support=0.002,confidence=0.6,minlen=2))
arules_p
#set of 10505 rules 

arules_p1 <- apriori(phone,parameter=list(support=0.002,confidence=0.75,minlen=2))
arules_p1
#set of 10219 rules 

#arules_p2 <-apriori(phone,parameter=list(support=0.002,confidence=0.9,minlen=2))
#arules_p2 
# there is no change in the value further with the change in the confidence and support values

inspect(head(sort(arules_p,by="lift")))

#viewing rules based on the lift vallues

#overall quality  
head(quality(arules_p))

#different  ways of visualization  of the rules
plot(arules_p)
plot(arules_p,method = 'grouped')
plot(arules_p[1:20],method = 'graph')


############################ TRANSACTION RETAIL DATASET #####################

##############LOAD DATASET#########################
trans <- read.csv(file.choose())
View(trans)

trans1 <- na.pass(trans)
View(trans1)


class(trans1$X.HANGING.)
class(trans1$X.HEART.)
class(trans1$X.HOLDER.)
class(trans1$X.T.LIGHT.)
class(trans1$X.WHITE.)
#factor
trans$NA. <- as.factor(trans$NA.)
class(trans1$NA.)
#factor

summary(trans1)
#load arulesViz
#making rules using apriori algorithm
#keep changing support and confidence values for getting different rules.

#model building using apriori algorithm
arules_t <- apriori(trans1,parameter=list(support=0.002,confidence=0.5,minlen=2))
arules_t
#set of 1415 rules

arules_t1 <- apriori(trans1,parameter=list(support=0.002,confidence=0.95,minlen=2))
arules_t1
#set of 995 rules

inspect(head(sort(arules_t,by="lift")))
inspect(head(sort(arules_t1,by="lift")))

#viewing rules based on the lift vallues

#overall quality  
head(quality(arules_t))
#overall quality  
head(quality(arules_t1))

#different  ways of visualization  of the rules
plot(arules_t)
plot(arules_t1)
plot(arules_t1,method = 'grouped')
plot(arules_t1[1:20],method = 'graph')
