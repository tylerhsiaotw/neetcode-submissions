import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = collections.defaultdict(set)
        c = collections.defaultdict(set)
        sub_box = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                elif (val in r[i] or val in c[j] or val in sub_box[(i // 3, j // 3)]):
                    return False
                else:
                    r[i].add(val)
                    c[j].add(val)
                    sub_box[(i // 3, j // 3)].add(val)
        return True