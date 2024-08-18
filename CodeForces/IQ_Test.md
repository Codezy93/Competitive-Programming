
# IQ Test

Date: 18-08-2024

## Solution
#### Python
```python
even = []
odd = []
length = int(input())
nums = [int(x) for x in input().split()]
if len(nums) > 2:
    for i in range(3):
        if nums[i]%2 == 0:
            even.append(nums[i])
        else:
            odd.append(nums[i])
if len(even) > len(odd):
    for x, i in enumerate(nums):
        if i%2 != 0:
            print(x+1)
else:
    for x, i in enumerate(nums):
        if i%2==0:
            print(x+1)
```
        