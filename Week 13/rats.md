# Rats!

A scientist is running an experiment using rats, which involves the rats moving between cages connected by tunnels. The rats are treated well, and the cages are made comfortable. The scientist has made each cage and tunnel different, to see what choices the rats will make. The scientist has made predictions about how the rats will make choices, and would like to know if their predictions line up with their experimental results.

They have asked you to run a simulation based on their predictions about the rat behaviour, and have provided you with all the information you need.

There are four cages, named A, B, C, and D, containing 100 rats in total. The scientist says the simulation should be modelled over 51 steps, including the first step (step 0). At each step, the rats may move between cages with probabilities given as follows:

From - To: Probability

A - B: 20%

A - C: 10%

B - A: 10%

B - C: 5%

B - D: 20%

C - A: 40%

C - B: 10%


Probabilities not listed are 0%. The probabilities for rats remaining in their cages is as follows:


Cage: Probability

A: 70%

B: 65%

C: 50%

D: 100%


These probabilities do not change over time. The number of rats in each cage to begin are as follows:

Cage: Number of Rats

A: 40

B: 20

C: 30

D: 10


**Task:** Using the given probabilities, model the number of rats in each cage over 51 steps, including the first step. Store the number of rats in each cage using the variables A, B, C, and D. Print the final number of rats in each cage using the print statements provided. Finally, print the maximum number of rats in each cage during a single step, and the step number for when that maximum first occurs. Store the max index values using the variables provided. 

Since it is a simulation, the number of rats in each cage does not need to be rounded while the values are being calculated. However, they do need to be rounded when printing the values.  

**Hint 1:** For example, the number of rats in cage A at step i is given by the equation: 

`A[i] = A[i-1]*0.7 + B[i-1]*0.1 + C[i-1]*0.3`

That's 70% of rats in cage A staying, 10% of rats from cage B moving to cage A, and 30% of rats from cage C moving to cage A. 

**Hint 2:** Again, it may be useful for you to copy your highest(A) function just below the import statement.

