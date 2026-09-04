class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # split into mn/2 each time 
        # each row is greater than the last row 

        m_len = len(matrix)
        n_len = len(matrix[0])

        l_r = l_c = 0
        r_r, r_c = m_len - 1, n_len - 1

        while l_r <= r_r and l_c <= r_c:
            m_r = l_r + ((r_r - l_r) // 2)

            m_c = l_c + ((r_c - l_c) // 2)

            if matrix[m_r][m_c] == target:
                return True
            elif target < matrix[m_r][m_c]:
                if m_c == 0: 
                    r_c = n_len - 1
                    r_r -= 1
                else:
                    r_c = m_c - 1
            elif target > matrix[m_r][m_c]:
                if m_c == n_len - 1:
                    l_c = 0
                    l_r += 1
                else:
                    l_c = m_c + 1
        
        return False   