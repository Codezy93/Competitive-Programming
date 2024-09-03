
# Type of Triangle

Date: 03-09-2024

## Solution
#### Python
```python
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a,b,c = map(int, nums)
        if a==b and b==c and a>0:
            return "equilateral"
        elif a+b>c and b+c>a and c+a>b:
            if a==b or a==c or b==c:
                return "isosceles"
            else:
                return "scalene"
        else:
            return "none"
```
        