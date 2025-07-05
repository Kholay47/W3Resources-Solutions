# Replace all even numbers in a list with their negative.

lst = [1,2,3,4,5,6,7,8,9]
newlst = [-x if x%2 == 0 else x for x in lst]
print(newlst)