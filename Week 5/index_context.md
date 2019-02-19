## Indexes (3) - Alien Tourism

You are in charge of alien vacations in our solar system. Each planet has a different cost to visit. After doing market research, you've found that if you show your alien customers the prices for the planets adjacent to the one they request, they will often change their mind and visit the most expensive planet listed instead. For example, if they ask to visit Jupiter, and you show them the prices for Mars, Jupiter, and Saturn, they will choose Mars - a more expensive vacation. 

Also, additional market research has shown you how to increase the chance that your alien customers will upgrade to a luxury package (which includes a stop at Pluto). If the planet they are initially interested in costs more than or equal to 10 billion dollars to visit, print the message "Excellent choice!" after listing prices. Otherwise, print the message "A popular destination!".

You also want to simulate supply and demand, so you update the cost of their initial planet choice by adding 2 billion to the price after you have printed your messages. 

**Task:** Edit the program so that it prints the cost to visit their initial planet choice and adjacent planets, then prints a message depending on their initial planet choice. Finally, update the cost of their initial planet choice by increasing it by 2 billion dollars. 

The costs are stored in the array `costs`, in order of how close they are to the sun. The index of the planets they choose are stored in the variable `planet`.

Note that for Mercury, there is no planet closer to the sun, so you should only print the cost of Mercury and Venus. For Neptune, there is no planet further away from the sun (that we know of and is classified as a planet), so you should only print the cost of Uranus and Neptune. 

You can expect all indexes to be valid (as in, between 0 and 7, inclusive).

**Inportant:** When printing, print in the order of closest to sun, to greatest distance away from the sun. Just print the prices with no words, then the message. For example, if they choose Venus then the output should be "18 13 5", then "Excellent choice!". If they initially ask for Neptune, you should print "8 7".

**Hint:** There are three possibilities: the planet is the closest to the sun, the planet is one of the ones in the middle, and the planet is the greatest distance from the sun. That's three different options, so you will need conditionals!

