# 2325. Decode the Message

---

You are given the strings `key` and `message`, which represent a cipher key and a secret message, respectively. The steps to decode `message` are as follows:

  1. Use the **first ** appearance of all 26 lowercase English letters in `key` as the **order ** of the substitution table.
  2. Align the substitution table with the regular English alphabet.
  3. Each letter in `message` is then **substituted ** using the table.
  4. Spaces `' '` are transformed to themselves.


  * For example, given `key = "_ **hap **_ p _ **y **_ _ **bo **_ y"` (actual key would have **at least one ** instance of each letter in the alphabet), we have the partial substitution table of (`'h' -> 'a'`, `'a' -> 'b'`, `'p' -> 'c'`, `'y' -> 'd'`, `'b' -> 'e'`, `'o' -> 'f'`).



Return _the decoded message_.

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2022/05/08/ex1new4.jpg)


**Input:** key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
**Output:** "this is a secret"
**Explanation:** The diagram above shows the substitution table.
It is obtained by taking the first appearance of each letter in "_ **the **_ _ **quick **_ _ **brown **_ _ **f **_ o _ **x **_ _ **j **_ u _ **mps **_ o _ **v **_ er the _ **lazy **_ _ **d **_ o _ **g **_ ".


**Example 2:**

![](https://assets.leetcode.com/uploads/2022/05/08/ex2new.jpg)


**Input:** key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
**Output:** "the five boxing wizards jump quickly"
**Explanation:** The diagram above shows the substitution table.
It is obtained by taking the first appearance of each letter in "_ **eljuxhpwnyrdgtqkviszcfmabo **_ ".


 

**Constraints:**

  * `26 <= key.length <= 2000`
  * `key` consists of lowercase English letters and `' '`.
  * `key` contains every letter in the English alphabet (`'a'` to `'z'`) **at least once **.
  * `1 <= message.length <= 2000`
  * `message` consists of lowercase English letters and `' '`.

---

## Solution



---

## Code
```python


```