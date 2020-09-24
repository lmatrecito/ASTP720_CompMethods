# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 19:55:44 2020

@author: lizam
"""


# Homework 3 Problem 1 - Unit Testing: Checking to see if stuff works
# from HW2 matrix class

import unittest 
from ASTP720_HW2_P3 import Matrix

class MatrixTests(unittest.TestCase):

# Addition unit test
    def testAdd(self):
        m1 = Matrix.fromList([[1, 2, 3], [4, 5, 6]])
        m2 = Matrix.fromList([[7, 8, 9], [10, 11, 12]])        
        m3 = m1 + m2
        self.assertTrue(m3 == Matrix.fromList([[8, 10, 12], [14,16,18]]))

# Subtraction unit test
    def testSub(self):
        m1 = Matrix.fromList([[1, 2, 3], [4, 5, 6]])
        m2 = Matrix.fromList([[7, 8, 9], [10, 11, 12]])        
        m3 = m2 - m1
        self.assertTrue(m3 == Matrix.fromList([[6, 6, 6], [6, 6, 6]]))

# Multiplication unit test
    def testMul(self):
        m1 = Matrix.fromList([[1, 2, 3], [4, 5, 6]])
        m2 = Matrix.fromList([[7, 8], [10, 11], [12, 13]])
        self.assertTrue(m1 * m2 == Matrix.fromList([[63, 69], [150, 165]]))
        self.assertTrue(m2*m1 == Matrix.fromList([[39, 54, 69], [54, 75, 96], [64, 89, 114]]))

# Transpose unit test
    def testTranspose(self):
        m1 = Matrix.makeRandom(25, 30)
        zerom = Matrix.makeZero(25, 30)
        m2 = m1 + zerom
        
        m1.transpose()
        m1.transpose()
        self.assertTrue(m2 == m1)

# Also testing getTranspose
        m2 = m1.getTranspose()
        r2 = m2.getRank()
        self.assertTrue(r2==(30,25))
        m2.transpose()
        self.assertTrue(m2 == m1)

# Identity matrix unit test
    def testId(self):
        m1 = Matrix.makeId(10)
        m2 = Matrix.makeRandom(4, 10)
        m3 = m2*m1
        self.assertTrue(m3 == m2)
        
# Trace unit test
# Determinant unit test
# Inversion unit test
# LU decomp unit test


if __name__ == "__main__":
    unittest.main()