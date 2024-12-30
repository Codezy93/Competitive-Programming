# Die Roll

Date: 2024-10-16 17:49:38.584114

## Solution

#### Python
```python
Y, W = map(int, input().split(" "))
probability = ["", "1/1", "5/6", "2/3", "1/2", "1/3", "1/6"]
D = max(Y, W);
print(probability[D])
 ```