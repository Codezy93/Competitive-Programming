# Print Linked List Elements

Date: 2024-11-09 19:13:28.406394

## Solution

#### Python
```python
class Solution:
    def display(self, head):
        while head:
            print(head.data, end=" ")
            head = head.next
 ```