
# Complementary DNA

Date: 19-09-2024

## Solution
#### Python
```python
def DNA_strand(dna):
    dna = list(dna)
    for i, j in enumerate(dna):
        if j == "A":
            dna[i] = "T"
        elif j == "T":
            dna[i] = "A"
        elif j == "G":
            dna[i] = "C"
        elif j == "C":
            dna[i] = "G"
        else:
            pass
    return "".join(dna)
```
        