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
    Ask for the days that the user has available
    Validate the data that the user inserts
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
    Ask for the country the user wants to travel to
    """
    country = input('Where would you like to travel to?\n')
    return country


def vacation_level():
    """
    Ask for the level of adventure/comfort that the user would like to experience
    Validate the data that the user inserts
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


def main():
    """
    Call all the functions above
    """
    vacation_days()
    # vacation_country()
    vacation_level()


print("Happy to see you at the Travel Cost Calculator!")
main()
