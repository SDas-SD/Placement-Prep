# You are given A, B and C .
# Calculate the value of (A ^ B) % C

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        c = A**B
        return c%C