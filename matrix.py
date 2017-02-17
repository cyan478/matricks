import math


def print_matrix( matrix ):
	str = ""
    for r in matrix:
    	str += "| "
    	for c in matrix:
    		str += matrix[r][c] + " " 
    	str += "|\n"
    print str

def ident( matrix ):
    for r in matrix.length:
        for c in matrix[r].length:
            if r == c:
                matrix[r][c] = 1
            else:
                matrix[r][c] = 0

def scalar_mult( matrix, s ):
    for r in matrix.length:
        for c in matrix[r].length:
            matrix[r][c] *= s

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):







def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
