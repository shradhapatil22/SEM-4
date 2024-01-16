nums=[10,56,89,43,54]
print(nums)

print(nums[4])

# prints all elements from the 3rd position
print(nums[2:])

# prints from the last
print(nums[-1])

names=["amy","jake","gina","terry"]
print(names)

# lists can have multiple data types
values=["amy",32,4.5]
print(values)

# list of lists
mil=[values,names]
print(mil)

nums.reverse()
print(nums)

# append elements adds at the end
nums.append(45)
print(nums)

# insert adds at given position
nums.insert(2,77)
print(nums)

# remove: removes the element from the list
nums.remove(45)
print(nums)

# pop: removes the element at the position specified and returns it
print(nums.pop(0))

# deleting multiple values
del nums[3:]
print(nums)

# adding multiple elements
nums.extend([29,76])
print(nums)

# finding the min,max,sum element
print(min(nums))
print(max(nums))
print(sum(nums))

# sorting the elements
nums.sort()
print(nums)