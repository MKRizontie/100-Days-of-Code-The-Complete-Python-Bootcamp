print("Ring... Ring...")
print("Delivery Service: Hello, thank you for calling Python Pizza. How can I assist you today?\n")

print("You: I'd like to order a pizza.")

size = input("Delivery Service: What size pizza would you like? S, M or L: ").upper()

if size == 'S':
    total_price = 15
elif size == 'M':
    total_price = 20
elif size == 'L':
    total_price = 25
else:
    print("Delivery Service: Sorry, we only offer S, M, or L sizes. Please choose again.")
    size = input("Delivery Service: What size pizza would you like? S, M or L: ").upper()

if size in ['S', 'M', 'L']:
    pepperoni = input("Delivery Service: Do you want pepperoni on your pizza? Y or N: ").upper()
    extra_cheese = input("Delivery Service: Do you want extra cheese? Y or N: ").upper()

    if pepperoni == 'Y':
        if size == 'S':
            total_price += 2
        elif size == 'M' or size == 'L':
            total_price += 3

    if extra_cheese == 'Y':
        total_price += 1

    print("\n--- Order Summary ---")
    print(f"Pizza size: {size}")
    print(f"Pepperoni: {pepperoni}")
    print(f"Extra Cheese: {extra_cheese}")
    print(f"Total Pizza Price: ${total_price}\n")

    print("Delivery Service: Okay, let me confirm your order...")
    input(f"Delivery Service: So, you've ordered a {size} pizza with {'pepperoni' if pepperoni == 'Y' else 'no pepperoni'} and {'extra cheese' if extra_cheese == 'Y' else 'no extra cheese'}. Is that correct? Press Enter to confirm.")
    input("Delivery Service: Your pizza will be delivered in 30 minutes. Anything else I can assist you with? Press Enter to continue.")

    tip = input("Delivery Service: Would you like to leave a tip for the delivery driver? Y or N: ").upper()
    if tip == 'Y':
        tip_percentage = input("Delivery Service: How much tip percentage would you like to give? (e.g., 10, 15, 20): ")
        tip_amount = total_price * (float(tip_percentage) / 100)
        print(f"Delivery Service: Thank you! You've chosen to give a {tip_percentage}% tip, which is ${tip_amount:.2f}.")
    else:
        tip_amount = 0
        print("Delivery Service: Thank you for your order. No tip will be given this time.")

    total_with_tip = total_price + tip_amount
    print("\n--- Final Total ---")
    print(f"Total Pizza Price: ${total_price}")
    print(f"Tip Amount: ${tip_amount:.2f}")
    print(f"Total with Tip: ${total_with_tip:.2f}")

    input(f"Delivery Service: Your total is ${total_with_tip:.2f}. Thank you for your order! Press Enter to confirm.")

    print("\nDelivery Service: Your pizza will be delivered shortly. Have a great day!")
    print("You: Thank you for the pizza!")

    print("\nThank you for using Python Pizza Deliveries. Enjoy your meal!")

