# 1964. Find the Longest Valid Obstacle Course at Each Position

---

You want to build some obstacle courses. You are given a **0-indexed ** integer array `obstacles` of length `n`, where `obstacles[i]` describes the height of the `ith` obstacle.

For every index `i` between `0` and `n - 1` (**inclusive **), find the length of the **longest obstacle course ** in `obstacles` such that:

  * You choose any number of obstacles between `0` and `i` **inclusive **.
  * You must include the `ith` obstacle in the course.
  * You must put the chosen obstacles in the **same order ** as they appear in `obstacles`.
  * Every obstacle (except the first) is **taller ** than or the **same height ** as the obstacle immediately before it.



Return _an array_ `ans` _of length_ `n`, _where_ `ans[i]` _is the length of the **longest obstacle course ** for index_ `i` _as described above_.

 

**Example 1:**


**Input:** obstacles = [1,2,3,2]
**Output:** [1,2,3,3]
**Explanation:** The longest valid obstacle course at each position is:
- i = 0: [_1_], [1] has length 1.
- i = 1: [_1_ ,_2_], [1,2] has length 2.
- i = 2: [_1_ ,_2_ ,_3_], [1,2,3] has length 3.
- i = 3: [_1_ ,_2_ ,3,_2_], [1,2,2] has length 3.


**Example 2:**


**Input:** obstacles = [2,2,1]
**Output:** [1,2,1]
**Explanation:** The longest valid obstacle course at each position is:
- i = 0: [_2_], [2] has length 1.
- i = 1: [_2_ ,_2_], [2,2] has length 2.
- i = 2: [2,2,_1_], [1] has length 1.


**Example 3:**


**Input:** obstacles = [3,1,5,6,4,2]
**Output:** [1,1,2,3,2,2]
**Explanation:** The longest valid obstacle course at each position is:
- i = 0: [_3_], [3] has length 1.
- i = 1: [3,_1_], [1] has length 1.
- i = 2: [_3_ ,1,_5_], [3,5] has length 2. [1,5] is also valid.
- i = 3: [_3_ ,1,_5_ ,_6_], [3,5,6] has length 3. [1,5,6] is also valid.
- i = 4: [_3_ ,1,5,6,_4_], [3,4] has length 2. [1,4] is also valid.
- i = 5: [3,_1_ ,5,6,4,_2_], [1,2] has length 2.


 

**Constraints:**

  * `n == obstacles.length`
  * `1 <= n <= 105`
  * `1 <= obstacles[i] <= 107`

---

## Solution



---

## Code
```python


```