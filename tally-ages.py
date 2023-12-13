# Programmer: 
# Description: 

# Read a list of ages from a file into the variable ages
ages_file = open("ages.txt")
ages = [int(age) for age in ages_file]
ages_file.close()

