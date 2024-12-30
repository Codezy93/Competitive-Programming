# Hurdle Race

Date: 2024-10-12 18:03:23.457274

## Solution

#### Python
```python
def hurdleRace(k, height):
    return max(height) - k if max(height) - k > 0 else 0
 ```