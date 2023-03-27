# -*- coding: utf-8 -*-
"""Sequence_Allignment_Using_Needleman_Wunsch_Algorithm

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fNTfWt6dJWpyq4SQuMY4JsMGxqlFyso5
"""

import numpy as np

seq_1 = input("Enter 1st sequence:")
seq_2 = input("Enter 2nd sequence:")

matrix1 = np.zeros((len(seq_1)+1,len(seq_2)+1))
matrix2 = np.zeros((len(seq_1),len(seq_2)))

match = 1
mismatch = -1
gap = -2

for i in range(len(seq_1)):
  for j in range(len(seq_2)):
    if seq_1[i] == seq_2[j]:
      matrix2[i][j]= match
    
    else:
      matrix2[i][j]=mismatch


#Matrix initialization

for i in range(len(seq_1)+1):
  matrix1[i][0]=i*gap

for j in range(len(seq_1)+1):
  matrix1[0][j]=j * gap

#Matrix Filling
for i in range(1,len(seq_1)+1):
  for j in range(1,len(seq_1)+1):

    matrix1[i][j] = max(matrix1[i-1][j-1]+matrix2[i-1][j-1],matrix1[i-1][j]+gap,matrix1[i][j-1]+gap)

print("Matrix:\n",matrix1)


aligned_1=""
aligned_2=""

ti = len(seq_1)
tj = len(seq_2)

while(ti > 0 and tj > 0):
  if(matrix1[ti][tj] == matrix1[ti-1][tj-1]+matrix2[ti-1][tj-1]):
    matrix2[i][j]= mismatch

#matrix initialisation
for i in range(len(seq_1)+1):
  matrix1[i][0]=i*gap
for j in range(len(seq_2)+1):
  matrix1[0][j]=j*gap

#matrix filling
for i in range(1,len(seq_1)+1):
  for j in range(1,len(seq_2)+1):
    matrix1[i][j]=max(matrix1[i-1][j-1]+matrix2[i-1][j-1],
                      matrix1[i-1][j]+gap,
                      matrix1[i][j-1]+gap)
    print("Matrix:\n",matrix1)

#traceback
aligned_1=""
aligned_2=""
ti=len(seq_1)
tj=len(seq_2)
while(ti>0 and tj>0):
  if(matrix1[ti][tj]==matrix1[ti-1][tj-1]+matrix2[ti-1][tj-1]):
    aligned_1=seq_1[ti-1]+aligned_1
    aligned_2=seq_2[tj-1]+aligned_2

    ti=ti-1
    tj=tj-1

  elif(matrix1[ti][tj]==matrix1[ti-1][tj]+gap):
      aligned_1=seq_1[ti-1]+aligned_1
      aligned_2="_"+aligned_2

      ti=ti-1
  else:
     aligned_1="_"+aligned_1
     aligned_2=seq_2[tj-1]+aligned_2 
     tj=tj-1

print("alignment of sequence 1 \n",aligned_1)
print("alignment of sequence 2 \n",aligned_2)