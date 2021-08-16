####################################################################################################
# Programming Project 1
# Author: <your name>
# ID Number: <your student ID number>
# Course: <your course>
# Description:
""" <program description>
"""
####################################################################################################

# Replace the "None" keyword with your ID number below (e.g. 11264500)
student_id = 12035939
# Replace the "None" keyword with your full name below (e.g. Dino Dominic Forte Ligutan)
student_name = Kianna Louise Eleserio Dacanay

# Note: Remember to remove the "raise NotImplementedError()" statements below

## Implement Feature 1 here
""" The function below should display a customary greeting and then ask for user's name and ID 
number. It should return the user name and ID number (as a string) as a tuple data type
(i.e. ("Dino", "20192118")).
"""
def greetings():
    

## Implement Feature 2 & 3 here
""" The function below should display the menu items in specified output display format.
"""
def display_menu():
    

## Implement Feature 4, 5 & 6 here
""" The function below will process the user input (selected item price and quantity) and compute
the running subtotal. It accepts the previous subtotal (through the subtotal parameter) and returns 
the new subtotal. This function must be called at most three times in your program.
"""
def compute_cost(subtotal):
    

## Implement Feature 7 here
""" The function below will display the allowed item pickup time options then ask for a selection.
Afterwards, it will ask for user confirmation of the transaction. This function should return a
string containing the selected pickup time information (e.g. "2:00 PM to 3:00 PM")
"""
def select_pickup():
    

## Implement Feature 8 here
""" The function below will display order summary then it asks the user for confirmation. The
function must return a boolean which becomes a True when the user confirms. It is False 
otherwise.
"""
def confirm(subtotal, pickupTime):
    

## Implement receipt displaying function here
"""
This function will display the output receipt in the presribed format as required for this project.
"""
def display_receipt(name, id, orderName1=None, orderPrice1=None, orderQuantity1=None,
                    orderName2=None, orderPrice2=None, orderQuantity2=None,
                    orderName3=None, orderPrice3=None, orderQuantity3=None,
                    pickupTime):
    

# The function below will be called when you run this program
# Decide what statements should be inside this function to meet the requirements
# Remember to remove the "raise NotImplementedError()" statement
def main_menu():
    

# DO NOT MODIFY THE CODE BELOW THIS LINE!
####################################################################################################
if __name__ == '__main__':
    main_menu()