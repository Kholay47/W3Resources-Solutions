# Convert a list of integers to a list of booleans where all non-zero values become True.

lst = [1,0,1,0,1,0,1,0,0,0,0,1,1,1,1]

newlst= [bool(x) for x in lst]

print(newlst)