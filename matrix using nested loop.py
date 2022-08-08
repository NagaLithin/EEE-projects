# 3x3 matrix
X = [[70,50,9],
    [10,17,99],
    [30 ,88,67]]
# 3x4 matrix
Y = [12,54,34,77],
[7,15,23,98],
[55,45,35,66]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
