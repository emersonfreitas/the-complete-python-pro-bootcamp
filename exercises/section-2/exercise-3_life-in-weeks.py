"""
I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

https://waitbutwhy.com/2014/05/life-weeks.html

Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.
"""
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
conveted_age_to_int = int(age)

# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months
year_in_days = 365
year_in_weeks = 52
year_in_months = 12
max_year = 90

age_in_days = year_in_days * conveted_age_to_int

days_age_left = (max_year * year_in_days) - age_in_days

age_in_weeks = year_in_weeks * conveted_age_to_int

weeks_age_left = (max_year * year_in_weeks) - age_in_weeks

age_in_months = year_in_months * conveted_age_to_int

months_age_left = (max_year * year_in_months) - age_in_months

print(f"You have {days_age_left} days, {weeks_age_left} weeks, and {months_age_left} months left.")
