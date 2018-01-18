number = eval(input('Please enter a number: '))
number2 = eval(input('Please enter a different number: '))

abb = int(number)
if (abb < 0):
    abb *= -1
    print(abb)
else:
    print(abb)
	
print(number2)

print('Sum:', number2+abb)