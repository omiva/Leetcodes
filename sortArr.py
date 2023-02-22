# PENDING

def matrixSearch(matrix, target):
    col = []
    row = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(''.join(matrix[i][j]))
            if ','.join(matrix[i][j]) == target:
                row = (matrix[i])
                for i in range(len(matrix)):
                    col.append(matrix[i][j])
                    # return sorted(row) == row and sorted(col) == col
    print(col, row)
    print(target)
print(matrixSearch(input("Matrix: "), input("\nTarget: ")))