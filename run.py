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


def vacation_days():
    """
    Asks for the days that the user has available and
    Validates the data that the user inserts.
    """
    while True:
        days = input('How many days do you have available? Insert here: ')

        try:
            days = int(days)
            break

        except ValueError:
            print('\nInvalid data entry, please insert a whole number!')
            print("Example: Insert '21' for three weeks\n")

    return days


def vacation_country():
    """
    Asks for the country the user wants to travel to.
    """
    country = input('Where would you like to travel to? Insert a country: ')
    country_list = tci.col_values(1)
    if country in country_list:
        print(f'The country {country} is in the list')
    else:
        print(f'The country {country} is not in the list')
    
    return country


def vacation_level():
    """
    Asks for the level of adventure/comfort that the user would like to experience and
    Validates the data that the user inserts.
    """
    options = ['a', 'b', 'c', 'd']
    print('\nWhich level of adventure/comfort do you want to experience?\n')
    print('Please choose a letter from the following options:')
    print("a: I'll travel like a backpacker\nb: I'll want some fancy hotels and food once in a while\nc: I'm all luxury\nd: I'm fed up with tourism - I want to live like a local!\n")
    while True:
        level = input(
            'Please choose one of the options by inserting the according lowercase letter: ')
        if level not in options:
            print("\nInvalid data entry, please insert 'a', 'b', 'c' or 'd'")
        else:
            break
    return level


def get_tci(country_input, level):
    """
    Searches for the country the user entered in the excel worksheet 'TCI',
    Searches for the level of adventure/comfort that the user entered and
    Retrieves the correct Travel-Cost-Index (TCI) for the right country and 
    The right level of adventure/comfort.
    """
    country_cell = tci.find(country_input)
    country_row = country_cell.row
    level_cell = tci.find(level)
    level_col = level_cell.col
    country_level = tci.cell(country_row, level_col).value
    print(country_level)

    return country_level


def main():
    """
    Calls all the functions above.
    """
    # vacation_days()
    country_input = vacation_country()
    level = vacation_level()
    get_tci(country_input, level)


print("Happy to see you at the Travel Cost Calculator!")
main()
