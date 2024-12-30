# Bouncing Balls

Date: 2024-11-12 22:19:35.073070

## Solution

#### Python
```python
def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    count = 0
    while h > window:
        h *= bounce
        count += 2
    return count-1 if count != 0 else -1
 ```