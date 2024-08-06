# Valid Palindrome

Platform: LeetCode

Date: 05/08/2024

## Problem
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

## Input
A string consisting of n chacters

## Output
Boolean based on validity as palindrome

## Solution
```python
import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        allowed = string.ascii_lowercase + string.digits
        s = s.lower()
        s = s.replace(" ", "")
        word = ""
        for i in s:
            if i in allowed:
                word += i
        if word == word[::-1]:
            return True
        else:
            return False
```