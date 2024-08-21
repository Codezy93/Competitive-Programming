
# Palindrome String

Date: 21-08-2024

## Solution
#### Python
```python
class Solution:
	def isPalindrome(self, S):
		if S == S[::-1]:
		    return 1
		else:
		    return 0
```
        