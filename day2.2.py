# Tip Calculator
# print welcome to the tip calculator
#what was the total bill ?
#what percentage tip would you like to a give ? 10,12,15
#how many people to split the bill ?
#each pearson should pay


print("##Welcome to the tip calculator##")
bill = float(input("what is total bill amount:"))
tip = int(input("what percenatge tip would you like to a give , 10 , 12 or 15 ?"))
people = int(input("how many people split the bill ?"))
bill_with_tip = tip/100*bill+bill
print(bill_with_tip)
total = bill_with_tip/people
print("each pearosn payable amount is:\n",total)

