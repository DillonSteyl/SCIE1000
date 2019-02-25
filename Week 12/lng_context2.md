# LNG Part 2

Natural gas that enters the plant upstream is condensed, and then stored as LNG in tanks until a ship is ready to collect cargo. When natural gas is condensed to LNG, it will occupy a volume approximately 400 times smaller than it would have in its gaseous form. 

When the LNG is in the tanks, due to imperfections in the insulation, some LNG will become ‘boil-off gas’, and therefore needs to be recycled back through the plant to be condensed to liquid again. This therefore slightly reduces the amount of LNG in the tanks. 

Ships that carry LNG will also produce some boil-off gas during loading which also gets recycled back through the plant. Loading takes between 12 and 14 hours for a load of roughly 150,000m^3. 

Suppose you are working at an LNG company and you are trying to produce a weekly loading schedule for the plant. Your task is to write a program that models the volume of LNG present in the tanks across the weekly schedule. The program should plot the volume of LNG in the tanks every 2 hours from Monday 8am to Friday 6pm. To do this, it will require the following elements:
1. The program should ask for the number of cargo ships to be expected for the week, which can be a maximum of 3. 
2. The program should ask for the gas supply rate upstream, and convert this into an appropriate volume going into the tanks.
3. It will be assumed that the boil-off gas rate is a 2% loss in the tank volume every 4 hours, and this increases to 3.5% when loading.

To undertake this task, note the following the facility has two LNG tanks with a capacity of 160,000m^3 each. For safety purposes, a combined volume above 300,000m^3 is undesirable. Therefore if the tanks are filled this high, no more LNG should be passed into them.
