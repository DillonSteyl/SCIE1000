The University of Queensland St. Lucia campus is home to a large variety of wildlife, including student favourites such as the families of ducks seen at UQ Lakes. The university is also home to a range of reptiles, insects and plant species, many of which are Australian fauna and flora. 

You may remember the species area curve discussed earlier in the semester, which can be used to predict the number of species present in a given area of land, dependent on certain geographical factors.

The UQ St. Lucia campus covers 114 hectares of land. Note that 1 hectare is equivalent to 10,000 metres squared. Recall that the species area curve is modelled using the form

```python
S(a) = M*a**p
```
where a is the area of a given sample of land, and M and p are constants. 

You anticipate that the number of different species at UQ is lower during the months of Autumn and Winter than it is in Summer and Spring. You predict that during the cooler months, the variety is 40% lower. After consulting with a peer, you believe the species area curve for Spring/Summer can be modelled using

```python
S = 3*a**0.5
```

Write a program that plots the species area curve for both Autumn/Winter and Spring/Summer, where the x-axis represents the number of 1,000m square cells of UQ land being considered. Label each of the individual plots as 'Spring/Summer' and 'Autumn/Winter', and give your graph the title 'Species Area Curve'. Label the axes as 'Area (1000m square cells)' and 'Number of Species'. Make sure you include a legend.

Use the following variable names:

a = area array

SS = Spring/Summer model

AW = Autumn/Winter model
