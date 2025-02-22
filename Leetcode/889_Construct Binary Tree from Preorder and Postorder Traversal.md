# 889. Construct Binary Tree from Preorder and Postorder Traversal

---

Given two integer arrays, `preorder` and `postorder` where `preorder` is the preorder traversal of a binary tree of **distinct ** values and `postorder` is the postorder traversal of the same tree, reconstruct and return _the binary tree_.

If there exist multiple answers, you can **return any ** of them.

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/07/24/lc-prepost.jpg)


**Input:** preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
**Output:** [1,2,3,4,5,6,7]


**Example 2:**


**Input:** preorder = [1], postorder = [1]
**Output:** [1]


 

**Constraints:**

  * `1 <= preorder.length <= 30`
  * `1 <= preorder[i] <= preorder.length`
  * All the values of `preorder` are **unique **.
  * `postorder.length == preorder.length`
  * `1 <= postorder[i] <= postorder.length`
  * All the values of `postorder` are **unique **.
  * It is guaranteed that `preorder` and `postorder` are the preorder traversal and postorder traversal of the same binary tree.

---

## Solution



---

## Code
```python
class Solution:
  def constructFromPrePost(self,pre: list[int],post: list[int],) -> TreeNode | None:
    postToIndex = {num: i for i, num in enumerate(post)}
    def build(preStart: int, preEnd: int, postStart: int, postEnd: int) -> TreeNode | None:
      if preStart > preEnd:
        return None
      if preStart == preEnd:
        return TreeNode(pre[preStart])
      rootVal = pre[preStart]
      leftRootVal = pre[preStart + 1]
      leftRootPostIndex = postToIndex[leftRootVal]
      leftSize = leftRootPostIndex - postStart + 1
      root = TreeNode(rootVal)
      root.left = build(preStart + 1, preStart + leftSize,
                        postStart, leftRootPostIndex)
      root.right = build(preStart + leftSize + 1, preEnd,
                         leftRootPostIndex + 1, postEnd - 1)
      return root
    return build(0, len(pre) - 1, 0, len(post) - 1)
```