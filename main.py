#Step 1
#Debug the following program so that it properly takes a users order and outputs the price of the order.

#Step 2
#Edit the existing code and have it print out the items you are ordering as follows...
#Example
# "Coffee x 0"
# "Cake x 2"
# "Tea x 3"

#Step 3
#Have the items you are ordering also output their indavidual cost.
#Example
# "Coffee x 0 : 0.00"
# "Cake x 2 : 5.00"
# "Tea x 3 : 3.6"


listOfOrders = ["Cofee", "Cake", "Tea"]
Price = 0

for i in range(listOfOrders):
  message = "Would you like to buy a "+str(listOfOrders[i])+ ". Yes / No   "

  myOrder = input(str(message))

  if myOrder == "Yes" and i == 1:
    number = int(input("How many would you like? "))
    for a in range(number):
      price = price + 2.5*a

  if myOrder == "Yes" and i == 2:
    number = int(input("How many would you like? "))
    for a in range(number):
      price += 5.2*a

  if myOrder == "Yes" and i == 3:
    number = int(input("How many would you like? "))
    for a in range(number):
      price += 1.2*a

print("Your total price is", price, ".")