# Unique in Order

Date: 2024-10-14 10:16:05.314276

## Solution

#### Python
```python
def unique_in_order(sequence):
    out = []
    for i in sequence:
        if len(out) == 0:
            out.append(i)
        else:
            if i != out[-1]:
                out.append(i)
    return out
 ```