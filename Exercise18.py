lst=[2,3,4,5,9,7]
minval, maxval = min(lst),max(lst)
normalizedlst=[(x-minval/maxval-minval) for x in lst]
print(normalizedlst)