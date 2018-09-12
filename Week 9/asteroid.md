# Euler's Method (4) - Asteroid!

An asteroid has been spotted travelling through our solar system. One astrophysicist has predicted that it will collide with Earth in exactly 215 days, using a new method of modelling trajectories. The researcher has asked you and others to verify their claim using a variety of methods. You have been tasked with modelling the asteroid's trajectory using Euler's method. 

For an asteroid to collide with Earth, it needs to have the same x, y, and z coordinates as the Earth in 215 days (x, y, and z represent the three dimensions. Because solar systems are three dimensional!). If any of the final predicted x, y, and z values are different to the Earth's, then that will mean the asteroid will not collide with Earth in 215 days. 

It was already been proven that the asteroid will have the same x and z coordinates as the asteroid in 215 days. So, you must check if the y value of the asteroid will be the same as Earth's in 215 days. 

The equation for the change in y at day t after the asteroid was discovered is:

`y'(t) = aksjdhalsjhd`

In order to be precise, you have decided to do 10 iterations of Euler's method for each of the 215 days. That's 2150 steps of Euler's method. The starting `y` position of the asteroid is 100 UNITS. The `y` position of Earth in 215 days is 32 UNITS. 

**Task:** Write a function called will_it_hit(), that returns the number `1` if the asteroid is going to hit Earth in 215 days, and 0 otherwise. The Earth will be considered 'hit' if the asteroid gets within 0.1 UNITS of Earth (so abs(earthy - asteroidy)<=0.1). This function will take no input. Do not print anything. 

Use your code from the previous exercises. The only thing you will need to change is fdash. We have written tests for each of your functions (fdash, onestep, eulers, will_it_hit), to help you understand where errors might be. Good luck!
