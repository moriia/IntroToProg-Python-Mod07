# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Pickling and Exception handling in Python
# ChangeLog (Who,When,What):
# mariia, 03.01.2023, Modified code to complete assignment 07
# ---------------------------------------------------------------------------- #
# import --------------------------------------------------------------------- #
import pickle

# Declare variables and constants -------------------------------------------- #
file_name = "pickle.dat"
paycheck = {}  # A dictionary with 2 keys "person_name" and "salary_dollars"
paychecks_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection


# Processing  --------------------------------------------------------------- #

# Adding new row to the list ------------------------------------------------ #

def add_new_row(lst):
    if not lst:  # check in case paycheck_list does not exist
        lst = []
    person_name = input("Enter a name: ")  # input for new username
    while True:  # loop for validation if salary entered as a digit
        try:
            salary_dollars = float(input("Enter a salary in $ :"))
            break
        except ValueError:  # exception in case entered value for salary cannot be cast as a number
            print("Error! Entered value is not a number")  # Error message shown to user in case of string input
    row = {"person_name": person_name.strip(), "salary_dollars": salary_dollars}  # Build a dictionary
    lst.append(row)  # add a dictionary row to the table/list of items
    return lst


# Editing existing row in the table ---------------------------------------- #
#!!!
# ---known limitation - function find the first match only
#!!!
def edit_person_salary(lst):
    if not lst:
        print("There is no paychecks to edit")
    else:
        person_name = input("Enter a name: ").strip()
        i = 0
        for row in lst:
            i += 1
            if row["person_name"].lower() == person_name.lower():
                while True:
                    try:
                        new_salary = float(input("Enter a salary in $ :"))
                        break
                    except ValueError:
                        print("Error! Entered value is not a number")  # Error message in case of string input
                row["salary_dollars"] = new_salary
                break
            elif row["person_name"].lower() != person_name.lower() and i == len(lst):
                print("The person does not exist in the list")


# Saving data to the file ------------------------------------------------ #

def save_data_to_the_file(lst):
    try:
        with open(file_name, 'wb') as file:  # writing data to the file by erasing previously existing
            pickle.dump(lst, file)
        print("Data saved!")
    except Exception as e:  # exception in case error will happen while writing
        print(f"An error occurred while saving the data: {e}")


# Load data from file and displaying it ---------------------------------- #

def load_data_from_the_file_and_display_it(lst):
    try:
        with open(file_name, 'rb') as file:
            lst = pickle.load(file)
            if not lst:
                print("There is no data, file is empty")
            else:
                print("--------------------------------------------")
                print("There is next data:")
                for row in lst:
                    print(row.get("person_name"), row.get("salary_dollars"))
                print("--------------------------------------------")
    except FileNotFoundError:
        print("No file found")
        print("\n")
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        print("\n")
    finally:
        return lst


# Displaying data to the user ---------------------------------- #

def display_data(lst):
    if not lst:
        print("There is no data to show")
    else:
        for row in lst:
            print(row.get("person_name"), row.get("salary_dollars"))


# Exiting the program  ---------------------------------- #

def exit_program():
    print("Goodbye!")
    exit()


# Printing the main menu  ---------------------------------- #

def print_main_menu():
    print('''
        Please choose one of the following options: 
        1. Add a new paycheck 
        2. Edit existing person salary
        3. Display the data
        4. Save data to the file
        5. Exit program
        ''')


# Receiving user choice ---------------------------------- #

def get_user_choice():
    choice_entered = input("Enter your choice: ")
    return choice_entered


# Defining Python user-defined exceptions  ---------------------------------- #

class ValidationErrorOfUserChoice(Exception):
    """Exception raised for case user entered wrong value.

       Attribute:
           user_choice -- users input
        Message explain of the error
    """

    def __init__(self, user_choice):
        # Call the base class constructor with the parameters it needs
        self.user_choice = user_choice
        self.message = f"\n -----! Error ! -----  \n" \
                       f"Entered value - {user_choice} is not correct.\n" \
                       f" Please choose a valid option.\n" \
                       f"Valid options are 1,2,3,4,5 and 6" \
                       f"\n -----! Error ! -----  \n"

    def __str__(self):
        return self.message


# Main Body of Script  ------------------------------------------------------ #

# Start the program
print("\n")
print("Welcome!")
print("\n")
print("About to load data exiting in the file ...")

# Load data from the file
paychecks_lst = load_data_from_the_file_and_display_it(paychecks_lst)

while True:
    # Print main menu to user
    print_main_menu()
    # Get user's choice
    choice_str = get_user_choice()

    if choice_str.lower().strip() == "1":
        # Add new row
        paychecks_lst = add_new_row(lst=paychecks_lst)
        continue

    elif choice_str.lower().strip() == "2":
        # Edit salary
        edit_person_salary(lst=paychecks_lst)
        continue

    elif choice_str.lower().strip() == "3":
        # Display data from the list
        display_data(lst=paychecks_lst)
        continue

    elif choice_str.lower().strip() == "4":
        # Save data to the file
        save_data_to_the_file(lst=paychecks_lst)
        continue

    elif choice_str.lower().strip() == "5":
        # Exit the program
        exit_program()

    else:
        try:
            raise ValidationErrorOfUserChoice(user_choice=choice_str)
        except ValidationErrorOfUserChoice as e:
            print("Caught the exception " + repr(e) + e.message)
        continue
