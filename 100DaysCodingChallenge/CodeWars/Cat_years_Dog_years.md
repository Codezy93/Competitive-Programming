# Cat years Dog years

Date: 2024-11-05 00:00:00

## Solution

#### Python
```python
def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        return [1,15,15]
    elif human_years == 2:
        return [2,24,24]
    else:
        return [human_years,24+((human_years-2)*4),24+((human_years-2)*5)]
 ```