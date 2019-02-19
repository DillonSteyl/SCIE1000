# Modulo Operator (3)

Your eccentric friend has been placed in charge of a Time Machine you built together. They have decided that they don't like to count in years, only months. This makes it difficult to pack your clothes - what kind of weather should you expect if you don't know what season it is?

**Task:** Write a function called `travel(current_month, num_months)` that outputs the season that you will arrive in. The `current_month` variable is the month you will travel from (from 0 to 11), and `num_months` is the number of months you will travel backward or forward in time. The output of the function should be 1 for autumn (months 2 to 4), 2 for winter (months 5 to 7), 3 for spring (months 8 to 10), and 0 for summer (months 11, 0, and 1). `num_months` will be positive if you are going forward in time, and negative if you are going backward. 

It is important to note that we will start counting the months at 0, so January will be 0 and December will be 11. 

For example, if the starting month is January (0), and you will be going forward 50 months (50), then the month will be March (2), because 50 months is 4 years + 2 months in the future. This would correspond with the operation `(0+50)%12`, which is equal to 2. March is in Autumn, so `travel(0, 50) = 1`. 

For an example going back in time, if the starting month is June (5), and you will be going back 6 months (-6), then the output of the function should be 1, because 6 months prior to June (5) is December (11). This would correspond with the operation `(5-6)%12`, which is equal to 11. December is in Summer, so `travel(5, -6) = 0`.

To reiterate, the formula for the new month is: `(current month + months travelling in time) % 12`

Unless you are very crafty, you will need conditionals in this function to handle converting from the month to the season. 

**Hint:** There is no need to write different code for going back in time vs going forward in time. Notice how in the examples the same formula is used either way. The modulo operator will work exactly how we want it to in either case, because it handles negative values just fine.
