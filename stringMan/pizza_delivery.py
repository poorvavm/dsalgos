from math import fabs
import sys

class m_matrix:
    def __init__(self, m, n, init=True):
        if init:
            self.rows = [[0]*n for x in range(m)]
        else:
            self.rows = []
        self.m = m
        self.n = n  

    def __str__(self):
        s='\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
        return s + '\n'

    def set_value(self, row, col, val):
        self.rows[row][col] = val

    def get_value(self, row, col):
        return self.rows[row][col]

    def get_cost(self, row, col):
        cost = 0
        for i in range(0, self.m):
            for j in range(0, self.n):
                manh_dist = fabs(row-i) + fabs(col - j)
                cost += (manh_dist*self.get_value(i,j))
        return cost

    def shotest_distance(self):
        min_cost = sys.maxint
        for i in range(0, self.m):
            for j in range(0, self.n):
                temp_cost = self.get_cost(i, j)
                if min_cost > temp_cost:
                    min_cost = temp_cost
                temp_cost = 0

        return int(min_cost)

pizza_file = open("test1.txt","r")
num_testcases = int((pizza_file.readline()).rstrip())

for test in range(num_testcases):
    matrix_size = pizza_file.readline().rstrip().split(" ")
    for i in range(0,len(matrix_size)):
        matrix_size[i] = int(matrix_size[i])

    my_matrix = m_matrix(matrix_size[0], matrix_size[1])

    for i in range(0,matrix_size[0]):
        matrix_row = pizza_file.readline()
        matrix_row = matrix_row.rstrip().split(" ")
        
        for j in range(0,len(matrix_row)):
            matrix_row[j] = int(matrix_row[j])
            my_matrix.set_value(i, j, matrix_row[j])

    print str(my_matrix.shotest_distance()) + " blocks"

pizza_file.close()