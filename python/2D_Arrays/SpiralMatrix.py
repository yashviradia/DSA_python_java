def spiralOrder(matrix: List[List[int]]) -> List[int]:
    if not matrix:
        return []

    startRow = 0
    endRow = len(matrix)-1
    startCol = 0
    endCol = len(matrix[0])-1

    output = []

    while len(output) <= (endRow+1) * (endCol+1):
        # top
        for j in range(startCol, endCol+1):
            output.append(matrix[startRow][j])
        startRow+=1

        # right
        for i in range(startRow, endRow+1):
            output.append(matrix[i][endCol])
        endCol-=1

        # bottom
        if startRow <= endRow:
            for j in range(endCol, startCol-1, -1):
                output.append(matrix[endRow][j])
            endRow-=1

        # left
        if startCol <= endCol:
            for i in range(endRow, startRow-1, -1):
                output.append(matrix[i][startCol])
            startCol+=1
    

    return output




    