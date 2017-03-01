from display import *
from draw import *


screen = new_screen()

color1 = [ 0, 255, 0 ]
color2 = [255, 0, 0]
color3 = [0, 0, 255]
matrix = new_matrix()

def test(matrix):
    for i in range(0, 150, 5):
        matrix = add_edge(matrix, i, 150-i, 0, -i, i - 150, 0)

    draw_lines( matrix, screen, color1 )
    print "Current Edge Matrix"
    print_matrix(matrix)
    print "New Identity Matrix I"
    a = ident(new_matrix())
    print_matrix(a)

    print "Multiplying I x Edge Matrix, here is the resultant matrix:"
    matrix = matrix_mult(a, matrix)
    print_matrix(matrix)

    #print "Now Scaling the Edge Matrix by 1.5"
    #print_matrix(matrix)
    #matrix = scalar_mult(matrix, 2)
    return matrix

def scale(matrix, s):
    matrix = scalar_mult(matrix, s)
    return matrix

def rotate(matrix, angle):
    angle = math.radians(angle)
    rot = new_matrix(4,4)
    rot = add_point(rot, math.cos(angle), math.sin(angle), 0)
    rot = add_point(rot, -1*math.sin(angle), math.cos(angle), 0)
    rot = add_point(rot, 0, 0, 1)
    rot = add_point(rot, 0, 0, 0)
    matrix = matrix_mult(rot, matrix)
    return matrix

matrix = test(matrix)

for i in range(0, 360, 90):
    matrix = rotate(matrix, i)
    draw_lines(matrix, screen, color1)
    matrix = rotate(matrix, i + 45)
    draw_lines(matrix, screen, color3)

matrix = scale(matrix, 2)
matrix = rotate(matrix, 22.5)
for i in range(0, 360, 90):
    matrix = rotate(matrix, i)
    draw_lines(matrix, screen, color3)
    matrix = rotate(matrix, i + 45)
    draw_lines(matrix, screen, color2)
display(screen)
