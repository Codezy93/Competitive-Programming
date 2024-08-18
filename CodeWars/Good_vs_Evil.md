
# Good vs Evil

Date: 18-08-2024

## Solution
#### Python
```python
def good_vs_evil(good, evil):
    good = [int(x) for x in good.split(" ")]
    evil = [int(x) for x in evil.split(" ")]
    good_worth = [1,2,3,3,4,10]
    evil_worth = [1,2,2,2,3,5,10]
    good = sum([good_worth[x]*y for x,y in enumerate(good)])
    evil = sum([evil_worth[x]*y for x,y in enumerate(evil)])
    if good > evil:
        return("Battle Result: Good triumphs over Evil")
    elif good < evil:
        return ("Battle Result: Evil eradicates all trace of Good")
    else:
        return ("Battle Result: No victor on this battle field")
```
        