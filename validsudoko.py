class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #for rows

        for i in range(9):
            visited = set()
            for j in range(9):
                if board[i][j] in visited:
                    return False
                elif board[i][j] != '.':
                    visited.add(board[i][j]) 



        #for columns

        for i in range(9):
            visited = set()
            for j in range(9):
                if board[j][i] in visited:
                    return False
                elif board[j][i] != '.':
                    visited.add(board[j][i]) 

        #for boxes

        start = [(0,0),(0,3),(0,6),
                (3,0),(3,3),(3,6),
                (6,0),(6,3),(6,6)]
        for i,j in start:
            s = set()
            for rows in range(i,i+3):
                for col in range(j,j+3):
                    if board[rows][col] in s:
                        return False
                    elif board[rows][col] != '.':
                        s.add(board[rows][col])
        return True

