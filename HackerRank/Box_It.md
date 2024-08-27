
# Box It

Date: 27-08-2024

## Solution
#### Python
```python
class Box {
    private:
        int length, breadth, height;
    public:
        Box() : length(0), breadth(0), height(0) {}
        Box(int l, int b, int h) : length(l), breadth(b), height(h) {}
        Box(const Box& box) : length(box.length), breadth(box.breadth), height(box.height) {}
        int getLength() { return length; }
        int getBreadth() { return breadth; }
        int getHeight() { return height; }
        long long CalculateVolume() { return static_cast<long long>(length) * breadth * height; }
        bool operator<(const Box& b) {
            if (length < b.length)
                return true;
            else if (length == b.length && breadth < b.breadth)
                return true;
            else if (length == b.length && breadth == b.breadth && height < b.height)
                return true;
            else
                return false;
        }
        friend ostream& operator<<(ostream& out, const Box& B) {
            out << B.length << " " << B.breadth << " " << B.height;
            return out;
        }
};
```
        