class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        grid_sets = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue

                grid_index = (i // 3) * 3 + (j // 3)

                if num in row_sets[i] or num in col_sets[j] or num in grid_sets[grid_index]:
                    return False

                row_sets[i].add(num)
                col_sets[j].add(num)
                grid_sets[grid_index].add(num)

        return True