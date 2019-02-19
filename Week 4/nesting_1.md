# Nesting

It is important to note that we can "nest" loops and conditionals inside each other to create more complex programs. Nesting simply requires multiple indents to keep track of structure. For example:

```python
i = 1
while i <= 5:
    print("Count:", i)
    if i == 3:
        print("Hey! 3 is my favourite number!")
    i = i + 1
print("Finished!")
```

The output of the code block above is given below.
```
Count: 1
Count: 2
Count: 3
Hey! 3 is my favourite number!
Count: 4
Count: 5
Finished!
```

This can be very useful when writing more complex programs.

**Task:** This program counts down from 20 to 0. Modify the program so that it prints the line "Only one digit now..." when the count-down reaches 10. Your output should be:

```
20
19
18
17
16
15
14
13
12
11
10
Only one digit now...
9
8
7
6
5
4
3
2
1
0
```
