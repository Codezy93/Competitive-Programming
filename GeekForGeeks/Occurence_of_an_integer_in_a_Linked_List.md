# Occurence of an integer in a Linked List

Date: 2024-10-29 00:00:00

## Solution

#### Python
```python
class Solution:
    def count(self, head, key):
        count = 0
        while head:
            if head.data == key:
                count += 1
            head = head.next
        return count
 ```