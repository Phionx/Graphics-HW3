#!/usr/bin/env python
import math
import sys

def print_matrix( matrix ):
    print "PRINTING MATRIX NOW:"
    if isinstance(matrix, list):
        for i in range(0, len(matrix)):
            if isinstance(matrix[i], list):
                for j in range(0, len(matrix[i])):
                    sys.stdout.write(str(matrix[i][j]) + " ")
                print " "
            else: 
                print "\nNOT A VALID MATRIX A"
                return
        return
    else:
        print "\nNOT A VALID MATRIX B"
        return



def ident( matrix ):
    if isinstance(matrix, list):
        for i in range(0, len(matrix)):
            if isinstance(matrix[i], list) and len(matrix) == len(matrix[i]):
                for j in range(0, len(matrix[i])):
                    if i == j:
                        matrix[i][j] = 1
                    else:
                        matrix[i][j] = 0
            else:
                print "\nNOT A SQUARE MATRIX, CAN'T MAKE AN IDENTITY"
                return
        return matrix
    else:
        print "\nNOT A VALID MATRIX"
        return
        

def scalar_mult( matrix, s ):
    if isinstance(matrix, list):
        for i in range(0, len(matrix)):
            if isinstance(matrix[i], list):
                for j in range(0, len(matrix[i])):
                    matrix[i][j] = s*matrix[i][j]
            else: 
                print "\nNOT A VALID MATRIX A"
                return
        return matrix
    else:
        print "\nNOT A VALID MATRIX B"
        return

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    if isinstance(m1, list) and isinstance(m2, list) and isinstance(m1[0], list) and isinstance(m2[0], list) and len(m1) == len(m2[0]):
        ans = [[None]*len(m1[0]) for lol in range(len(m2))]
        temp1 = [None]*len(m1)
        dot = 0
        for i in range(0, len(m1[0])):
            for j in range(0, len(m1)):
                temp1[j] = m1[j][i]
            for k in range(0, len(m2)):
                ans[k][i] = dot_product(temp1, m2[k])
        return ans
    else: 
        print "\nCAN'T MULTIPLY THESE MATRICES"
        return

def dot_product(v1, v2):
    ans = 0
    if isinstance(v1, list) and isinstance(v2, list) and len(v1) == len(v2):
        for i in range(0, len(v1)):
            ans += v1[i]*v2[i]
        return ans
    else:
        print "\nINVALID INPUT"
        return



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( None )
    return m

'''
a = new_matrix(4, 4)
b = new_matrix(4, 4)
a = ident(a)
b = ident(b)
print_matrix(a)
print_matrix(b)
c = matrix_mult(a, b)
print_matrix(c)
print str(c[0][0])
a = new_matrix(4,4)
print str(a)
'''
