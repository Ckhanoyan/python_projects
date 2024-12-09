print("welcome to the rollercoaster!")
height = int(input("what is your height in cm?"))
bill = 0

if height >= 120:
  print("you can ride the rollercoaster!")
  age = int(input("what is your age?"))
  
  if age < 10:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Your ticket is $7.")
  elif age >= 45 and age <= 55:
    print("Everything will be okay. You have a free ride on us!")
  else:
    bill = 12
    print("Your adult ticket is $12.")

  photo = input("Do you want a photo taken? (Yes/No)")
  if photo == "Yes":
    bill += 3
  
  print(f"Your final price is ${bill}. Please pay at the counter.")

else: 
  print("you cannot ride a rollercoaster.")
