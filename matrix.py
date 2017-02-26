import math

def print_matrix( matrix ):
	string = ""
	for r in range(0,len(matrix)):
		string += "| "
		for c in range(0,len(matrix[r])):
			string += str(matrix[r][c]) 
			string += " " 
			#print string
		string += "|\n"
	print string

def ident( matrix ):
    for r in range(0,len(matrix)):
        for c in range(0,len(matrix[r])):
            if r == c:
                matrix[r][c] = 1
            else:
                matrix[r][c] = 0

def scalar_mult( matrix, s ):
    for r in range(0,len(matrix)):
        for c in range(0,len(matrix[r])):
            matrix[r][c] *= s

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
	m = []
	for r1 in range(0,len(m1)):
		nr = []
		for c in range(0,len(m2[0])): 
			dotProd = 0
			for r2 in range(0,len(m2)): 
				dotProd += m1[r1][r2] * m2[r2][c]
			nr.append(dotProd)
		m.append(nr)
	return m

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

'''
# TEST CASES
a = [[1,2,3],[4,5,6]]
b = [["a","b"],["c","d"],["e","f"]]
c = [[1,2,3],[1,2,3],[1,2,3]]
print_matrix(a)
print_matrix(b)


print_matrix(ident(c)) 

print_matrix(scalar_mult(a,5))
'''
