from display import *
from draw import *

screen = new_screen()
color = [ 219, 131, 159 ]
matrix = new_matrix()

def matrixTest():
	print
	print "~~~~~~~~~~~~"
	print "Matrix Tests"
	print "~~~~~~~~~~~~"
	print

	print "Original matrix"
	print_matrix(matrix)
	print

	print "Identity matrix"
	ident(matrix)
	print_matrix(matrix)
	print

	print "Matrix multiplied by scalar"
	scalar_mult(matrix,42)
	print_matrix(matrix)
	print

	print "Matrix multiplication"
	a = [[1,2,3],[4,5,6]]
	b = [[6,3],[5,6],[1,4]]
	print "Matrix A"
	print_matrix(a)
	print "Matrix B"
	print_matrix(b)
	print "Result after multiplying"
	c = matrix_mult(a,b)
	print_matrix(c)
	print

	#print "Image Matrix"

	a = 50
	b = 75
	c = 100
	d = 25
	scalar_mult(matrix,30)

	for i in range(80): #IT LOOKS LIKE A BUG :'( im scared
		add_edge(matrix, a, b, 0, c, d, 0)
		add_edge(matrix, a, c, 0, b, d, 0)
		add_edge(matrix, d, a, 0, c, b, 0)
		add_edge(matrix, a, d, 0, b, c, 0)
	
		a += 5
		b += 5
		c += 5
		d += 5

	#print_matrix(matrix)
	print "the matrix itself is very long so i won't be printing it"
	print

matrixTest()

draw_lines( matrix, screen, color )
display(screen)