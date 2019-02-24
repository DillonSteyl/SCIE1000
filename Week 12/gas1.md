# Natural Gas (1)

Liquified Natural Gas (LNG) is natural gas (mostly composed of methane) that has been chilled to a liquid form. Australia is one of the world’s largest LNG exporters, and LNG is a highly sought-after resource due to its ease of transportation and high energy density. 

To cool natural gas to form LNG, other chemical substances such as propane and ethylene are required to be used as refrigerants. These substances are highly flammable, and the material used to contain these substances is flame-resistant in the event of gas ignition. Combustion of these flammable substances needs to be well understood when one wants to transport, store, or use them.

The balanced chemical equation for the combustion of ethylene (C2H4) is

C2H4(g)+3O2(g)->2CO2(g)+2H2(l),

where CO2 (Carbon Dioxide) is a product of the combustion that has negative environmental effects. This chemical equation can be interpreted as 'one ethylene molecule reacts with three oxygen molecules to produce two carbon dioxide molecules and two hydrogen molecules'. This is an exothermic reaction, meaning it also releases energy in the form of light or heat. 

Suppose you are an environmental scientist hired by an LNG production company and you are investigating the potential environmental consequences of a recent ethylene ignition incident at the company's plant. You wish to write a program that will assist you and other users in understanding the consequences of ethylene ignitions. 

**Task:** To begin, write a function called `ideal_gas_n(V)` that takes as input the volume of a gas in litres, and returns the number of moles. To do this, you will need to make use of the ideal gas law, which is as follows:

`PV = nRT`,

where `P` is the pressure of the gas (pascals), `V` is volume of the gas (cubic metres), `n` is the number of moles (mol), `R` is the ideal gas constant, and `T` is the absolute temperature of the gas (Kelvin). You will need to rearrange this equation to suit your needs, and you can assume that `P`, `R`, and `T` will take on the following values:

```
P = 101325 Pa
R = 8.413 m^3 Pa K^-1 mol^-1
T = 298.15 K
```
