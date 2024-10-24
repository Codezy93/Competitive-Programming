# Implement Stack using Array

Date: 2024-10-24 00:00:00

## Solution

#### Python
```python
class MyStack:
    def __init__(self):
        self.arr=[]
    def push(self,data):
        self.arr.insert(0, data)
    def pop(self):
        if len(self.arr) != 0:
            temp = self.arr[0]
            del self.arr[0]
            return temp
        else:
            return -1
 ```