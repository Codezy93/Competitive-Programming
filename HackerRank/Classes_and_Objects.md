
# Classes and Objects

Date: 16-08-2024

## Solution
#### Python
```python
class Student{
  public:
  int marks;
  void input(){
      int a,b,c,d,e;
      cin >> a >> b >> c >> d >> e;
      marks = a+b+c+d+e;
  }
  int calculateTotalScore(){
      return marks;
  }
};
```
        