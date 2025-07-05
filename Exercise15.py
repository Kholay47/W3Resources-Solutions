# take out common elements from list

lst1=[1,2,3,4,5]
lst2=[6,8,5,1,10]

commonlist=list(set(lst1) & set(lst2))
print(commonlist)