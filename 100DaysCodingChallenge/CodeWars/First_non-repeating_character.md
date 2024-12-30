
# First non-repeating character

Date: 15-08-2024

## Solution
#### Python
```python
def first_non_repeating_letter(s):
    t = s.lower()
    for i in s:
        u = i.lower()
        if t.count(u) == 1:
            return i
    else:
        return ""
```
        