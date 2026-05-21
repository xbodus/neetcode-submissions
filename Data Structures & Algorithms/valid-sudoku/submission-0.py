class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = set()
        col_set = {
            0: set(),
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set(),
            6: set(),
            7: set(),
            8: set()
        }
        grid_set = {
            0: set(), # Rows 1-3 Cols 1-3
            1: set(), # Rows 1-3 Cols 4-6
            2: set(), # Rows 1-3 Cols 7-9
            3: set(), # Rows 4-6 Cols 1-3
            4: set(), # Rows 4-6 Cols 4-6
            5: set(), # Rows 4-6 Cols 7-9
            6: set(), # Rows 7-9 Cols 1-3
            7: set(), # Rows 7-9 Cols 4-6
            8: set() # Rows 7-9 Cols 7-9
        }

        # Check rows and cols
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num == ".":
                    continue

                if num in row_set or num in col_set[j]:
                    return False
                
                row_set.add(num)
                col_set[j].add(num)

            row_set.clear()
        
        # Chunk grid
        chunk = 0
        for i, row in enumerate(board):
            if i and i % 3 == 0:
                chunk += 1 

            pointer = 3 * chunk
            for j, num in enumerate(row):
                if j and j % 3 == 0:
                    pointer += 1
                
                if num == ".":
                    continue

                if num in grid_set[pointer]:
                    return False

                grid_set[pointer].add(num)

        return True