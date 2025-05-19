# 3024. Type of Triangle

---

You are given a **0-indexed ** integer array `nums` of size `3` which can form the sides of a triangle.

  * A triangle is called **equilateral ** if it has all sides of equal length.
  * A triangle is called **isosceles ** if it has exactly two sides of equal length.
  * A triangle is called **scalene ** if all its sides are of different lengths.



Return _a string representing_ _the type of triangle that can be formed_ _or_`"none"`_if it **cannot ** form a triangle._

 

**Example 1:**


**Input:** nums = [3,3,3]
**Output:** "equilateral"
**Explanation:** Since all the sides are of equal length, therefore, it will form an equilateral triangle.


**Example 2:**


**Input:** nums = [3,4,5]
**Output:** "scalene"
**Explanation:** 
nums[0] + nums[1] = 3 + 4 = 7, which is greater than nums[2] = 5.
nums[0] + nums[2] = 3 + 5 = 8, which is greater than nums[1] = 4.
nums[1] + nums[2] = 4 + 5 = 9, which is greater than nums[0] = 3. 
Since the sum of the two sides is greater than the third side for all three cases, therefore, it can form a triangle.
As all the sides are of different lengths, it will form a scalene triangle.


 

**Constraints:**

  * `nums.length == 3`
  * `1 <= nums[i] <= 100`

---

## Solution



---

## Code
```python
class Solution:
    def checkTriangle(self, sides):
        a = sides[0]
        b = sides[1]
        c = sides[2]
        if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
            return True
        else:
            return False
    def triangleType(self, sides: List[int]) -> str:
        if self.checkTriangle(sides):
            a = sides[0]
            b = sides[1]
            c = sides[2]
            if a==b and b==c and c==a:
                return 'equilateral'
            elif a==b or b==c or c==a:
                return 'isosceles'
            else:
                return 'scalene'
        return 'none'
```