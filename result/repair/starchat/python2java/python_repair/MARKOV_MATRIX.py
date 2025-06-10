def f_gold(matrix):
        for i in range(len(matrix)):
            sum = 0
            j=0 
            while j<len(matrix[i]) :
                sum += matrix[i][j]
                j += 1
            if sum!= 1:
                return False
        return True
