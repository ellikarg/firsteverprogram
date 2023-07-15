import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds_new.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Travel_Cost_Index')

tci = SHEET.worksheet('TCI')
data = tci.get_all_values()
country = None
country_list = None


def vacation_days():
    """
    Asks for the days that the user has available and
    Validates the data that the user inserts.
    """
    while True:
        days = input('\nHow many days do you have available? Insert here: ')

        try:
            days = int(days)

        except ValueError:
            print('\nInvalid data entry, please insert a whole number!')
            print("Example: Insert '21' for three weeks")

        else:
            print('>>>Thank you for your input!\n')
            break

    return days


def vacation_country():
    """
    Asks for the country the user wants to travel to.
    """
    global country
    global country_list
    country = input('Where would you like to travel to? Insert a country: ')
    country_list = tci.col_values(1)
    validate_country()
    return country


def validate_country():
    """
    Validates the user input for a country and calls the search_country
    Function if the country cannot be found within the country_list.
    """
    global country

    if country in country_list:
        print(f'>>>Thanks, the country {country} is in my list!')
    else:
        search_country()

    return


def search_country():
    """
    Gives the user two options to search for the country she/he wants to travel to.
    """
    global country
    global country_list
    print(f'\nOh no, the country {country} is not in my list.')
    search_country_options = """
    \nWhat do you want to do now?
    \n1: Maybe I mistyped, let me insert the first letter of the country I want to go to
2: Show me an alphabetical list of all 132 countries"""
    print(search_country_options)

    while True:
        no_country = input('\nPlease choose one of the options above: ')
        if no_country == '1':
            country_first_letter = input(
                "\nAlright, let's try! Please insert the first (capitalized) letter of the country you are thinking of (e.g. 'A'): ")
            first_letter_list = [entry for entry in country_list if entry.startswith(country_first_letter)]
            print(f'Here is a list of all countries that start with {country_first_letter}: ')
            print(first_letter_list)
            country_from_letter = input('\nPlease insert one of the countries from the list above: ')
            country = country_from_letter
            validate_country()
            break
        elif no_country == '2':
            print(country_list)
            country_from_list=input(
                '\nPlease choose one of the countries listed above: ')
            country=country_from_list
            validate_country()
            break
        else:
            print("\nInvalid data entry, please insert either '1' or '2'.")

    return


def vacation_level():
    """
    Asks for the level of adventure/comfort that the user would like to experience and
    Validates the data that the user inserts.
    """
    options=['a', 'b', 'c', 'd']
    print('\nWhich level of adventure/comfort do you want to experience?\n')
    vacation_level_options="""
    Please choose a letter from the following options:
a: I'll travel like a backpacker
b: I'll want some fancy hotels and food once in a while
c: I'm all luxury
d: I'm fed up with tourism - I want to live there like a local!
    """
    print(vacation_level_options)

    while True:
        level=input(
            '\nPlease choose one of the options by inserting the according lowercase letter: ')
        if level not in options:
            print("\nInvalid data entry, please insert 'a', 'b', 'c' or 'd'.")
        else:
            break
    return level


def get_tci(country_input, level_input):
    """
    Searches for the country the user entered in the excel worksheet 'TCI',
    Searches for the level of adventure/comfort that the user entered and
    Retrieves the correct Travel-Cost-Index (TCI) for the right country and
    The right level of adventure/comfort.
    """
    print('\n>>>Thank you for your request!\nYour Travel-Cost-Index is being calculated...')
    country_cell=tci.find(country_input)
    country_row=country_cell.row
    level_cell=tci.find(level_input)
    level_col=level_cell.col
    country_level=tci.cell(country_row, level_col).value
    return country_level


def get_budget(tci_user, days_input):
    """
    Calculates the budget the user needs to undertake the Travel by
    Multiplying the TCI from the get_tci() function with the number
    Of days the user has available for the travel.
    """
    global country
    print('\nYour Travel-Cost-Index is ready:')
    budget="{:.2f}".format(round(float(tci_user), 2) * days_input)
    print(f'You will need {tci_user} € per day as soon as you are in {country}. For your travel of {days_input} days you will need a budget of {budget} €!')
    return budget


def main():
    """
    Calls all the functions above.
    """
    days_input = vacation_days()
    country_input=vacation_country()
    level_input = vacation_level()
    tci_user = get_tci(country_input, level_input)
    get_budget(tci_user, days_input)


print("\nHappy to see you at the Travel Cost Calculator!")
main()
