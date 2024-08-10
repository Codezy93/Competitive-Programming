
# Count the smiley faces

Date: 10-08-2024

## Solution
#### Python
```python
def count_smileys(arr):
    count = 0
    for i in arr:
        if len(i) == 2 and ( i[0] == ":" or i[0] == ";"):
            if i[1] == ")" or i[1] == "D":
                count += 1
            else:
                pass
        elif len(i) == 3 and ( i[0] == ":" or i[0] == ";"):
            if i[1] == "-" or i[1] == "~":
                if i[2] == ")" or i[2] == "D":
                    count += 1
                else:
                    pass
            else:
                pass
        else:
            pass
    return count
```
        