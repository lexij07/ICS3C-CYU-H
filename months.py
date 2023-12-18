# Programmer: Lexi
# Description: Days in a month

months = [
    "January", 
    "February", 
    "March", 
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

month_chosen = input("Enter a month:")
while month_chosen not in months:
    print("Invalid Month")
    month_chosen = input("Enter a month:")

if month_chosen in ["January", "March", "May", "July", "August", "October", "December"]:
    print(f"{month_chosen} has 31 days")
    
if month_chosen in ["April", "June", "September", "Novemeber"]:
    print(f"{month_chosen} has 30 days")
    
if month_chosen in ["February"]:
    print(f"{month_chosen} has 28 or 29 days")
   
