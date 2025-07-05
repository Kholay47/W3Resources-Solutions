# Replace all odd numbers in a list with -1.

lst = [1,2,3,4,5,6,7,8,9]
newlst = [-1 if i%2 !=0 else i for i in lst]
print(newlst)