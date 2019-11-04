# Penguin Island

The Galápagos penguin, endemic to the Galápagos Islands, is an endangered species with less than 1000 breeding pairs remaining at last count. The Galápagos Islands sit on the equator, and the penguins are able to survive there because of weather conditions that result in relatively cool temperatures for the equator. 

Recently, an ecologist has raised concerns about the impact of climate change on the Galápagos penguin population. While the penguins are spread out over multiple islands, the ecologist is most concerned about the penguins on Isabela island. The tip of Isabela island crosses the equator, making the penguins on the northern tip of Isabela island the only penguins found north of the equator. 

The penguins breed between May and January, but only when food is abundant. Their main source of food, which consists mostly of fish, is brought in by cool ocean currents. Thus, the availability of their food is dependent on varying weather patterns - which can be affected by climate change. 

You must work with your ecologist colleague to model the population of penguins. They have already written a small program that models the amount of fish available to the penguins, and have provided you with the following information to help you model the penguin population:

Time to model: The populations will be modelled with a step every 3 months, referred to as a 'quarter', for a total of 16 quarters (including quarter 0, the initial quarter).

Fish: modelled as a percentage instead of number of individuals. 100 percent means there is enough fish for all penguins to be happy. 0 percent means that the penguins will not breed, but can still eat. The equation is provided.

Initial population of penguins: 600 (an educated guess by the ecologist)

Breeding rate: with X number of penguins, there will be approximately X/6 breeding pairs ready to breed, which will produce one offspring each quarter - a simplification of their real breeding patterns. So the breeding rate is `current_penguins/6 * current_fish/100` each quarter.

Death/Migration rate: The ecologists predicts that 20% of the penguins will die each year, and that the net migration rate will be -20%. This comes to a change in population of 40% less penguins per year, or 10% less penguins per quarter. So, 90% of the penguin population is sustained each quarter.

The result of this information is the following equation:

`P[i] = P[i-1]*0.90 + (P[i-1]/6) * (F[i-1]/100)`,

where `P[i]` is the number of penguins at step i, and `F[i]` is the number of fish at step i. 

**Task:** Edit the program so that it also calculates the number of penguins each quarter, and stores it in the array `P`. Find the quarter for when the fish population is at its highest percentage, and print the penguin population for this quarter, with the print statement provided. 

**Hint:** It will be helpful to use the `highest(A)` function you wrote in the previous exercise to find the index (quarter) for the highest number of fish. Make sure to copy it into your code underneath the import statement.

