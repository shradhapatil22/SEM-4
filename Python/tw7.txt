# 7)	Three IA’s are conducted for a class of 10 students for the subject Maths. The name, marks and USN are read from a file in.txt.
# Find the average of the IA for each student and write the USN and average to a file out.txt. Display the highest average of the class on the console.

import numpy as np
import csv

data=np.loadtxt("in.txt",usecols=range(1,5),delimiter=",")
print("Marks data: \n ",data)

avg=np.array([])
for mks in data:
    avg=np.append(avg,round(np.mean(mks),2))

print("Averages are: ")
for avgMks in avg:
    print(avgMks)

with open("in.txt") as inF:
    with open("out.txt","w") as outF:
        reader=csv.reader(inF)
        i = 0
        for line in reader:
            outF.write(line[5] + ' ' + str(avg[i]) + ' \n ')
            i=i+1
print(" class Topper has scored average mks : ", np.max(avg))
