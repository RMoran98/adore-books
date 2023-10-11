import gspread
from google.oauth2.service_account import Credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('adore_books')


def get_sales():
    """
    This function will request sales data from the most recent quarter from the user as comma separated values
    """
    print("Please enter the sales data from the last quarter.")
    print("The data should be in order of genre, as follows: Fantasy, Romance, Thriller, Horror, Sci Fi.")
    print("You should input the five numbers separated by a comma only, without any spaces.")
    print("Example: 1,2,3,4,5\n")

    sales_str = input("Please input sales data here: ")
