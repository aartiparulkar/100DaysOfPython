print("Welcome to the tip calculator!")

# Enter the split details
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# Calculate the amount each person have to contribute
tip_as_percent = tip / 100
total_bill = bill * (1 + tip_as_percent) 
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

# Display the spit
print(f"Each person should pay: ${final_amount}")


