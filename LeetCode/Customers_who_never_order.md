# Customers who never order

Date: 2024-11-09 19:13:28.406394

## Solution

#### Python
```python
select
    Name as Customers
from
    Customers
where
    Id
not in(
    select CustomerId from Orders
);
 ```