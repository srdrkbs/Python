"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

solution :
 using four loops, every  for loop defines the direction along the matrix.
 The first for loop represents the movement from left to right, whereas the second crawl represents the movement from top to bottom,
 the third represents the movement from the right to left, and the fourth represents the movement from bottom to up.
"""

class Solution(object):
    def spiralOrder(self, matrix):  #time complexity: O(n)
        row_start = 0
        row_end = len(matrix)
        col_start = 0
        col_end = len(matrix[0])
        spiral = []
        while row_start < row_end and col_start < col_end:
            # left to right
            for idx in range(col_start, col_end):
                spiral.append(matrix[row_start][idx])
            row_start += 1

            # top to bottom
            for idx in range(row_start, row_end):
                spiral.append(matrix[idx][col_end - 1])
            col_end -= 1

            # right to left
            if row_start < row_end:
                for idx in range(col_end - 1, col_start - 1, -1):
                    spiral.append(matrix[row_end - 1][idx])
                row_end -= 1

            # bottom to top
            if col_start < col_end:
                for idx in range(row_end - 1, row_start - 1, -1):
                    spiral.append(matrix[idx][col_start])
                col_start += 1
        return spiral