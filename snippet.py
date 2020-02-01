print 'Hello queen'

class Board (object):
    def __init__(self, size):
        self.matrix = []
        self.size=size
        for row in range(size):
            self.matrix.append ([0] * size)

    def reset(self):
        self.matrix = []
        for row in range(self.size):
            self.matrix.append ([0] * self.size)

    def set_queen(self,row,column):
        self.matrix[row][column] = 1
    
    def square_is_free(self,row,column):
        free = True
        if (sum(self.matrix[row]) > 0 ):
             free = False
             
        for row_aux in self.matrix:
            if (row_aux[column] == 1):
                free = False

        for row_aux in range(-self.size, self.size):
            if (not (row_aux + row) in range(self.size)):
                continue
            for column_aux in range(-self.size, self.size):
                if (not (column_aux + column) in range(self.size)):
                    continue
                if (abs(column_aux) == abs(row_aux)):
                    if (self.matrix[row_aux + row][column_aux + column] == 1):
                        free = False
       
        return free

    def find_queen_solution(self):
        import random
        queens = 0
        while (queens<self.size):
            queens = 0
            self.reset()
            row_range=range(self.size)
            random.shuffle(row_range)
            for row_aux in row_range:
                for column_aux in range( self.size):
                    if (False): 
                        continue
                    if self.square_is_free(row_aux,column_aux):
                        self.set_queen(row_aux,column_aux)
                        queens += 1

            if (queens==8):
                print ('VAMOS COPON\n'+ str(self))
            else:
                print ("Stupid algorythm failed : " + str(queens) + " queens")
    
    def __str__(self):

        return '\n'.join([''.join(['{:2}'.format(item) for item in row])for row in self.matrix] )

board= Board(8)
board.find_queen_solution()




