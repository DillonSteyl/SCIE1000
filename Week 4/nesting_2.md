# Nesting (2)

**Task:** This program counts upwards from -3 to 3. Modify it so that the following output is produced:
```
Negative: -3
Negative: -2
Negative: -1
Zero: 0
Positive: 1
Positive: 2
Poistive: 3
```
You will need to use a nested conditional (if/elif/else) to do this.

## Program
```python
i = -3
while i <= 3:
    print(i)
    i = i + 1
```

## Solution
```python
i = -3
while i <= 3:
    if i < 0:
        print("Negative:", i)
    elif i == 0:
        print("Zero:", i)
    else:
        print("Positive:", i)
    i = i + 1
```
