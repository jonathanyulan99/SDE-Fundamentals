def pascals_triangle(input_row:int)->list:
    if input_row == 0:
        return [1]
    
    line = [1] 
    previousLine = pascals_triangle(input_row - 1)
    for i in range(len(previousLine)-1):
        line.append((previousLine[i]+previousLine[i+1]))
    line = line + [1]
    
    return line 

print(pascals_triangle(5))