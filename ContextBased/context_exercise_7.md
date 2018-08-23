The sensitivity and specificity of bowel cancer screening varies depending on the stage of cancer being screened. The recommended screening method for bowel cancer is immunochemical faecal occult blood test (FOBT), which has the following sensitivity ratings, if one sample from a patient is taken:

50% for stage I cancer

75% for stage II cancer

The specificity for either of these stages of bowel cancer using this method is 95%. 

The stage of bowel cancer can be roughly predicted based on the size of the growth found. Stage I and II can be distinguished from each other by observing how deep the tumour has grown within the lining of the bowel. Stage I is anything below 50% of the bowel lining depth, and Stage II is anything including and above this threshold. In the event a growth is found to be greater than 150% of the size of the bowel lining, stage III or IV cancer will be present.

A colleague of yours has predicted that the thickness of a patient’s bowel lining can be *roughly* approximated as a twentieth of their weight in kilograms. 

You want to write a program that will predict the chance of receiving a true positive and true negative result from an FOBT screen for bowel cancer, if a patient is within a testing population of 5,000 participants, and the size of their tumour is known. The program should therefore prompt the user to input the tumour size (in mm), along with the patient weight (in kg). Call these variables 'tumoursize' and 'weight' respectively. 

Your program should make use of a function called 'ratio', which determines what percentage of the bowel lining size is equivalent to the size of the patients tumour, and returns this value as a decimal. The result of this should then be used to determine which stage of cancer is present and print the required output.

The program should display the results as follows:

If the tumour is predicted to be a stage I or II growth, the output should be:

The chance of receiving a true positive and negative result from the FOBT screen are **ANSWER**% and **ANSWER**% respectively. 

If the tumour is in stage III or IV, print the following message:

The tumour is now in stage III or IV. 

User input should be prompted as follows:

Enter the tumour size (mm):

Enter the patient weight (kg):
