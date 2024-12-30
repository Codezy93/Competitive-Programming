
# Grading Students

Date: 29-09-2024

## Solution
#### Python
```python
def gradingStudents(grades):
    for i, grade in enumerate(grades):
        if grade < 37:
            grades[i] = grade
        elif grade%5 >= 3:
            grades[i] = grade+(5-grade%5)
        else:
            grades[i] = grade
    return grades
```
        