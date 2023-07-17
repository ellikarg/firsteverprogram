import gspread
from google.oauth2.service_account import Credentials
import time
import textwrap

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Travel_Cost_Index')

tci = SHEET.worksheet('TCI')
regions = SHEET.worksheet('Regions')
data = tci.get_all_values()
country = None
country_list = tci.col_values(1)[1:]


def vacation_days():
    """
    Asks for the days that the user has available and
    Validates the data that the user inserts.
    """
    while True:
        days = input('\n\n***\nHow many days do you have available? \
Insert here:\n')
        try:
            days = int(days)
        except ValueError:
            print('\nThat did not work, please insert a whole number!')
            print('Example: Insert "21" for three weeks')
        else:
            print('>>> Thank you for your input!')
            time.sleep(1)
            break

    return days


def vacation_country():
    """
    Asks for the country the user wants to travel to.
    """
    global country
    global country_list
    country = input('\n\n***\nWhere would you like to travel to? \
Insert a country:\n')
    converted_country = country.lower()
    country = converted_country
    validate_country()

    return country


def validate_country():
    """
    Validates the user input for a country and calls the search_country
    Function if the country cannot be found within the country_list.
    """
    global country
    global country_list

    if country in country_list:
        print(f'>>> Thanks, the country {country.title()} is in my \
database!')
        time.sleep(1)
    else:
        search_country()

    return


def search_country():
    """
    Gives the user two options to search for the country she/he wants to
    Travel to.
    """
    global country
    global country_list

    print()
    print(textwrap.fill(f'>>> Oh no, I cannot find the country {country}. Either it is \
because of a typo or you named a country that is not in my database \
of 132 available countries.'))
    search_country_options = """
    \nWhat do you want to do now?
    \n1: Search by regions
2: Search in the whole list of available countries"""
    print(search_country_options)

    while True:
        no_country = input('\nPlease choose one of the options above \
(insert 1 or 2):\n')
        if no_country == '1':
            search_country_by_region()
            break
        elif no_country == '2':
            search_country_by_list()
            break
        else:
            print('\nThat did not work, please insert either 1 or 2.')

    return


def search_country_by_region():
    """
    Gives the user the option to search a country from a list of regions.
    """
    global country
    global country_list

    regions_list = regions.row_values(1)
    print('\nPlease choose from the regions below:')
    print()
    for value in regions_list:
        print(value.title())

    while True:
        regions_input = input('\nInsert a region to see all the countries \
listed in it:\n')
        converted_regions_input = regions_input.lower()
        if converted_regions_input in regions_list:
            regions_column = regions.find(converted_regions_input)
            regions_column_values = regions.col_values(regions_column.col)[1:]
            print()
            for value in regions_column_values:
                print(value.title())
            while True:
                country_from_region = input('\nPlease insert one of the \
countries listed above:\n')
                converted_country_from_region = country_from_region.lower()
                if converted_country_from_region in country_list:
                    break
                else:
                    print()
                    print(textwrap.fill("That did not work, maybe it's easier to use \
the copy and paste function than typing it out!\n"))
            break
        else:
            print()
            print(textwrap.fill("That did not work, maybe it's easier to use the copy \
and paste function than typing it out!\n"))

    country = converted_country_from_region
    validate_country()

    return


def search_country_by_list():
    """
    Gives the user the option to search a country from the list of all 132
    Countries available.
    """
    global country
    global country_list

    print()
    for value in country_list:
        print(value.title())

    while True:
        country_from_list = input('\nPlease choose one of the countries \
listed above:\n')
        converted_country_from_list = country_from_list.lower()
        if converted_country_from_list in country_list:
            break
        else:
            print()
            print(textwrap.fill("That did not work, maybe it's easier to use the \
copy and paste function than typing it out!\n"))

    country = converted_country_from_list
    validate_country()

    return


def vacation_level():
    """
    Asks for the level of adventure/comfort that the user would like
    To experience and validates the data that the user inserts.
    """
    options = ['a', 'b', 'c', 'd']
    print()
    print(textwrap.fill('***Which level of adventure/comfort do you want to \
experience?'))
    vacation_level_options = """
Please choose a letter from the following options:
a: I'll travel like a backpacker
b: I'll want some comfy hotels and costly food once in a while
c: I'm all luxury
d: I'm fed up with tourism - I want to live there like a local!"""
    print(vacation_level_options)

    while True:
        level = input(
            '\nPlease choose one of the options (a, b, c or d):\n')
        if level not in options:
            print('\nThat did not work, please insert a, b, c or d.')
        else:
            break

    return level


def get_tci(level_input):
    """
    Searches for the country the user entered in the excel worksheet 'TCI',
    Searches for the level of adventure/comfort that the user entered and
    Retrieves the correct Travel-Cost-Index (TCI) for the right country and
    The right level of adventure/comfort.
    """
    global country

    print()
    print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
    print('\n>>> Thank you for your request! I have all the data I need now.')
    time.sleep(1)
    print('\nYour Travel-Cost-Index is being calculated...')
    country_cell = tci.find(country)
    country_row = country_cell.row
    level_cell = tci.find(level_input)
    level_col = level_cell.col
    country_level = tci.cell(country_row, level_col).value
    time.sleep(2)

    return country_level


def get_budget(tci_user, days_input):
    """
    Calculates the budget the user needs to undertake the Travel by
    Multiplying the TCI from the get_tci() function with the number
    Of days the user has available for the travel.
    """
    global country
    print('\nYour Travel-Cost-Index is ready:\n')
    tci_user_round = "{:.2f}".format(round(float(tci_user), 2))
    budget = "{:.2f}".format(round(float(tci_user), 2) * days_input)
    print(textwrap.fill(f'You will need {tci_user_round} € per day as soon as you are in \
{country.title()}. For your travel of {days_input} days you will need a \
budget of {budget} €!'))
    print()
    time.sleep(2)
    print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
    print('\nThank you for using the Travel Cost Calculator!\n')
    time.sleep(1)
    print(textwrap.fill('Remember this is only an estimation based on data from other \
travellers and can vary from individual to individual.'))
    time.sleep(1)
    print()
    print (textwrap.fill('If you want to check out the origin of my database, please \
have a look at those two websites:'))
    print('\nhttps://www.budgetyourtrip.com/africa/rankings')
    print('https://livingcost.org/cost')
    print()

    return


def main():
    """
    Calls all the functions above.
    """
    days_input = vacation_days()
    country_input = vacation_country()
    level_input = vacation_level()
    tci_user = get_tci(level_input)
    get_budget(tci_user, days_input)


print('\nHappy to see you at the Travel Cost Calculator!\n')
print (textwrap.fill('With this calculator you can estimate the budget you will need \
when travelling within a specific country.\n'))
print (textwrap.fill('All I need to know from you is how many days you have available, \
to which country you want to go to and at which level of comfort you \
want to travel.'))
print("\nLet's get started!")
print('-------------------------------------------------')
main()
