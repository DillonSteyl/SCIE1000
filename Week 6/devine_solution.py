# Write function here:
def IBW(s,h):
    if s == 1:
        ibw = 45.5 + (0.9 * (h - 152) )
    elif s == 0:
        ibw = 50 + (0.9 * (h - 152) )
    return(ibw)

# Do not modify:
sex = float(input("Enter 1 for female, 0 for male: "))
height = float(input("Enter height in cm: "))
print("Ideal weight:", IBW(sex,height), "kg.")
