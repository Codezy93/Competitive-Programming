# 135. Candy

---

There are `n` children standing in a line. Each child is assigned a rating value given in the integer array `ratings`.

You are giving candies to these children subjected to the following requirements:

  * Each child must have at least one candy.
  * Children with a higher rating get more candies than their neighbors.



Return _the minimum number of candies you need to have to distribute the candies to the children_.

 

**Example 1:**


**Input:** ratings = [1,0,2]
**Output:** 5
**Explanation:** You can allocate to the first, second and third child with 2, 1, 2 candies respectively.


**Example 2:**


**Input:** ratings = [1,2,2]
**Output:** 4
**Explanation:** You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.


 

**Constraints:**

  * `n == ratings.length`
  * `1 <= n <= 2 * 104`
  * `0 <= ratings[i] <= 2 * 104`

---

## Solution



---

## Code
```python
class Solution:
  def candy(self, ratings: list[int]) -> int:
    n = len(ratings)
    ans = 0
    l = [1] * n
    r = [1] * n
    for i in range(1, n):
      if ratings[i] > ratings[i - 1]:
        l[i] = l[i - 1] + 1
    for i in range(n - 2, -1, -1):
      if ratings[i] > ratings[i + 1]:
        r[i] = r[i + 1] + 1
    for a, b in zip(l, r):
      ans += max(a, b)
    return ans
```