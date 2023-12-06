def staircaseSearch(matrix, key):
    row = len(matrix)-1
    col = 0

    while (row >= 0 and col < len(matrix[0])):
        if (matrix[row][col] == key):
            print("found at (" + str(row) + "," + str(col) + ")")
            return True
        elif(key < matrix[row][col]):
            row-=1
        else:
            col+=1
    
    print("key not found")
    return False

matrix = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]
staircaseSearch(matrix, 33)