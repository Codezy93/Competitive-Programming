
# Reformat Date

Date: 21-08-2024

## Solution
#### Python
```python
class Solution:
    def reformatDate(self, date: str) -> str:
        days = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']
        months = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}
        DD, MM, YYYY = date.split(" ")
        DD = days.index(DD)+1
        MM = int(months[MM])
        return f"{YYYY}-{MM:02d}-{DD:02d}"
```
        