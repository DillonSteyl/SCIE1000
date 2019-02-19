# Week 12 - Context 2

Liquified Natural Gas (LNG) is natural gas (mostly composed of methane) that has been chilled to a liquid form. Australia is one of the world’s largest LNG exporters, and LNG is a highly sought-after resource due to its ease of transportation and high energy density. 

To cool natural gas to form LNG, other chemical substances such as propane and ethylene are required to be used as refrigerants. These substances are highly flammable, and the material used to contain these substances is flame-resistant in the event of gas ignition.

The balanced chemical equation for the combustion of ethylene is

C2H4(g)+3O2(g)->2CO2(g)+2H2(l)

where CO2 (Carbon Dioxide) is a product of the combustion that has negative environmental effects. 

Suppose you are an environmental scientist hired by an LNG production company and you are investigating the potential environmental consequences of a recent ethylene ignition incident at the company’s plant. Your task is to write a program that calculates the amount of CO2 produced by the combustion of a user indicated amount of ethylene gas. This will require the following steps:

1. Prompt the user to input the following values with variable names as indicated below:
*ethylene* = "Please enter the volume of ethylene burnt in litres: "
*temp* = "Please enter the ambient air temperature in degrees Celsius: "

2. Write a function called ideal_gas_n, which uses the ideal gas law to determine the number of moles of ethylene burnt in the combustion reaction. The ideal gas law rearranged to determine the number of moles of ethylene present is
```python
n = pV/RT
```
where n is the number of moles of ethylene burnt, p is atmospheric pressure (1.083 atm), V is the volume of ethylene burnt (Litres) indicated by the user input variable *ethylene*, R is the ideal gas constant (8.413J/K/mol), and T is the ambient air temperature converted to Kelvin. To convert Kelvin, add 273.15 to the *temp* input entered in Celsius. 

3. Find the number of moles of CO2 produced. To do so, note that there is a molar ratio of 1:2 in the balanced chemical equation, so there will be double the number of moles of CO2 as there are ethylene present in the combustion reaction.

4. Write a function called *ideal_gas_v*, which uses the ideal gas law to determine the volume of CO2 produced from the combustion reaction. The ideal gas law rearranged to determine the volume of CO2 produced in litres is 
```python
V = nRT/p
```
where n is the number of moles of CO2 produced, and variables R, T and p are the same as they were in the function *ideal_gas_n*. 

5.	Print the volume of CO2 produced as shown below:
“A total of **ANSWER** litres of carbon dioxide were produced in the combustion reaction from **INPUT** litres of ethylene.”

# Solution
