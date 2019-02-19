from pylab import *

drinks = array([3, 3.5, 2, 2.5, 6, 3, 3, 5, 2.5])
fresh = array([2.5, 2.5, 2.5, 3, 3, 3, 2, 0.5, 0.5, 1.5, 5, 5])
cabinet = array([4, 4, 4.5, 6, 3.5, 5, 3.5, 3.5])

total = 0

product_type = 1

while product_type!=0:
    print("The total is", total)
    product_type = float(input("Enter the product type (1 = drinks, 2 = fresh, 3 = cabinet, 0 to exit): "))
    if product_type == 1:
        product_code = int(input("Enter the product code: "))
        total = total + drinks[product_code]
    elif product_type == 2:
        product_code = int(input("Enter the product code: "))
        total = total + fresh[product_code]
    elif product_type == 3:
        product_code = int(input("Enter the product code: "))
        if cabinet[product_code]>4:
            choice = float(input("Enter 1 for yes, 0 for no: "))
            if choice==1:
                total = total + 1.5
        total = total + cabinet[product_code]
     
    

print("The final total is", total)
