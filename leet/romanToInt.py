"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together.
12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.


"""


class Solution:
    mappings = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        if any([c for c in s if c not in self.mappings.keys()]):
            return 0
        res = 0
        i = len(s) - 1
        while i >= 0:
            if i == 0:
                res += self.mappings[s[i]]
                break

            r0 = s[i]
            r1 = s[i-1]

            # subtraction case:
            if self.mappings[r1] < self.mappings[r0]:
                res = res + (self.mappings[r0] - self.mappings[r1])
                i = i - 2

            # otherwise add the mapping (already contains "multiplier" effect)
            else:
                res += self.mappings[r0]
                i = i - 1

        return res



    """
    read from right to left
    - read rightmost char (r0) and the next rightmost char (r1)
    - if r1 < r0 (ie IX, IV...)
        - next dig = mappings[r0] - mappings[r1] (V-I etc)
        - r0 = move left 2 spaces, r1 = move left 2 spaces
    - else
        - next dig = mappings[r0]
        - r0 = r1
        - r1 = move left one space
        
        
    
    
    
    """


s = Solution()
assert s.romanToInt('LVIII') == 58

assert s.romanToInt('III') == 3
assert s.romanToInt('IV') == 4
assert s.romanToInt('VII') == 7
assert s.romanToInt('LVIII') == 58


