print("welcome to the tip calculator.")
bill = float(input("what was the total bill? $"))
tip = int(input("what % would you like to tip? 20? 15? 10? "))
friends = int(input("how many friends of yours should be paying each? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
per_person_bill = total_bill / friends
final_amount = round(per_person_bill, 2)
print(f"each person should pay: ${final_amount}")
