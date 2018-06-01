# 240. Search a 2D Matrix II

# A little tricky.
# 2-D binary search.
# Divide matrix into four blocks and recursively do the search for each block. 

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        elif m == 1:
            for i in range(len(matrix[0])):
                if matrix[0][i] == target:
                    return True
            return False
            
        n = len(matrix[0])

        if n == 1:
            for i in range(m):
                if matrix[i][0] == target:
                    return True
            return False

        m_mid = int((m - 1) / 2)
        n_mid = int((n - 1) / 2)

        if matrix[0][0] > target or matrix[m - 1][n - 1] < target:
            return False
        
        if matrix[0][0] <= target and matrix[m_mid][n_mid] >= target:
            new_m = self.copyMatrix(matrix, 0, m_mid, 0, n_mid)
            a1 = self.searchMatrix(new_m, target)
        else:
            a1 = False
            
        if matrix[m_mid + 1][n_mid +1] <= target and matrix[m - 1][n - 1] >= target:
            new_m = self.copyMatrix(matrix, m_mid + 1, m - 1, n_mid + 1, n - 1)
            a2 = self.searchMatrix(new_m, target)
        else:
            a2 = False
            
        if matrix[m_mid + 1][0] <= target and matrix[m - 1][n_mid] >= target:
            new_m = self.copyMatrix(matrix, m_mid + 1, m - 1, 0, n_mid)
            a3 = self.searchMatrix(new_m, target)
        else:
            a3 = False
            
        if matrix[0][n_mid] <= target and matrix[m_mid][n - 1] >= target:
            new_m = self.copyMatrix(matrix, 0, m_mid, n_mid + 1, n - 1)
            a4 = self.searchMatrix(new_m, target)
        else:
            a4 = False
        
        
        return a1 or a2 or a3 or a4

    def copyMatrix(self, matrix, m_l, m_h, n_l, n_h):

        return [[matrix[i][j] for j in range(n_l, n_h + 1)] for i in range(m_l, m_h + 1)]
