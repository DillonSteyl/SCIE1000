from pylab import *

#Ask the user to give the amplitudes and middles. Do not edit these lines!
amplitudeA = float(input("Enter the amplitude for Team A: "))
amplitudeB = float(input("Enter the amplitude for Team B: "))
shiftA = float(input("Enter the vertical shift for Team A: "))
shiftB = float(input("Enter the vertical shift for Team B: "))


i = 1
scoreA = 0
scoreB = 0
while i <=12:
    teamA = amplitudeA*sin(2*pi*(i-1)/3)+shiftA
    teamB = amplitudeB*sin(2*pi*(i+3)/12)+shiftB
    if teamA>teamB:
        print("Team A has the most fans for month", i)
        scoreA+=1
    elif teamA<teamB:
        print("Team B has the most fans for month", i)
        scoreB+=1
    else:
        print("Both teams are equally popular for month", i) 
    i=i+1

if scoreA>scoreB:
    print("Team A has the most fans for", scoreA, "months.")
elif scoreB>scoreA:
    print("Team B has the most fans for", scoreB, "months.")
else:
    print("Both teams are equally popular.")
