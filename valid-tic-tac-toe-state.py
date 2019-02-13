# A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

# The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

# Here are the rules of Tic-Tac-Toe:

# Players take turns placing characters into empty squares (" ").
# The first player always places "X" characters, while the second player always places "O" characters.
# "X" and "O" characters are always placed into empty squares, never filled ones.
# The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
# Example 1:
# Input: board = ["O  ", "   ", "   "]
# Output: false
# Explanation: The first player always plays "X".

# Example 2:
# Input: board = ["XOX", " X ", "   "]
# Output: false
# Explanation: Players take turns making moves.

# Example 3:
# Input: board = ["XXX", "   ", "OOO"]
# Output: false

# Example 4:
# Input: board = ["XOX", "O O", "XOX"]
# Output: true
# Note:

# board is a length-3 array of strings, where each string board[i] has length 3.
# Each board[i][j] is a character in the set {" ", "X", "O"}.
class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        # Rules
        # Atmost 5 X and 4 Os
        # At any step we have either equal X and Os or 1 extra X than O
        # Either X or O can be in a winning position at any time

        game=''.join(board)
        winning_moves=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

        # Check for X and O count
        x_count=game.count('X')
        o_count=game.count('O')

        if(o_count>x_count or x_count-o_count>1):
            return False
        
        x_win=False
        o_win=False
        
        for move in winning_moves:
            if(game[move[0]]==game[move[1]]==game[move[2]]=='X'):
                x_win=True
            elif(game[move[0]]==game[move[1]]==game[move[2]]=='O'):
                o_win=True
        
        if(x_win and o_win):
            return False
        if(x_win):
            return x_count-o_count==1
        if(o_win):
            return x_count==o_count


        return True
        
s=Solution()
print(s.validTicTacToe(["OOO","OXX","XX "]))
