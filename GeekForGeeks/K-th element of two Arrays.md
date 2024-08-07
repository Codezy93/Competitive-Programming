# K-th element of two Arrays

Date: 07-08-2024

## Solution
#### Python
```python
class Solution:
    def kthElement(self, k, arr1, arr2):
        arr1 = arr1 + arr2
        arr1.sort()
        return arr1[k-1]

def main():
    T = int(input())
    while (T > 0):
        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(k, a, b))
        T -= 1
if __name__ == "__main__":
    main()
```