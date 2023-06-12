# my life calculator

age = int(input("enter a age"))
age_as_int = int(age)
years_reamaining = 90-age_as_int
days_reamaning = years_reamaining *365
weeks_reamaining = years_reamaining * 52
months_reamaining = years_reamaining * 12
message = f"you have {years_reamaining} years, {days_reamaning} days ,  {weeks_reamaining} weeks,  {months_reamaining} months, left"
print(message)