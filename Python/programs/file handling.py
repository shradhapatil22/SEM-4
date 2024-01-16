# reading from a file
file=open('Mydata.txt','r')

# print entire content
print(file.read())

# print 1st line
print(file.readline())
print(file.readline(2))

# writing to a file
file2=open('WriteTo.txt','w')
file2.write('something')

# append to a file
file2=open('WriteTo.txt','a')
file2.write('something again')

# reding from one file and pasting it to other
for data in file:
    file2.write(data)