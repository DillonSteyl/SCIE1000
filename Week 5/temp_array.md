Now, try something a bit harder. 




You want to write a program that calculates all the marks for your courses simultaneously. There are three types of assessment: exams, assignments, and attendance. Fortunately, all of the courses were standardised so that each assessment type is worth the same amount. Exams are worth 50% of the total grade, assignments are worth 35%, and attendance is worth 15%. 

So for one of your courses, if you recieved 90% for your exam, 80% for your assignments, and 95% for attendance, your total grade will be 87.25%. Check this on paper to make sure you are doing the correct calculation.

The program currently has three arrays: `exams`, `assignments`, and `attendance`. The first element of each array corresponds to your first course. The second elements all correspond to your second course, and so on. The `final` array is yet to be written, and should be the final percentage grade for each course. 

**Task:** Modify this program so that it calculates the total grade for each class your friend is enrolled in. Store the final grades in the variable 'final'.

Use the following print statement to end your program: print("The final marks out of 100 are:", final").

**Hint:** Array operations happen to each element individually. If there are multiple arrays in one equation, then the operations are applied to all the first elements alone, then all the second elements alone, and so on. 

## Solution
```python
from pylab import *

exams = array([82, 48, 55, 67])
assignments = array([90, 83, 64, 88])
attendance = array([100, 80, 50, 70])

final = exams*0.5+assignments*0.35+attendance*0.15

print("The final marks out of 100 are:", final)
```

