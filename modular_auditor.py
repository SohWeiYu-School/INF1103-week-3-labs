""" 
INF1103 Week 3 - Modular Auditor
"""

inventory_units = 0
number_of_failed_attempts = 0

#Global Constant
MAX_CAPACITY = 500
TAX_RATE = 0.1 # 10% tax rate

def get_valid_input(input):

    if input == "quit":
        return "quit"
    elif not user_input.lstrip('-').isdigit():
        number_of_failed_attempts+=1
        print("Invalid input. Please enter a valid stock quantity or 'quit' to exit")
    elif int(user_input) <0:
        number_of_failed_attempts+=1
        print("Invalid input. Please enter a non-negative stock quantity or 'quit' to exit")
    else:
        if inventory_units + int(user_input)>500:
            number_of_failed_attempts+=1
            print("Overstock alert! You cannot add " + str(user_input)+ " items. Maximum capacity is 500.")

def calculate_tax(amount):
    tax_rate = 0.15
    tax_amount = amount * tax_rate
    return tax_amount

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total


def generate_report(total_units, failed_attempts):
    print("Exiting the program. " + "Total units processed: " + str(total_units) + ". Number of failed attempts: " + str(failed_attempts) )


while True:
    user_input=input("Enter stock quantity or 'quit' to exit: ")
    get_valid_input(user_input)


    

