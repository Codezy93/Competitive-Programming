
# Inherited Code

Date: 20-08-2024

## Solution
#### Python
```python
class BadLengthException{
    int n;
    public:
    BadLengthException(int n){
        this->n = n;
    }
    int what()
    {
        return n;
    }
};
```
        