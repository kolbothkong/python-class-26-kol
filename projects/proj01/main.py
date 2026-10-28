# Starting file for PROJECT 1
# Include your course number, student first and last name, and date in the comment header
# CS31, Kolboth Kong, October 22, 2026


# Greeting the customer and explaining what the product/service is.
print(" =" * 10)
print(" Pocket Dust Blower")
print(" =" * 10)
print()
# Give the customer a short introduction to the product
print(" Tired of dust building up on your laptop, keyboard, or gaming setup? Meet the Pocket Dust Blower, your new everyday cleaning companion!")
print()
print(" * " * 20)
print()
# Ask if the customer wants to learn more about the product
# Store their answer in the start_sale variable
start_sale = input(" Would you like to learn more about the Pocket Dust Blower? (y/n): ")
print()
# Check if the customer answered yes
# Use upper() to accept both lower and upper case letters
if start_sale.upper() == "Y":
    # Display a message and provide more information about the product
    print(" Amazing news! I can't wait to share some details with you.")
    print(" =" * 25)
    print(" The Pocket Dust Blower is a compact yet powerful cleaning device designed to keep your belongings clean and dust-free.")
    print()
    print(" Despite its small size, it delivers strong airflow that can easily remove dust and dirt from laptops, keyboards, gaming setups, and other electronics.")
    print()
    print(" Its lightweight and pocket-sized design makes it easy to carry wherever you go.")
    print()
    print(" Whether you're at home, school, work, or traveling, the Pocket Dust Blower is always ready to help you clean those hard to reach places.")
    print(" =" * 25)
    print()
    # Ask the customer if they would like to purchase the product
    # Store their answer in the start_purcase variable
    start_purchase = input(" Did I BLOW your mind away enough for you to consider owning one? (y/n): ")
    print()
    print(" =" * 25)
    print()
    if start_purchase.upper() == "Y":
        # Start the ordering process
        print(" That's great! Let's get the order started for you.")
        # Store each answer in a separate variable
        first_name = input(" First, what is your first name? ")
        last_name = input(" And now your last name? ")
        email_address = input(" Now could you provide me with your email address? ")
        phone_number = input(" Finally, what is your phone number? ")
        print()
        # Set the price of one pocket dust blower
        # Display the price to the customer
        price = 14.99
        print(f" Our Pocket Dust Blower starts at ${price} each.")
        print()
        # Ask the customer how many they want to purchase
        # Convert the answer into an integer
        quantity = int(input(" How many would you like to purchase? "))
        print()
        # Display receipt title with decorative lines
        print(" =" * 15)
        print(" POCKET DUST BLOWER RECEIPT")
        print(" =" * 15)
        # Display their information on the receipt
        print(f" Customer's Full Name: {first_name} {last_name}")
        print(f" Email: {email_address}")
        print(f" Phone: {phone_number}")
        print(" =" * 15)
        # Display the quantity purchased and price per item
        print(f" Quantity: {quantity}")
        print(" Price per unit: $14.99")
        print(" -" * 15)
        # Store the total into a variable and calculate the subtotal by multiplying quantity by price
        # Display the subtotal rounded to two decimal places
        subtotal = quantity * price
        print(f" Subtotal: ${subtotal:.2f}")
        # Store the tax into a variable and display amound due and tax in two decimal places
        tax = subtotal * 0.10
        print(f" Tax (10%): ${tax:.2f}")
        print(" =" * 15)
        # Calculate the final total by adding the subtotal and tax
        # Display the total amount due rounded to two decimal places
        total_amount = subtotal + tax
        print(f" Total Amount Due: ${total_amount:.2f}")
        print(" =" * 15)
        # Thank the customer for purchasing the product and end the convo with a funny farewell message
        print()
        print(" Thank you for your purchase! A confirmation email will be sent shortly.")
        print()
        print(" Your very own Pocket Dust Blower will be shipped out within 1-2 business days.")
        print()
        print(" I'd BLOW your mind with a goodbye, but I'll let our Pocket Dust Blower do the blowing! ")
        print()
        print(" Pocket Dust Blower: Small in size. Big in power!")
        # If customer does not want to purchase, end the conversation
    elif start_purchase.upper() == "N":
        print(" Thank you for checking out our product. Have a nice day!")
        # Display error message if the customer enters an invalid answer
    else:
        print(f" Sorry, \"{start_purchase}\" is an invalid response. Try again.")
# If the customer doesn't want to learn more, end the conversation
elif start_sale.upper() == "N":
    print(" Thank you for checking out our product. Have a nice day!")
    # Display error message if the customer enters an invalid answer
else:
    print(f" Sorry, \"{start_sale}\" is an invalid response. Try again.")




        



        



    

