# Challenge: Crack the Code

**Note:** For this question, you will be using a nested while loop - which is a while loop inside another while loop. This may be new for you, so a relevant example has been provided at the end of the question. However, we recommend that you try this exercise on your own first (perhaps in Jupyter or Spyder), as it can be very satisfying to figure something out yourself!

The context for this challenge question is cryptography, a field of mathematics concerned with the encryption and decryption of messages, and the cracking of those encryptions. Specifically, you will write an algorithm that can help crack an RSA encryption, which is based on prime numbers. You will be given all the information you need to complete this exercise, but if you are interested in learning the purpose of your program, we have provided extra context information below. This extra context is optional, and you don't need to fully understand it to complete the question.

**Context:**

For computers to communicate with each other they must send messages, and often times these messages must remain a secret. Messages are encrypted by the sender, sent to the recipient, and then unlocked by the recipient using a 'key' that only the sender and recipient know. 

The mathematical field of cryptography is concerned with the creation and cracking of encryptions - coming up with ways to encrypt/decrypt messages, and how to figure out keys for messages you don't know. Cryptography can have a significant impact on our lives, with various governments even restricting the export of cryptographic technology after World War II by classifying it as a weapon. For example, the US listed cryptography as "Auxillary Military Equipment" as late as 1992. These days, you likely use cryptographic technology many times a day without even thinking about it - every time you load a page on the internet or send a text message, that information gets encrypted and decrypted. 

There are many different ways to encrypt and decrypt messages, and each method uses a particular type of key (think of keys as the thing that locks and unlocks a message, just like you would a treasure chest). There are generally two types of keys: private keys and public keys. 

For private keys, a key (usually a string of letters and/or numbers) is used to encrypt the message, and then that same key is used to decrypt the message. Using a treasure chest metaphor - your friend will put a message in the treasure chest, lock it with a key, and then send that treasure chest to you. Your friend will make sure you have the right key, by sending an exact copy of they to you in the mail (separately to the chest, of course). When you receive the treasure chest, you can open it with the key thye gave you and read the message. This way, only you and your friend can unlock the treasure chest, and you can send your messages back and forth. Anyone who intercepts the treasure chest cannot unlock it because they don't have the key, and thus your messages will be safe. Although, the intercepter may be able to 'pick the lock' if the lock is too simple, and read your messages, so you must try to have a very advanced lock! Picking the lock in this metaphor means cracking an encryption to read a message that wasn't meant for you. 

Public keys are a bit different. The idea is that one key is used to encrypt the message, but a different key is used to decrypt the message. To use the treasure chest metaphor again - you will send an unlocked treasure chest to a person that wants to send you a message. They will put the message in the treasure chest and close it. The treasure chest automatically locks, and they send it back to you. You can then open the treasure chest with your key, and read the message. Just like with private keys, someone intercepting the chest will not be able to read the message unless they can pick the lock. However, it has the advantage that you don't need to send your key through the mail, nor give anyone a copy of it. 

This way, you can give all your friends (and even enemies) an encryption key. People can encrypt messages and send them to you, but only you can decrypt them. This can be very useful!

In fact, a very popular public key cryptosystem is known as RSA, and is still in use today. RSA works by coming up with two large prime numbers, which is the decryption key. These two prime numbers are multiplied together to make the encryption key, which is sent to anyone who wants it. People can use your encryption key to send you encrypted messages, but you can only decrypt the message if you know the two prime numbers. 

This cryptosystem is not easy to crack quickly, because currently we do not have an efficient way of finding the two prime numbers that were multiplied together to create the decryption key. When the prime numbers are really big, it just takes too long! Numbers with a couple hundred digits can take a state of the art algorithm months, or even years, to find the prime numbers for. 

This is called a "prime factorisation" problem, and the task for this exercise is to write an algorithm that finds the prime factorisation for a given number. Now, you wont be expected to make any great mathematical discoveries today. We will describe to you the algorithm you should use, and it is a very simple and common one in computer science. It also runs quite slowly, so we will only give you small numbers.

**Task:**

For this exercise you will write a function named `primes` that takes a single number as input, and returns the two primes that are multiplied together to make that number. For example, given the number 35, your function must return the numbers 7 and 5. The order the nubmers are returned in is not important. 

You can assume that the primes will all be less than 30 (so the biggest number we could give you is `841 = 29*29`). We have given you an array of all primes under 30 to help you out. You are welcome to write other functions to help complete the task, but it is not necessary. If you cannot find the two primes (not all numbers are made up of exactly two primes multiplied together), return -1, -1.


**Algorithm:**
You will use a simple algorithm known as the 'brute force algorithm'. In computer science, a brute force algorithm is one that methodically tries every single possibility until it finds one that works, without using any special tricks. The brute force algorithm will go through each possible pair of primes (from 2 and 2 all the way to 29 and 29), and see if it's the correct answer. If it finds the correct answer, the algorithm can finish early and return the pair of primes.

The hint below will tell you how to solve this problem, but see if you can figure some of it out first. Use pen and paper and see how you would 'brute force' the problem - focusing on methodically trying different pairs of primes. Try finding the two prime numbers for the number 10 as if you were a computer. The output should be 2 and 5. Try again for 21, the answer should be 3 and 7.


**Hint:** To 'brute force' this problem, you need to try every combination of prime numbers from the list. So you need to compare 2 and 2, 2 and 3, 2 and 5, and so on, all the way to 2 and 29. Then you need to compare 3 and 2, 3 and 3, 3 and 5, and so on, all the way to 3 and 29. This gets repeated for all the rest of the prime numbers, 5 to 29. For this you will need a while loop inside a while loop. 

Here is an example nested while loop that prints all the different combinations of even numbers 2 to 6:

```
from pylab import *

#makes an array with numbers [2, 4, 6]
numbers = array([2, 4, 6])

#initialise the outer while loop
i = 0

# recall, the len(A) function returns the length of the array A. In this case len(numbers) is 3.
while i<len(numbers):
    # every time you run the outer loop, you want to run the inner loop all over again
    # the inner loop needs its own counter variable, different to i
    # here we have chosen j and initialised it to 0
    j = 0
    while j<len(numbers):
        # use i and j to access the array and print the numbers
        print("The first number is", numbers[i], "and the second number is", numbers[j])
        # do not forget to increment j
        j = j + 1
    # do not forget to increment i
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

This example of nested while loops just prints the numbers in the array, but for the prime function you will need to check each combination to see if it is correct. You can do this by using a conditional inside the inner while loop to see if the two numbers multiplied together make the input number. This would go in place of the print statement in the example nested while loop. 

Once you have found two numbers that satisfy that condition, you do not need to search anymore. Once you have found them, you just need to return the two numbers. If you have cycled through every combination and have not found them, remember to return -1, -1. This will happen at the end of your function, outside of the while loops. 

If you are struggling, open up Jupyter and test your code in there!

# Solution

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
