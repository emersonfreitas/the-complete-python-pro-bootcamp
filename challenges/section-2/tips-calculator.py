#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? ")
tip = input("How much tip wold you like to give? 10, 12 or 15? ")
amount_people = input("How many people to split the bill? ")

total_bill_as_float = float(total_bill)
tip_as_float = float(f"1.{tip}")
amount_people_as_int = int(amount_people)


result = (total_bill_as_float / amount_people_as_int) * tip_as_float

result_final = "{:.2f}".format(result)

print(f"Each person should pay: ${result_final}")
