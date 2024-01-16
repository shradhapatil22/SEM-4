sum=0
counter=1
fact=1
n=int(input("Enter n: "))
# while counter<=n :
#     sum+=counter
#     counter += 1

# while counter<=n :
#     if counter%2==0:
#         sum+=counter
#     counter += 1

while counter<=n :
    fact*=counter
    print(fact, end="\t")
    counter += 1

#print("\n sum= ",sum)

