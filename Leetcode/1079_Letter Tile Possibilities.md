# 1079. Letter Tile Possibilities

---

You have `n`  `tiles`, where each tile has one letter `tiles[i]` printed on it.

Return _the number of possible non-empty sequences of letters_ you can make using the letters printed on those `tiles`.

 

**Example 1:**


**Input:** tiles = "AAB"
**Output:** 8
**Explanation:** The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".


**Example 2:**


**Input:** tiles = "AAABBC"
**Output:** 188


**Example 3:**


**Input:** tiles = "V"
**Output:** 1


 

**Constraints:**

  * `1 <= tiles.length <= 7`
  * `tiles` consists of uppercase English letters.

---

## Solution



---

## Code
```python
class Solution:
  def numTilePossibilities(self, tiles: str) -> int:
    count = collections.Counter(tiles)
    def dfs(count: dict[int, int]) -> int:
      possibleSequences = 0
      for k, v in count.items():
        if v == 0:
          continue
        count[k] -= 1
        possibleSequences += 1 + dfs(count)
        count[k] += 1
      return possibleSequences
    return dfs(count)
```