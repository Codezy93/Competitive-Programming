
# Best Internet Browser

Date: 25-09-2024

## Solution
#### Python
```python
for _ in range(0, int(input())):
    site = input()
    total = len(site)
    site = site.replace('www.', '')
    site = site.replace('.com', '')
    for i in 'aeiou':
        site = site.replace(i, "")
    print(f"{len(site)+4}/{total}")
```
        