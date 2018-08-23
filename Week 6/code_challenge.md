# Challenge - Crack the Code

For computers to communicate with each other they must send messages, and often times these messages must remain a secret. Messages are encrypted by the sender, sent to the recipient, and then unlocked by the recipient using a 'key' that only the sender and recipient know. 

The mathematical field of cryptography is concerned with the creation and cracking of encryptions - coming up with ways to encrypt/decrypt messages, and how to figure out keys for messages you don't know. Cryptography can have a significant impact on our lives, with various governments even restricting the export of cryptographic technology in the past by classifying it as a weapon. That's right! Maths as a weapon!

There are many different ways to encrypt and decrypt messages, and each method uses a particular type of key (think of keys as the thing that locks and unlocks a message, just like you would with your front door). There are generally two types of keys. Private keys and Public keys. For private keys, a 'key' (usually a string of letters or numbers) is used to encrypt the message, and then that same key is used to decrypt the message. 

Public keys are a bit different. The idea is that one key is used to encrypt the message, but a different key is used to decrypt the message. This way, you can give all your friends (and even enemies) an encryption key. People can encrypt messages and send them to you, but only you can decrypt them. This can be very useful!

In fact, a very popular public key cryptosystem is known as RSA, and is still in use today. RSA works by coming up with two large prime numbers, which is the decryption key. These two prime numbers are multiplied together to make the encryption key, which is sent to anyone who wants it. People can use your encruption key to send you encrypted messages, but you can only decrypt the message if you know the two prime numbers. 

This cryptosystem is hard to crack, because currently we do not have an efficient way of finding the two prime numbers that were multiplied together to create the decryption key. When the prime numbers are really big, it just takes too long!

For this exercise you will write a function that takes a number as input, and finds the two primes that are multiplied together to make that number. Now, we aren't going to be making any great mathematical discoveries with this exercise. You will use a simple method known as 'brute force'. In computer science, a brute force algorithm is one that just tries every single possibility until it finds one that works, without using any special tricks.

**Task:** Write a function that takes a single number as input, and returns the two primes that can be multiplied together to get that number. Name the function `primes`. You can assume that the primes will all be less than 30. We have given you an array of all primes under 30. You are welcome to write other functions to help complete the task, but it is not necessary. If you cannot find the two primes, return -1, -1.

The hint below will tell you how to solve this problem, but see if you can figure some of it out first. Use pen and paper and see how you would 'brute force' the problem. Try finding the two prime numbers for the number 21 as if you were a computer. The output should be 3 and 7. Try again for 65, the answer should be 5 and 13.

**Hint:** To 'brute force' this problem, you need to try every combination of prime numbers from the list. So you need to compare 2 with 2, with 3, with 5, with 7 and so on. Then you need to compare 3 with 2, with 3, with 5, and so on. For this you will need a while loop inside a while loop(!!!). 

Here is an example nested while loop that prints all the different combinations of even numbers 2 to 6:

```
from pylab import *

#makes an array with numbers [2, 4, 6]
numbers = array([2, 4, 6])

#initialise the outer while loop
i = 0

# recall, the len(A) function returns the length of the array A. In this case it is 3.
while i<len(numbers):
    # every time you run the outer loop, you want to run the inner loop all over again
    # so j is set to 0 here
    # remember to use a different variable to i (we chose j) or else your program will be silly
    j = 0
    while j<len(numbers):
        # use i and j to access the array and print the numbers
        print("The first number is", numbers[i], "and the second number is", numbers[j])
        j = j + 1
    i = i + 1

```

The output is: 

```
2 2
2 4
2 6
4 2
4 4
4 6
6 2
6 4
6 6
```

You will also need to check each combination to see if it is correct. You can do this by using a conditional inside the inner while loop to see if the two numbers multiplied together make the input number. This would go in place of the print statement in the example nested while loop. 

Once you have found two numbers that satisfy that condition, you do not need to search anymore. Once you have found them, you just need to return the two numbers. If you have cycled throuhg every combination and have not found them, remember to return -1, -1. This will happen at the end of your function, outside of the while loops. 


```
from pylab import *

def primes(n):
    P = array([2,3,5,7,11,13,17,19,23,29])
    i = 0
    while i < len(P):
        j = 0
        while j< len(P):
            if P[i]*P[j]==n:
                return(P[i],P[j])
            j = j + 1
        i = i + 1
    return(-1,-1)


```
