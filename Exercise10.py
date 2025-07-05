# Find the indices of non-zero elements in a list.

lst= [1,0,0,4,3,0]
newlst=[i for i, x in enumerate(lst) if x!=0]
print('Indices of non zero elements:',newlst)