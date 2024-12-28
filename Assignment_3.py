#  Q1. Write program to check a person’s eligibility for a loan based on age, credit score, and income.
#  This time, the eligibility criteria will be:
#  The person must be 18 years or older. 
#  The person must have a credit score of 650 or higher. 
#  The person must have an annual income of at least 30000 dollars 
#  If the person has a credit score of 700 or higher, 
#  they may still be eligible with an income of 25000 dollars or more

## ____________________________  Q1 _________________________________
age = int(input("Enter the person's age : ")) 
if (age < 18 or age > 65 ):
    print("Please enter Correct age.")
else:
    credit_score = int(input("Enter the person's credit score : "))
    annual_income = int(input("Enter the person's  monthly income : "))
    if (credit_score >= 650 or credit_score >= 700) and (annual_income == 30000 or annual_income >= 25000  ):
        print("Eligible for loan")
    else:
        print("Not Eligible for loan")

#*******************************  End  **********************************

    
##  Q2. Write a Python program that checks if a person is an adult (age ≥ 18).
##  Take the age as input.
##  If the person is underage (age < 18), show message: "You are underage" and don't ask for experience.
##  If the person is an adult, take years of experience as input and print:
##  "You have a lot of experience." (10+ years)
##  "You have moderate experience." (5-9 years)
##  "You are relatively new." (2-4 years)
##  "You are just starting out." (less than 2 years) 
## __________________________   Q2   _____________________________   

# Get the person's age and experience
age = int(input("Enter the person's age: "))
# Check the conditions and print the appropriate message
if age < 18:
    print("You are underage and don't ask for experience.")
else:
    x = experience = int(input("Enter the person's experience: "))
    if (10 == x <= 15):
      print("You have a lot of experience.")
    elif (5 <= x <= 9):
        print("You have moderate experience.")
    elif (2 <= x <= 4):
        print("You are relatively new.")
    elif (x < 2):
        print("You are just starting out.")
    else:
        print("x level not categorized.")
            
            

##  *********************************************************************

##  _________________________________   Q-3   ____________________________________
# # a) Print their memory address (to check if python assigns same address of different variables having same element)
# Variables with the same value
a = 100
b = 100
c = "hello"
d = "hello"

# Print memory addresses
print(f"Memory address of a (100) : {id(a)}")
print(f"Memory address of a (100): {id(a)}")
print(f"Memory address of b (100): {id(b)}")
print(f"Memory address of c ('hello'): {id(c)}")
print(f"Memory address of d ('hello'): {id(d)}")

#extra variables to explore different values
e = 200
f = 200
print(f"Memory address of e (200): {id(e)}")
print(f"Memory address of f (200): {id(f)}")
#Output:
# memory address of a : 135453182299472
# memory address of b : 135453182299472
# memory address of c : 135452756370032
# memory address of d : 135452756370032
# Memory address of e (200): 135453182302672
# Memory address of f (200): 135453182302672
##   ______________________________________________
## b) Find memory size and append them in a list, use this list to find data type having least memory size
## c) Print final name of data type which has lowest memory
## b) Find memory size and append them in a list, use this list to find data type having least memory size
## c) Print final name of data type which has lowest memory
import sys
memory_size_list = []
variable_list = []
# Define variables
x = 100                            # Integer
memory_size_x = sys.getsizeof(x)
memory_size_list.append(memory_size_x )
variable_list.append(x)

y = 3.14                           # Float
memory_size_y = sys.getsizeof(y)
memory_size_list.append(memory_size_y )
variable_list.append(y)


z = "hello"                        # String
memory_size_z = sys.getsizeof(z)
memory_size_list.append(memory_size_z )
variable_list.append(z)


a = [1, 2, 3]                     # List
memory_size_a = sys.getsizeof(a)
memory_size_list.append(memory_size_a )
variable_list.append(a)

k = (1, 2, 3)                     # Tuple
memory_size_b = sys.getsizeof(k)
memory_size_list.append(memory_size_b )
variable_list.append(k)

m = {"key": "value"}              # Dictionary
memory_size_c = sys.getsizeof(m)
memory_size_list.append(memory_size_c )
variable_list.append(m)

n = True                           # Boolean
memory_size_d = sys.getsizeof(n)
memory_size_list.append(memory_size_d )
variable_list.append(n)

e = None                           # NoneType
memory_size_e = sys.getsizeof(e)
memory_size_list.append(memory_size_e )
variable_list.append(e)

# Print memory size list
print(f"Memory size : {memory_size_list} bytes")
# Find the data type with the least memory size
min_size_index = memory_size_list.index(min(memory_size_list))
print(f"min size index : {min_size_index}")
least_memory_variable = memory_size_list[min_size_index]
print(variable_list)

least_memory_size = memory_size_list[min_size_index]
print(f"least memory size : {least_memory_size}")
print(f"least memory variable : {variable_list[7]}")
print(min_size_index )

## Output:
# Variable: 100, Type: int, Size: 28 bytes
# Variable: 3.14, Type: float, Size: 24 bytes
# Variable: hello, Type: str, Size: 54 bytes
# Variable: [1, 2, 3], Type: list, Size: 64 bytes
# Variable: (1, 2, 3), Type: tuple, Size: 56 bytes
# Variable: {'key': 'value'}, Type: dict, Size: 64 bytes
# Variable: True, Type: bool, Size: 28 bytes
# Variable: None, Type: NoneType, Size: 16 bytes

# Memory size : [28, 24, 54, 88, 64, 232, 28, 16] bytes
# min size index : 7
# [100, 3.14, 'hello', [1, 2, 3], (1, 2, 3), {'key': 'value'}, True, None]
# least memory size : 16
# least memory variable : None
# Variable with least memory size: None (<class 'NoneType'>)
# Memory size: 16 bytes
##  ***************************************************************
## _____________________________  Q-4   _____________________________
# Q4. Write a Python program that asks the user to enter an email address. The program should check if the email
# contains the characters @ and "."(ignoring case). If either character is present, print "Email format is valid."
# Otherwise, print "Invalid email format."

# Prompt the user to enter an email address
email = input("Enter your email address: ").strip().lower() 

# Check for '@' and '.' in the email (ignoring case)
if '@' in email and '.' in email:
    print("Email format is valid.")
else:
    print("Invalid email format.")
##  **********************************
## ___________________________  Q-5  ___________________________
# Q5. Write a python program to know data type of each element stored in a tuple, append the data types in a list.
# Show final output in a list as data types of tuple elements
# x = (11,22.333,'apple',[1,2,3],('a','b'))
# Given tuple
# Simple Method:
x = (11, 22.333, 'apple', [1, 2, 3], ('a', 'b'))
# List to store data types
data_types = []
# Iterate through each element in the tuple and append its data type to the list
data_types.append(type(x[0]).__name__)
data_types.append(type(x[1]).__name__)
data_types.append(type(x[2]).__name__)
data_types.append(type(x[3]).__name__)
data_types.append(type(x[4]).__name__)
print("Data types of tuple elements:", data_types)
#_______________________________________________________
## By Loop:
# Given tuple
x = (11, 22.333, 'apple', [1, 2, 3], ('a', 'b'))

# List to store data types
data_types = []

# Iterate through each element in the tuple and append its data type to the list
for element in x:
    data_types.append(type(element).__name__)
data_types.append(type(x[0]).__name__)
# Display the final list of data types
print("Data types of tuple elements:", data_types)


##  ____________________________ Q-6  ***  ________________________
# #  Q6. Write a Python program that:
# #  Checks if a given username exists in a list of active users.
# #  Verifies if the user is the admin using identity operators.
# #  Hints:
# #  Use a list of tuples where each tuple contains a username and role
# #  [("alice", "admin"),
# #  ("bob", "user"),
# #  ("charlie", "moderator")]
# #  Use the in operator to check if the username exists in the list.
# #  Use the is operator to check if the user is the admin (admin is a specific reference, e.g., ("alice", "admin")).
# #  

# Check if the username exists and determine the role
# user_tuple_list = next((user for user in active_users if user[0] == username), None)

user_tuple_list = [
    ("alice", "admin"),
    ("bob", "user"),
    ("charlie", "moderator"),
    ("taj", "user"),
    ("naheed", "user"),
    ("areeba", "moderator")
]

user_name = input("Enter the username : ")
if (user_name in user_tuple_list[0]):
    print("User exists")
# # Verify if the user is the admin
if user_name in user_tuple_list[0]:
    print("user is admin")
elif user_name in user_tuple_list[1]:
    print("user is user")
elif user_name in user_tuple_list[2]:
    print("user is moderator")
else:
  print("user is not exist")
##  _________________________   Q-7   ________________________
#  Q7. person1 has same family as of person2, write a program to print relation between person1 and person2, if their
#  data is [father-name, mother-name, district, family-number] same (Print relation 'Siblings') also check person1
#  data with person3 which is cousin of person1 (Print relation 'Cousin')
#  Hint:
#  Use identity operator

# Data for each person
person1 = ['John', 'Jane', 'Springfield', '123']
person2 = ['John', 'Jane', 'Springfield', '123']
person3 = ['Mike', 'Mary', 'Springfield', '456']

# is checks for the same object in memory.
# == checks for equal content.

# Check if person1 and person2 are siblings (using identity)
# Assign person1 to person2 (now they refer to the same object)
# Check identity
print(person1 is person2)  # Output: False (different objects)
# person1 is person2 ## This will be False
person2 = person1
if person1 is person2:  # This will be False since they are different objects
    print("Relation: Siblings")
else:
    print("Relation: Not siblings")

# Check if person1 and person3 are cousins (using identity)
person1 = person3
if person1 is person3:  # This will also be False
    print("Relation: Cousin")
else:
    print("Relation: Not Cousin")
 


##  _________________________________   Q-8   ___________________________________
##  Q8. Write a Python program to store and display a books title, author, year of publication, and price using a tuple.
##  Instructions:
##  Create a tuple to store the book details.
##  Ask the user for the books title, author, year, and price.
##  Display the stored book information.
# Prompt the user for book details
title = input("Enter the book title: ")
author = input("Enter the author's name: ")
year = input("Enter the year of publication: ")
price = float(input("Enter the price of the book: "))

# Create a tuple to store the book details
book_details = (title, author, year, price)

# Display the stored book information
print("\nStored Book Information:")
print(f"Title: {book_details[0]}")
print(f"Author: {book_details[1]}")
print(f"Year of Publication: {book_details[2]}")
print(f"Price: ${book_details[3]:.2f}")

##  _____________________________   Q-9  _______________________________
##  Q9. Write a program to check if a user’s chosen subject is available in the list of offered subjects.
##  Instructions:
##  Given a list of subjects, ask the user to input a subject.
##  Display whether the subject is available or not.
subject_list = ["mathematic", "chemistry", "physics", "biology", "arabic", "english" ]
subject = input("Enter the subject").lower()
if subject in subject_list:
   print("Subject is available")
else:
    print("Subject is not available")
##   __________________________________   Q-10  ________________________________
#  Q10. Write a Python program that performs the following tasks using tuple methods
#  Create a tuple with multiple integer values, including duplicates.
#  Prompt the user to input a number and find the index of its first occurrence in the tuple.
#  Ask the user for another number and count how many times it appears in the tuple.
#  Display appropriate messages based on the results
number_tuple = (1,2,3,4,2,5,3,6,7,5,8)
# Prompt the user to input a number and find the index of its first occurrence
first_number = int(input("Enter a number to find its first occurrence: "))


if first_number in number_tuple:
    index_no = number_tuple.index(first_number)
    print(f"The first occurrence of {first_number} is at index {index_no}.")
else:
    print(f"{first_number} is not in the tuple.")
# Ask the user for another number and count how many times it appears in the tuple
second_number = int(input("Enter another number to count its occurrences: "))
count = number_tuple.count(second_number)

# Display the count of occurrences
if (count > 0 ):
    print(f"{second_number} appears {count} times in the tuple.")
else:
    print(f"{second_number} does not appear in the tuple.")
   #**************************************
number_tuple = (1,2,3,4,2,5,3,6,7,5,8)
index_of_2 = number_tuple.index(first_number)
print(index_of_2)  # Output: 1 (the first occurrence of 20)

    
 ##   ********************Question for Hard working learners (Not Mandatory)************************
# Get the current temperature from the user
current_temperature = float(input("Enter the current temperature in Celsius: "))

# Define the predefined temperature values
freezing_point = -5
normal_point = 25
hot_point = 40

# Check the temperature category
if current_temperature <= freezing_point:
    print("It's freezing.")
elif freezing_point < current_temperature < normal_point:
    print("The temperature is normal.")
elif normal_point <= current_temperature < hot_point:
    print("It's warm, a normal temperature.")
else:  # temperature >= hot_point
    print("It's hot.")