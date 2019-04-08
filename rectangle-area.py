# Find the total area covered by two rectilinear rectangles in a 2D plane.

# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

# Rectangle Area
# They intersect at 0,0 and 3,2

# Example:

# Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
# Output: 45
# Note:

# Assume that the total area is never beyond the maximum possible value of int.


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        # Initialize coordinates of two rectangles
        lower1 = (A, B)
        upper1 = (C, D)

        lower2 = (E, F)
        upper2 = (G, H)

        # Check if two x-axis meet
        x_coords = [A, C, E, G]
        x_coords.sort()

        y_coords = [B, D, F, H]
        y_coords.sort()

        common_area = -1

      #  print(x_coords)
        if((x_coords[0:2] == [A, C] or x_coords[0:2] == [C, A]) or (x_coords[0:2] == [E, G] or x_coords[0:2] == [G, E])):
            common_area = 0

        if((y_coords[0:2] == [B, D] or y_coords[0:2] == [D, B]) or (y_coords[0:2] == [F, H] or y_coords[0:2] == [H, F])):
            common_area = 0

        if(common_area == -1):
            # Compute common area
            common_area = self.getArea(
                (x_coords[1], y_coords[1]), (x_coords[2], y_coords[2]))

        return self.getArea(lower1, upper1)+self.getArea(lower2, upper2)-common_area

    def getArea(self, node1, node2):
        return abs(node1[0]-node2[0])*abs(node1[1]-node2[1])


s = Solution()

print(s.computeArea(A=-2, B=-2, C=2, D=2, E=3, F=3, G=4, H=4))
