# Introduction to Functions (1)

We have already covered functions that are **included** in Python, such as the `sqrt` and `exp` functions. It can be very useful to create your own custom functions to use in your programs. Once you have written a function, you can use it in multiple places without having to rewrite the same lines of code over and over again.

When working with functions, you must first create (*define*) the function - here you will give it a name, and include the code which that function will perform when it is used (*called*).

To demonstrate the utility of creating functions, let's suppose we need to convert *days* to *minutes*. For instance:

```python
days = float(input("Number of days: "))
minutes = days * 24 * 60
print(minutes)
```

If you had to do this multiple times throughout your code, it may be useful to write a function to do this. We could call it `toMinutes`, and the code might then look more like this:

```python
days = float(input("Number of days: "))
minutes = toMinutes(days)
print(minutes)
```

Of course, if we are using a function, we need to define how it works. Here is one example of how we might define this function:
```python
def toMinutes(days):
    mins = days * 24 * 60
    return(mins)
```

Read this example carefully! 

The first line is where we give our function a name. The `def` stands for *define*, and it is essential. The first line of a function definition always has the following format:
```python
def functionName(input):
    # your code here
``` 
The variable `input` inside the brackets will, in this case, contain the number of days to be converted to minutes. We say that this value is *passed* into the function. It doesn't matter what you call this variable - it is simply a placeholder name. Try to choose a name that makes sense; we chose `days` for this example.

As with loops and conditionals, we need every line in the function to be indented. This allows Python to determine which code is involved in the function definition. As before, use four spaces or one tab. The indented lines will perform the calculations required by the function.

The last line, `return(mins)`, 'returns' the value calculated by the function. This just tells Python what the function's output should be.

The final program would then look more like this:
```python
def toMinutes(days):
    mins = days * 24 * 60
    return(mins)
    
days = float(input("Number of days: "))
print(toMinutes(days))
```
Here are some really important notes on functions. Make **sure** you understand these! Ask your tutors if you have any questions!
* A function *must* be defined **before** it is called. It is good practice to define your functions at the *top* of your programs. 
* Variables defined **inside** a function **cannot** be accessed outside the function, even if the same name is used in both places.
* You can define multiple functions in the same file/program. Remember indenting!
* The lines inside a function are only used when the function is **called** later in the program.
* A Python function need not be strictly mathematical - it can do anything a program does. It doesn't even have to return a value. 

This is a lot to take in - so take your time to make sure you understand everything!

**Task:** To start us off, we'll just practice *using* functions. This program has a function which converts inches to centimetres. Modify the program so that it converts `height_inches` to centimetres using the function `toCentimetres`, and assigns it to the variable `height_cm`.
