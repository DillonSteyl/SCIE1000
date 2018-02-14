In microbiology, the growth of bacteria in batch culture can be modelled using the bacteria growth curve. For those unfamiliar with this procedure, a small population of bacteria is placed inside an a Petri dish containing agar, and the growth of the population is then monitored. 

The bacteria growth curve consists of four phases, as follows:

Phase A - The lag phase: For some period of time, no observed growth happens. This is the result of the bacteria adapting to a new environment. 

Phase B - The exponential phase: Once adapted, the bacteria population will increase through cell doubling. Each single bacteria cell divides into two identical cells. The population increase is therefore exponential, and is dependent on the number of bacteria cells present in the population at a given time.

Phase C - The stationary phase: Eventually, further population growth is prohibited due to limiting resources available in the cell environment, or due to environment changes such as temperature. The death rate and growth rate of the bacteria is roughly equivalent, resulting in no observable growth.

Phase D - The death phase: Once the environment is no longer suitable for population growth, the bacteria will die, and the population will decrease.

To create the bacterial growth curve from these four phases, the bacteria present in the sample is represented in the units of CFU/mL, which is the number of ‘Colony Forming Units’ per millilitre. A colony forming unit is a bacteria cell that is able to perform cell division and cause population growth.

The log of the number of CFU/mL is then plotted against time. This will result in phase B showing a linear curve, rather than an exponential one. The slope of this line is the growth rate of the bacteria population.

We want you to write a program that will determine and plot the bacterial growth curve for a sample of *Pseudomonas aeruginosa*, a common infectious Pseudomonas species, that has been tested through a batch culture experiment.  Observations from the experiment are as follows:

The initial number of CFU present in the 15 millilitre sample of agar was 225,000.
The lag phase lasted for 6 hours, and following this the bacteria were observed to double every 15 minutes.
At the 14 hour mark, the population remained roughly stable, and continued to do so for a following 8 hours.
The population then began to decrease, and was observed to decrease by 25% every 15 minutes.

Some helpful reminders and guidelines to consider when writing your program are:

1. Use hours as the units for the x-axis of your plot. Create the growth curve for a 24 hour time span from the start of the experiment, using the time array provided. Note the spacing used between intervals, and consider carefully how this will affect the way you refer to specific array elements and set up any conditional statements. 

2. Be sure to plot the log of CFU/mL on the y-axis. In python, if you want to find the log to base 10 of a variable x, use log10(x).

3. Think carefully about the order in which you are calculating values in this program. Conditionals will need to be written in a particular order for the program to give the correct output. Remember that your program runs from top to bottom, so steps at the bottom of your program have the potential to override previous steps.

4. Consider using an array of zeros to store your information that you will use to plot the growth curve.

5. Give your plot the title 'Bacteria Growth Curve' and label the axes as 'Time (hours)' and 'Population (log CFU/mL)'. 
