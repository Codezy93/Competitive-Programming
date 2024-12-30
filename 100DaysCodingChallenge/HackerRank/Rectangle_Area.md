
# Rectangle Area

Date: 15-08-2024

## Solution
#### Python
```python
class Rectangle{
    int l, b;
    public :int data(int lin, int bin){
        l = lin;
        b = bin;
        return 0;
    }
    public :int display(){
        cout << l << " " << b << endl;
        return 0;
    }
};
class RectangleArea : public Rectangle{
    int l, b;
    public :int read_input(){
        cin >> l >> b;
        data(l, b);
        return 0;
    }
    int display(){
        cout << l*b << endl;
        return 0;
    }
};
```
        