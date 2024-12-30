
# C++ Class Templates

Date: 17-08-2024

## Solution
#### Python
```python
template <class T>
class AddElements {
private:
    T element;
public:
    AddElements(const T& element) : element(element) {}
    T add(const T& other) {
        return element + other;
    }
    T concatenate(const T& other) {
        return element + other;
    }
};
```
        