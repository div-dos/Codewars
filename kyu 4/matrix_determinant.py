def determinant(matrix):
    #your code here
    if len(matrix) == 1:
        return matrix[0][0]
    
    total = 0
    
    for i in range(len(matrix)):
        total += (-1)**(i) * matrix[0][i] * determinant(cal_sub_arr(matrix, i))
    return total
        
    
def cal_sub_arr(matrix, index):
    new_matrix = []
    
    for i in range(1,len(matrix)):
        new_matrix.append(matrix[i][:index]+matrix[i][index+1:])

    return new_matrix