# Create a 3x3 identity matrix as a list of lists.

matlist=[[1 if i==j else 0 for j in range(3)] for i in range(3)]
print(matlist)