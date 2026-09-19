import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxs = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                if (val in rows[i] or val in cols[j] or val in boxs[(i // 3, j // 3)]):
                    return False
                else:
                    rows[i].add(val)
                    cols[j].add(val)
                    boxs[(i//3,j//3)].add(val)
        return True        
        