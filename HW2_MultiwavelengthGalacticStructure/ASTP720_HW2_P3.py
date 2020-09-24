# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 17:17:12 2020

@author: lizam
"""


# Homework 2 Problem 3 - Write a matrix library that includes a Matrix
# class

import random
import sys

# Exception case
class MatrixError(Exception):
    pass

# Creating a matrix to use for the rest of the code
class Matrix(object):
    def __init__(self, m, n, init=True):    
        if init:
            self.rows = [[0]*n for x in range(m)]
        else:
            self.rows = []
        self.m = m
        self.n = n
    def __getitem__(self, idx):
        return(self.rows[idx])
    def __setitem__(self, idx, item):
        self.rows[idx] = item
    def __str__(self):
        s='\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
        return(s + '\n')
    def __repr__(self):
        s=str(self.rows)
        rank = str(self.getRank())
        rep="Matrix: \"%s\", rank: \"%s\"" % (s,rank)
        return(rep)
    def reset(self): # Reset Matrix data
        self.rows = [[] for x in range(self.m)]
    

# Obtaining Transponse of a matrix
    def transpose(self):                                    # Changes original
        self.m, self.n = self.n, self.m
        self.rows = [list(item) for item in zip(*self.rows)]
    def getTranspose(self):                         # Does not change original
        m, n = self.n, self.m
        mat = Matrix(m, n)
        mat.rows =  [list(item) for item in zip(*self.rows)]
        return(mat)
    def getRank(self):
        return (self.m, self.n)
 
# Test equality
    def __eq__(self, mat):
        return(mat.rows == self.rows)
       
# Adding matrices
    def __add__(self, mat): 
        if self.getRank() != mat.getRank():
            raise MatrixError('Trying to add matrixes of varying rank')
        ret = Matrix(self.m, self.n)        
        for x in range(self.m):
            row = [sum(item) for item in zip(self.rows[x], mat[x])]
            ret[x] = row
        return(ret)
    def __iadd__(self, mat):                     # Adding this and that matrix
        tempmat = self + mat                                   # Calls __add__
        self.rows = tempmat.rows[:]
        return(self)

# Subtracting matrices
    def __sub__(self, mat):  
        if self.getRank() != mat.getRank():
            raise MatrixError('Trying to add matrixes of varying rank')
        ret = Matrix(self.m, self.n)
        for x in range(self.m):
            row = [item[0]-item[1] for item in zip(self.rows[x], mat[x])]
            ret[x] = row
        return(ret)
    def __isub__(self, mat):               # Subtracting this and that matrix
        tempmat = self - mat                                   # Calls __sub__
        self.rows = tempmat.rows[:]     
        return(self)
    
# Multiplying matrices
    def __mul__(self, mat):
        matm, matn = mat.getRank()
        if (self.n != matm):
            raise MatrixError('Matrices cannot be multipled')
        mat_t = mat.getTranspose()
        mulmat = Matrix(self.m, matn)
        for x in range(self.m):
            for y in range(mat_t.m):
                mulmat[x][y] = sum([item[0]*item[1] for item in zip(self.rows[x], mat_t[y])])
        return(mulmat)
    def __imul__(self, mat):                # Multiplying this and that matrix
        tempmat = self * mat                                   # Calls __mul__
        self.rows = tempmat.rows[:]
        self.m, self.n = tempmat.getRank()
        return self

    def save(self, filename):
        open(filename, 'w').write(str(self))
      
# Makes matrix
    @classmethod
    def _makeMatrix(cls, rows):
        m = len(rows)
        n = len(rows[0])
        # Validity check
        if any([len(row) != n for row in rows[1:]]):
            raise MatrixError('Inconsistent row length')
        mat = Matrix(m,n, init=False)
        mat.rows = rows
        return(mat)
        
# Makes random matrix with elements in range low to high
    @classmethod
    def makeRandom(cls, m, n, low=0, high=10):
        obj = Matrix(m, n, init=False)
        for x in range(m):
            obj.rows.append([random.randrange(low, high) for i in range(obj.n)])
        return(obj)

# Makes zero-matrix of rank m x n
    @classmethod
    def makeZero(cls, m, n):
        rows = [[0]*n for x in range(m)]
        return(cls.fromList(rows))

# Makes Identity matrix rank m x n
    @classmethod
    def makeId(cls, m):
        rows = [[0]*m for x in range(m)]
        idx = 0
        for row in rows:
            row[idx] = 1
            idx += 1
        return(cls.fromList(rows))
    
# Read matrix from input
    @classmethod
    def readStdin(cls):
        print('Enter matrix row by row. Type "q" to quit')
        rows = []
        while True:
            line = sys.stdin.readline().strip()
            if line=='q': break
            row = [int(x) for x in line.split()]
            rows.append(row)            
        return(cls._makeMatrix(rows))

# Read matrix from a file
    @classmethod
    def readGrid(cls, fname):
        rows = []
        for line in open(fname).readlines():
            row = [int(x) for x in line.split()]
            rows.append(row)
        return cls._makeMatrix(rows)

# Create matrix by passing a list of lists
    @classmethod
    def fromList(cls, listoflists):
        rows = listoflists[:]
        return cls._makeMatrix(rows)
