# 391. Perfect Rectangle

---

Given an array `rectangles` where `rectangles[i] = [xi, yi, ai, bi]` represents an axis-aligned rectangle. The bottom-left point of the rectangle is `(xi, yi)` and the top-right point of it is `(ai, bi)`.

Return `true` _if all the rectangles together form an exact cover of a rectangular region_.

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/27/perectrec1-plane.jpg)


**Input:** rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
**Output:** true
**Explanation:** All 5 rectangles together form an exact cover of a rectangular region.


**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/27/perfectrec2-plane.jpg)


**Input:** rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
**Output:** false
**Explanation:** Because there is a gap between the two rectangular regions.


**Example 3:**

![](https://assets.leetcode.com/uploads/2021/03/27/perfecrrec4-plane.jpg)


**Input:** rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
**Output:** false
**Explanation:** Because two of the rectangles overlap with each other.


 

**Constraints:**

  * `1 <= rectangles.length <= 2 * 104`
  * `rectangles[i].length == 4`
  * `-105 <= xi < ai <= 105`
  * `-105 <= yi < bi <= 105`

---

## Solution



---

## Code
```python


```