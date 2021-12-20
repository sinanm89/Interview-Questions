# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


# | A- | B- | C- | E |
# | S  | F  | C- | S |
# | A  | D- | E- | E |


# Example 1:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        if len(board) > 0:
            if len(board[0]) > 0:
                x, y = len(board[0]), len(board)
            else:
                return False
        else:
            return False


        letter_map = {}

        def look_around(curr_iy, curr_ix, sol_i, stack):
            if sol_i > len(word) - 1:
                return True
            if curr_iy == y or curr_ix == x:
                return None
            # if board[curr_iy][curr_ix] != word[sol_i]:
                # return None

            key = f"{curr_iy}{curr_ix}"
            out = None
            next_sol = word[sol_i]


            #right
            next_key = f"{curr_iy}{curr_ix+1}"
            if curr_ix + 1 < x and board[curr_iy][curr_ix+1] == next_sol and next_key not in stack:
                out = look_around(curr_iy, curr_ix+1, sol_i+1, stack + [key])
                if out:
                    return out
            #down
            next_key = f"{curr_iy+1}{curr_ix}"
            if curr_iy + 1 < y and board[curr_iy+1][curr_ix] == next_sol and next_key not in stack:
                out = look_around(curr_iy+1, curr_ix, sol_i+1, stack + [key])
                if out:
                    return out
            #up
            next_key = f"{curr_iy-1}{curr_ix}"
            if curr_iy - 1 >= 0 and board[curr_iy-1][curr_ix] == next_sol and next_key not in stack:
                out = look_around(curr_iy-1, curr_ix, sol_i+1, stack + [key])
                if out:
                    return out

            #left
            next_key = f"{curr_iy}{curr_ix-1}"
            if curr_ix - 1 >= 0 and board[curr_iy][curr_ix-1] == next_sol and next_key not in stack:
                out = look_around(curr_iy, curr_ix-1, sol_i+1, stack + [key])
                if out:
                    return out

            return out

        ix, iy = 0, 0
        sol_i = 0
        out = None
        stack = []
        while iy < y and ix < x:
            if board[iy][ix] == word[sol_i]:
                out = look_around(iy, ix, sol_i+1, stack)
                if out:
                    return out
            ix += 1
            if ix == len(board[0]):
                ix = 0
                iy += 1
                if iy == len(board):
                    # finish board
                    break
            # print(ix, iy)
        return False


# # Example 1:

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
# Output: true


print(Solution().exist(board, word))


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
# Output: true


print(Solution().exist(board, word))


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
# Output: false


print(Solution().exist(board, word))

board =[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word = "ABCEFSADEESE"
# output : true
print(Solution().exist(board, word))
