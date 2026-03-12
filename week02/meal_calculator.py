# Creativity: I added a 15% tip calculation and a nice closing message.
#1. Ask for Prices (using float for decimals)
child_price = float ( input ("What is the price of a child's meal?"))
adult_price = float (input ("What is the price of an adult's meal?"))

#2. Ask for Quantities (using int for whole numbers)
children = int(input("How many children are there?"))
adults = int(input("How many adults are there?"))

#3. Calculate and display Subtotal
subtotal = (child_price * children) + (adult_price * adults)
print (f"Subtotal: ${subtotal:.2f}")

#4. Sales tax
tax_rate= float (input("What is the sales tax rate?"))
sales_tax = subtotal * (tax_rate / 100)
print(f"Sales Tax: ${sales_tax:.2f}")

#5 Total
total = subtotal + sales_tax
print (f"Total: ${total:.2f}")

#6 Payment
payment = float (input("What is the payment amount? "))

#7 Change
change = payment - total
print (f"Change: ${change:.2f}")

#8 Creativity (tip)
tip = subtotal * 0.15
print (f"Suggested Tip (15%): ${tip:.2f}")

#9 Closing message
print ("Thank you for dining with us! Have a wonderful day!")