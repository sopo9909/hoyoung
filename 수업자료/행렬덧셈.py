<<<<<<< HEAD
matrix_1 = [[1,2],[3,4]]
matrix_2 = [[5,6],[7,8]]
matrix_3 = [[],[]]
matrix_4 = [[],[]]
matrix_5=[]
for i in range(2):
    for j in range(2):
        matrix_3[i].append(matrix_1[i][j] + matrix_2[i][j])
print(matrix_3)

for i in range(2):
    temp= []
    for j in range(2):
        temp.append(matrix_1[i][j] + matrix_2[i][j])
    matrix_5.append(temp)
print(matrix_5)

for i in range(2):
    for j in range(2):
        matrix_4[i].append(matrix_1[i][j]+1)
print(matrix_4)

=======
matrix_1 = [[1,2],[3,4]]
matrix_2 = [[5,6],[7,8]]
matrix_3 = [[],[]]
matrix_4 = [[],[]]
matrix_5=[]
for i in range(2):
    for j in range(2):
        matrix_3[i].append(matrix_1[i][j] + matrix_2[i][j])
print(matrix_3)

for i in range(2):
    temp= []
    for j in range(2):
        temp.append(matrix_1[i][j] + matrix_2[i][j])
    matrix_5.append(temp)
print(matrix_5)

for i in range(2):
    for j in range(2):
        matrix_4[i].append(matrix_1[i][j]+1)
print(matrix_4)

>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
