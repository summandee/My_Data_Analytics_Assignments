#            ********       Question 1     *********
#      **********    Age Group Classification

##  Write a Python program that takes the age of a person as input and classifies them into one of the
##  following age groups:
##  Child if the age is between 0 and 12 (inclusive).
##  Teenager if the age is between 13 and 19 (inclusive).
##  Adult if the age is between 20 and 64 (inclusive).
# First Program:
age = int(input("Enter your age: "))

if age >= 0 and age <= 12:
  print("Your age group is Child")
elif age >= 13 and age <= 19:
  print("Your age group is Teenager")
elif age >= 20 and age <= 59:
  print("Your age group is Adult")
else:
  print("Your age group is Senior Citizen")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# 2nd Program:
age_input = int(input("Enter the age of the person: "))

if age_input < 0:
      print( "Invalid age")
elif 0 <= age_input <= 12:
    print(" Age_Group is : Child")
elif 13 <= age_input <= 19:
    print("Age_Group is : Teenager")
elif 20 <= age_input <= 64:
    print("Age_Group is : Adult")
else:
    print("Age_Group is : Senior")

#________________________________________End Q-1_____________________________________________

#            ********       Question 2       *********
##           ********    Checking for Eligibility for Discount   *******
# 
## Write a Python program that determines if a customer is eligible for a discount. The program should
## take the customer's membership status and purchase amount as input and check the following
## conditions:
## The customer is a premium member and the purchase amount is greater than or equal to 1000.
## The customer is a regular member and the purchase amount is greater than or equal to 2000.
## If the customer meets either of the above conditions, print Eligible for discount, otherwise print
## Not eligible for discount.

# First Program :
membership_status = input("Enter your status: premium/regular :")
purchase_amount = int(input("Enter the purchase amount"))
if membership_status == "premium" and purchase_amount >= 1000:
    print("Eligible for discount")
elif membership_status == "regular" and purchase_amount >= 2000:
    print("Eligible for discount")
else:
    print("Not eligible for discount")

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# 2nd Program :
membership_status = input("Enter your status: premium/regular :")
purchase_amount = int(input("Enter the purchase amount"))

if (membership_status == "premium" and purchase_amount >= 1000) or (membership_status == "regular" and purchase_amount >= 2000):
    print("Eligible for discount")
else:
    print("Not eligible for discount")

#  _______________________________________End Q-2______________________________________________

#            ********       Question 3        *********
##           ********   Voting Eligibility Check     *******
##  Write a Python program that checks if a person is eligible to vote based on their age and citizenship
##  status. The program should take the following inputs:
##  Age (an integer).
##  Citizenship status (a string: either citizen or on-citizen).
##  The eligibility conditions are:
##  The person must be at least 18 years old and a citizen to be eligible to vote.
##  Alternatively, the person can be at least 16 years old and a citizen of a special region where voting is
##  allowed from age 16.
##  If the person meets either of the conditions, print Eligible to vote, otherwise print Not eligible to
##  vote.

# Take user input for age
age = int(input("Enter your age: "))
# Take user input for citizenship status
<<<<<<< HEAD
citizenship_status = input("Enter your citizenship status (citizen/non-citizen): ").strip().lower()
special_region = input(" special region : yes or no ")

# Check eligibility based on the conditions
if  (age >= 16 and citizenship_status == "citizen") and (special_region == "yes") or \
=======
citizenship_status = input("Enter your citizenship status (citizen/non-citizen):").strip().lower()
special_region = input("special region yes/no : ")

# Check eligibility based on the conditions
if  (age >= 16 and citizenship_status == "citizen") and\
    (special_region == "yes") or \
>>>>>>> e79061c83bf60ddde06d9186e700bffb1ce300e4
    (age >= 18 and citizenship_status == "citizen"): 

    print("Eligible to vote")
else:
    print("Not eligible to vote")

#__________________________________________End Q-3_______________________________________________

#            ********       Question 4       *********
##           ********    Employee Salary Bonus Eligibility    *******

##  Write a Python program that determines if an employee is eligible for a salary bonus based on the
##  following conditions:
##  The employee performance rating is Excellent and their years of service are greater than or equal
##  to 5 years.
##  The employee performance rating is Good and their years of service are greater than or equal to
##  10 years.
##  The employee performance rating is Satisfactory or their years of service are greater than or
##  equal to 15 years.
##  The employee is not eligible for a bonus if neither of these conditions is met.
##  The program should print one of the following:
##  Eligible for bonus if the employee meets any of the criteria.
##  Not eligible for bonus if none of the conditions apply.

##           ***  Employee Salary Bonus Eligibility  **

years_of_service = int(input("Enter your years of service: "))
employee_performance_rating = input("Enter your performance (Excellent/Good/Satisfactory): ").strip().lower()

if (years_of_service  >= 5 and employee_performance_rating == "Excellent") or \
   (years_of_service  >= 10 and employee_performance_rating == " Good ") or\
   (years_of_service  >= 15 and employee_performance_rating == "Satisfactory"): 
    print("Eligible for bonus")
else:
    print("Not Eligible for bonus")
    
    
#__________________________________________End Q-4_______________________________________________



#            ********       Question 5       *********

##           ********    replaces spaces with underscores / count Underscores / position of the first underscore     *******

#  Write a program that replaces spaces with underscores, counts how many underscores are there, and finds the position of the first underscore.
#   Use text: "I'm learning Python programming"?

text = "I'm learning Python programming"
text = text.replace(" ", "_")
count = text.count("_")
first_position = text.find("_")
print(f"Text with spaces replaced with underscores: {text}\nCount :  {count}\nFirst_Position : {first_position}")
## Output :
## Text with spaces replaced with underscores: I'm_learning_Python_programming
## Count :  3
## First_Position : 3

#__________________________________________End Q-5_______________________________________________


#                ********       Question 6      *********
#           ***********     Takes a string as input  ************* 

# Write a Python program that: Takes a string as input :
string_input  = input("Enter your string here")

# Prints all characters of the string except the last 3 using slicing.
print(string_input[:-3])
  
# Prints every second character of the string using slicing.
print(string_input[0::2])

# Prints the string in reverse using slicing
print(string_input[::-1])

#__________________________________________End Q-6______________________________________________

#            ********       Question 7      *********


#  Given a sentence, you need to reverse the order of the words in the sentence while
#  preserving their original capitalization and spaces.
#   Use text : "Hello World, We are learning Python"

text =  "Hello World, We Are  learning Python"
# Split the text into words
words = text.split()
# Reverse the order of the words
words = words[::-1]
# Join the words back into a sentence
sentence = ' '.join(words)
print(sentence)
## Output :
##   Python learning are We World, Hello

#__________________________________________End Q-7_____________________________________________

#                ********       Question 8     *********
#       **************    Extract and return the numbe      ************

    # You have a product code that follows the format "SKU-12345-XYZ".
    # You need to:Remove the "SKU-" and the "-XYZ" from the product code.
    # Extract and return the number  
product_code = "SKU-12345-XYZ"
# Remove the "SKU-" and the "-XYZ" from the product code
product_code = product_code.replace("SKU-", "").replace("-XYZ", "")
# Extract and return the number
number = product_code
print(number)
    
#__________________________________________End Q-8____________________________________________

#                ********       Question 9    *********
#         *************     check user password Authentication   *************

##   Write a Python program to check user password has following:
# Whether the string contains any uppercase characters.
# Whether the string contains any lowercase characters.
#  Whether the string contains any spaces.
# Whether the string contains any special 
#Whether the string contains any spaces.
# Whether the string contains any special characters (anything other than letters, digits, and spaces).

# Input password from the user
password = input("Enter your password: ")
if password.upper():
    print("has_upper_characters  : True")
else:
    print("has_upper_characters  : False")
if password.lower():
    print("has_lower_characters  : True")
else:
    print("has_lower_characters  : False")
if password.isdigit():
    print("has_digits  : True")
else:
    print("has_digits  : False")
if password.isspace():
    print("has_characters_spaces  : True")
else:
    print("has_characters_spaces  : False")
if not password.isalnum():
    print("has_special_characters  : True")
else:
    print("has_special_characters  : False")

#__________________________________________End Q-9___________________________________________

#                ********       Question 10  *********
#         **********     Find the Longest Word     ************

#  Write a Python program that finds the longest word in a given string.
#  Example:
#  Input: "I love programming in Python"
#  Output: "programming"
text_string = "I love programming in Python"
# Split the sentence into words
words = text_string.split()
# Find the longest word
longest_word = max(words, key=len)  
print(longest_word)
#  output :
#  programming
#__________________________________________End Q-10_________________________________________

