# 1787. Make the XOR of All Segments Equal to Zero

---

You are given an array `nums`​​​ and an integer `k`​​​​​. The XOR of a segment `[left, right]` where `left <= right` is the `XOR` of all the elements with indices between `left` and `right`, inclusive: `nums[left] XOR nums[left+1] XOR ... XOR nums[right]`.

Return _the minimum number of elements to change in the array_ such that the `XOR` of all segments of size `k`​​​​​​ is equal to zero.

 

**Example 1:**


**Input:** nums = [1,2,0,3,0], k = 1
**Output:** 3
**Explanation:** Modify the array from [_ **1 **_ ,_ **2 **_ ,0,_ **3 **_ ,0] to from [_ **0 **_ ,_ **0 **_ ,0,_ **0 **_ ,0].


**Example 2:**


**Input:** nums = [3,4,5,2,1,7,3,4,7], k = 3
**Output:** 3
**Explanation:** Modify the array from [3,4,**_5_ ** ,**_2_ ** ,**_1_ ** ,7,3,4,7] to [3,4,**_7_ ** ,**_3_ ** ,**_4_ ** ,7,3,4,7].


**Example 3:**


**Input:** nums = [1,2,4,1,2,5,1,2,6], k = 3
**Output:** 3
**Explanation:** Modify the array from [1,2,**_4,_ ** 1,2,**_5_ ** ,1,2,**_6_ **] to [1,2,**_3_ ** ,1,2,**_3_ ** ,1,2,**_3_ **].

 

**Constraints:**

  * `1 <= k <= nums.length <= 2000`
  * `​​​​​​0 <= nums[i] < 210`

---

## Solution



---

## Code
```python


```