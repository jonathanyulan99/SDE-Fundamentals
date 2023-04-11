def transpose(m: list[list[int]]) -> list[list[int]]:
    matrix_rows = len(matrix)
    matrix_cols = len(matrix[0])
    results = [] 
    for _ in range(matrix_cols):
        result = [] 
        for _ in range(matrix_rows):
            result.append(0)
        results.append(result)
        
    for row in range(len(results)):
        for col in range(len(results[row])):
            results[row][col] = m[col][row]
        
    return results

matrix = [[1,2,3],[4,5,6]]

print(transpose(matrix))