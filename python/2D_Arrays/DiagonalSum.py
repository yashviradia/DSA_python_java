def diagonalSum(matrix) -> int:

    sum = 0
    n = len(matrix)

    for i in range(n):

        sum += matrix[i][i]

        if (i != n-i-1):
            sum += matrix[i][n-i-1]
    
    return sum 

matrix = [[1,2,3,4], [5,6,7,8], [9, 10, 11, 12], [13, 14, 15, 16]]

print(diagonalSum(matrix))