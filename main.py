#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the tip Calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("Split the bill among how many people? "))

tip_as_percent = tip / 100
total_tip_amount = round((bill * tip_as_percent),2)

total_bill = round((bill + total_tip_amount),2)

bill_per_person = (total_bill / people)
final_amount = round(bill_per_person, 2)

print(f"Total tip is ${total_tip_amount}")
print(f"Total bill is: ${total_bill}")
print(f"Each person should pay: ${final_amount}")

