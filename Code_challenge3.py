# Get information
sender_name = input("Sender name: ")
type_of_item = input("Type of item: ")

weight = float(input("Weight in kg: "))
distance = float(input("Distance in km: "))

is_fragile = input("Is it fragile? Yes/No: ") == "Yes"
is_express = input("Is it express? Yes/No: ") == "Yes"
is_international = input("Is it international? Yes/No: ") == "Yes"


# Calculate base cost
base_cost = (weight * 2.50) + (distance * 0.15)


# Decide the final price
if weight <= 2 and distance <= 100 and not is_express and not is_international:
    total = 0

elif is_international and is_express:
    total = (base_cost * 1.40) + 50

elif is_express or (is_international and weight > 20):
    total = (base_cost * 1.20) + 25

elif weight > 30 or distance > 1000:
    total = base_cost + 30

else:
    total = base_cost


print("Total shipping cost: Php", format(total, ".2f"))