# Multiple Inputs (4) - The Devine Formula

The *Devine* formula is a commonly used formula to calculate 'ideal' body weight based on the height of a person. It was first published by Dr. BJ Devine, and was originally intended to be used to calculate the dosage of certain medications. It has become the most popular formula on the internet for calculating ideal body weight. It appears on a vast number of websites, including websites which suggest using it as a goal for weight loss.

The formula (roughly converted to work with centimetres instead of feet and inches) is as follows:
* **Men:** Ideal Body Weight (kg) = 50 + (0.9 * (height - 152) )
* **Women:** Ideal Body Weight (kg) = 45.5 + (0.9 * (height - 152) )

**Task:** Write a function `IBW` which calculates the Ideal Body Weight of a person. It should take two inputs. The first input should be `sex`, with 1 representing female and 0 representing male. The second input should be `height` in centimetres.

If you copy the finished program and test it elsewhere, you might notice that there is a big problem with this formula. Fun fact: it isn't based on *any* population data. Apparently, it has been based on the *estimations* of Dr. Devine's mentor. A known issue with the Devine formula is that it suggests an IBW that is far too low for women, especially shorter women. 
