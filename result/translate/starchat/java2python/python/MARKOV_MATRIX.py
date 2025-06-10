def f_gold(matrix):
        for i in range(len(matrix)):
            sum = 0
            for j in range(len(matrix[0])):
                sum += matrix[i][j]
            if sum!= 1:
                return False
        return True