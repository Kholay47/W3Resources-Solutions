lst1=[4,5,6]
lst2=[7,8,9]
product=sum(x*y for x,y in zip(lst1,lst2))
print(product)