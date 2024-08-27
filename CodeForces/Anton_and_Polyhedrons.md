
# Anton and Polyhedrons

Date: 27-08-2024

## Solution
#### Python
```python
sum = 0
shapes = {
    "Tetrahedron" : 4,
    "Cube" : 6,
    "Octahedron" : 8,
    "Dodecahedron" : 12,
    "Icosahedron" : 20
}
for _ in range(0, int(input())):
    sum += shapes[input()]
print(sum)
```
        