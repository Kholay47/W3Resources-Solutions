# Extract all odd numbers from a list of integers.

lst=[1,2,3,4,5]

newlist=[i for i in lst if i%2!=0]
print(newlist)