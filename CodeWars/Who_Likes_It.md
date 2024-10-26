# Who Likes It

Date: 2024-10-26 18:21:47.060623

## Solution

#### Python
```python
def likes(names):
    if len(names) == 0:
        return f"no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f'{" and ".join(names)} like this'
    elif len(names) == 3:
        print(names)
        return ", ".join(names[0:2]) + f' and {names[-1]} like this'
    else:
        return f'{", ".join(names[0:2])} and {len(names)-2} others like this'
 ```