# 2332. The Latest Time to Catch a Bus

---

You are given a **0-indexed ** integer array `buses` of length `n`, where `buses[i]` represents the departure time of the `ith` bus. You are also given a **0-indexed ** integer array `passengers` of length `m`, where `passengers[j]` represents the arrival time of the `jth` passenger. All bus departure times are unique. All passenger arrival times are unique.

You are given an integer `capacity`, which represents the **maximum ** number of passengers that can get on each bus.

When a passenger arrives, they will wait in line for the next available bus. You can get on a bus that departs at `x` minutes if you arrive at `y` minutes where `y <= x`, and the bus is not full. Passengers with the **earliest ** arrival times get on the bus first.

More formally when a bus arrives, either:

  * If `capacity` or fewer passengers are waiting for a bus, they will **all ** get on the bus, or
  * The `capacity` passengers with the **earliest ** arrival times will get on the bus.



Return _the latest time you may arrive at the bus station to catch a bus_. You **cannot ** arrive at the same time as another passenger.

**Note:** The arrays `buses` and `passengers` are not necessarily sorted.

 

**Example 1:**


**Input:** buses = [10,20], passengers = [2,17,18,19], capacity = 2
**Output:** 16
**Explanation:** Suppose you arrive at time 16.
At time 10, the first bus departs with the 0th passenger. 
At time 20, the second bus departs with you and the 1st passenger.
Note that you may not arrive at the same time as another passenger, which is why you must arrive before the 1st passenger to catch the bus.

**Example 2:**


**Input:** buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2
**Output:** 20
**Explanation:** Suppose you arrive at time 20.
At time 10, the first bus departs with the 3rd passenger. 
At time 20, the second bus departs with the 5th and 1st passengers.
At time 30, the third bus departs with the 0th passenger and you.
Notice if you had arrived any later, then the 6th passenger would have taken your seat on the third bus.

 

**Constraints:**

  * `n == buses.length`
  * `m == passengers.length`
  * `1 <= n, m, capacity <= 105`
  * `2 <= buses[i], passengers[i] <= 109`
  * Each element in `buses` is **unique **.
  * Each element in `passengers` is **unique **.

---

## Solution



---

## Code
```python
class Solution:
  def minimumScore(self, nums: list[int], edges: list[list[int]]) -> int:
    n = len(nums)
    xors = functools.reduce(operator.xor, nums)
    subXors = nums[:]
    tree = [[] for _ in range(n)]
    children = [{i} for i in range(n)]
    for u, v in edges:
      tree[u].append(v)
      tree[v].append(u)
    def dfs(u: int, prev: int) -> tuple[int, set[int]]:
      for v in tree[u]:
        if v == prev:
          continue
        vXor, vChildren = dfs(v, u)
        subXors[u] ^= vXor
        children[u] |= vChildren
      return subXors[u], children[u]
    dfs(0, -1)
    ans = math.inf
    for i in range(len(edges)):
      a, b = edges[i]
      if b in children[a]:
        a, b = b, a
      for j in range(i):
        c, d = edges[j]
        if d in children[c]:
          c, d = d, c
        if c in children[a] and a != c:
          cands = [subXors[c], subXors[a] ^ subXors[c], xors ^ subXors[a]]
        elif a in children[c] and a != c:
          cands = [subXors[a], subXors[c] ^ subXors[a], xors ^ subXors[c]]
        else:
          cands = [subXors[a], subXors[c], xors ^ subXors[a] ^ subXors[c]]
        ans = min(ans, max(cands) - min(cands))
    return ans
```
