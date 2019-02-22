# Penguin Island

The Galapagos penguin, endemic to the Galapagos Islands, is an endangered species with less than 1000 breeding pairs remaining at last count. The Galapagos Islands sit on the equator, and the penguins are able to survive in there because of weather conditions that result in relatively cool temperatures for the equator. 

Recently, an ecologist has raised concerns about the impact of climate change on the Galapagos penguin population. While the penguins are spread out over multiple islands, the ecologist is most concerned about the penguins on Isabela island. The tip of Isabela island crosses the equator, making the penguins on the northern tip of Isabela island the only penguins found north of the equator. 

The penguins do not have a regular breeding season, and instead breed when food is abundant. Their main source of food, which consists mostly of fish, is brought in by cool ocean currents. Thus, the availability of their food is dependent on varying weather patterns - which can be affected by climate change. 

You must work with your ecologist colleague to model the population of penguins. They have already written a small program that models the amount of fish available to the penguins, and have provided you with the following information to help you model the penguin population:

Time to model: The populations will be modelled over 5 years, with a step size of 3 months. So there will be `5*3+1 = 16` steps, including theinitial step.

Fish: modelled as a percentage instead of number of individuals. 100 percent means there is enough fish for all penguins to be happy. 0 percent means that the penguins will not breed, but can still eat. The equation is provided.

Initial population of penguins: 600 (an educated guess by the ecologist)

Breeding rate: with X number of penguins, there will be approximately X/3 breeding pairs, which will produce one offspring over three months. So the breeding rate is `current_penguins/3 * current_fish/100`.

