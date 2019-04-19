'''

Coding problem: 

https://leetcode.com/problems/add-digits/

Submission stats: 

    Runtime: 40 ms, faster than 99.77% of Python3 online submissions for Add Digits.
    Memory Usage: 13.3 MB, less than 5.82% of Python3 online submissions for Add Digits.

'''

class Solution:   
    def addDigits(self, num):
        while num > 9:
            num =sum(list(map(int,str(num))))
        return num
