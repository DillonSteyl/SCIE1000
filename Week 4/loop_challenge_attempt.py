from pylab impor *

#Ask the user to give the amplitudes and middles. Do not edit these lines!
amplitudeA = float(input("Enter the amplitude for Team A: "))
amplitudeB = float(input("Enter the amplitude for Team B: "))
middleA = float(input("Enter the middle for Team A: "))
middleB = float(input("Enter the middle for Team B: "))



#Write your while loop here, printing for each month.


#Write some if statements here to print which team is most popular.

if scoreA>scoreB:
    print("Team A has the most fans for", scoreA, "months.")
elif scoreB>scoreA:
    print("Team B has the most fans for", scoreB, "months.")
else:
    print("Both teams are equally popular.")
