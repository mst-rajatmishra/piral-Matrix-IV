# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # Extract values from the linked list
        values = []
        while head:
            values.append(head.val)
            head = head.next
        
        # Initialize the matrix with -1
        matrix = [[-1] * n for _ in range(m)]
        
        # Directions for moving in the spiral: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Fill the matrix in spiral order
        x, y = 0, 0
        direction_index = 0
        
        for value in values:
            matrix[x][y] = value
            # Move to the next cell in the current direction
            next_x, next_y = x + directions[direction_index][0], y + directions[direction_index][1]
            
            # Check if we need to change direction
            if not (0 <= next_x < m and 0 <= next_y < n and matrix[next_x][next_y] == -1):
                # Change direction
                direction_index = (direction_index + 1) % 4
                next_x, next_y = x + directions[direction_index][0], y + directions[direction_index][1]
            
            # Update position
            x, y = next_x, next_y
        
        return matrix
