# Print the Elements of a Linked List

Date: 2024-10-26 18:21:47.060623

## Solution

#### Python
```python
def printLinkedList(head):
    while head:
        print(head.data)
        head = head.next
 ```