
# Tribonacci Sequence

Date: 21-09-2024

## Solution
#### Python
```python
def tribonacci(signature, n):
    if n == 0 :
        return []
    if n < 3:
        return signature[0:n]
    for i in range(n-3):
        signature.append(sum(signature[-3:]))
    return signature
```
        