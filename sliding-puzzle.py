# On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

# A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

# The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

# Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

# Examples:

# Input: board = [[1,2,3],[4,0,5]]
# Output: 1
# Explanation: Swap the 0 and the 5 in one move.
# Input: board = [[1,2,3],[5,4,0]]
# Output: -1
# Explanation: No number of moves will make the board solved.
# Input: board = [[4,1,2],[5,0,3]]
# Output: 5
# Explanation: 5 is the smallest number of moves that solves the board.
# An example path:
# After move 0: [[4,1,2],[5,0,3]]
# After move 1: [[4,1,2],[0,5,3]]
# After move 2: [[0,1,2],[4,5,3]]
# After move 3: [[1,0,2],[4,5,3]]
# After move 4: [[1,2,0],[4,5,3]]
# After move 5: [[1,2,3],[4,5,0]]
# Input: board = [[3,2,4],[1,5,0]]
# Output: 14


class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        target = '123450'
        start = ''

        # Load the start
        for i in range(len(board)):
            start = start+''.join(map(str, board[i]))

        # Initialize adjacency matrix
        adj_matrix = {0: [1, 3], 1: [0, 2, 4], 2: [
            1, 5], 3: [0, 4], 4: [1, 3, 5], 5: [2, 4]}

        # Initialize step counter

        # Initialize the visited queue
        # Initialize the looping queue

        # Load the queue with initial position

        # Loop queue till it is empty
        # For each loop, if queue value is equal to target
        # Break

        # Else
        # Get index of 0
        # Get the adjacent swapping positions

        # For each position
        # If not present in visited matrix, add it to looping queue

        # Increment the step counter

        # If step counter is 0, return -1
        # Else return step counter


s = Solution()
print(s.slidingPuzzle([[1, 2, 3], [4, 5, 0]]))
