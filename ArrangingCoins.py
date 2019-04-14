'''

Coding Problem: 

Statistics: 

  Runtime: 40 ms, faster than 100.00% of Python3 online submissions for Arranging Coins.
  Memory Usage: 13.2 MB, less than 5.17% of Python3 online submissions for Arranging Coins.

'''

import math
class Solution:
    def arrangeCoins(self, n):
        return int(-0.5 + math.sqrt(1 * 2 * n + 0.25))
