
# Moving Zeros To End

Date: 14-08-2024

## Solution
#### Python
```python
def move_zeros(lst):
    zeros = lst.count(0)
    while 0 in lst:
        lst.remove(0)
    for i in range(zeros):
        lst.append(0)
    return lst
```
        