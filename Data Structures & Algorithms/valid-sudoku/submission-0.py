class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # 9 hashmaps for sub-boxes
        # 9 hashmaps for rows
        # 9 hashmaps for columns

        # hashmap[row][col] = {{}, {}, ....}

        for row in range(9):
            seen = set()
            for col in range(9):
                if board[row][col] in seen:
                    return False
                elif board[row][col] == ".":
                    continue
                else:
                    seen.add(board[row][col])

        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] in seen:
                    return False
                elif board[row][col] == ".":
                    continue
                else:
                    seen.add(board[row][col])

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3  + j

                    if board[row][col] in seen:
                        return False
                    elif board[row][col] == ".":
                        continue
                    else:
                        seen.add(board[row][col])

        return True



