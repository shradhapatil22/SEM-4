# 8) Write a Pandas program to create a Data Frame from csv and perform the following operations:
# a) Display column names of data frame
# b) Read the column name and display unique values,
# c) Display frequency of occurrence of each unique value.
# d) Count of total number of records in the Dataframe.

import numpy as np
import pandas as pd

data = pd.read_csv("marks.csv")
print(data)

cols = list(data.columns)
print ("column names : ")
for col in cols:
    print(col)

attr = input("Enter the attribute : ")
attrvals = list(data[attr])
print(attrvals)

uniq =np.unique(attrvals)
print(" unique values for the attributes ", attr, " are ")
for u in uniq:
    print(u)
print(" frequency of occurence of unique values is ")
for u in uniq :
    print(u , attrvals.count(u))
print ( " total no of records : ",len(data))