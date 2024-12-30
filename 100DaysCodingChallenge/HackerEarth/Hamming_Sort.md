
# Hamming Sort

Date: 09-09-2024

## Solution
#### Python
```python
def hamming_distance(a, b):
    return bin(a ^ b).count('1')
def solve(N, K, A):
    sorted_A = sorted(A, key=lambda x: (hamming_distance(x, K), x))
    return sorted_A
T = int(input())
for _ in range(T):
    custom_input_1 = list(map(str, input().split()))
    N = int(custom_input_1[0])
    K = int(custom_input_1[1])
    A = list(map(int, input().split()))

    out_ = solve(N, K, A)
    print (' '.join(map(str, out_)))
```
        