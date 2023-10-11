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
    while True:
        print("Please enter the sales data from the last quarter.")
        print("The data should be in order of genre, as follows: Fantasy, Romance, Thriller, Horror, Sci Fi.")
        print("You should input the five numbers separated by a comma only, without any spaces.")
        print("Example: 1,2,3,4,5\n")

        sales_str = input("Please input sales data here: ")
        sales_data = sales_str.split(",")

        if validate_num(sales_data):
            print("Figures entered successfully.")
            break


def validate_num():
    """
    This function will ensure the data entered can be converted into integers, and do so if it is able. Otherwise it will raise a warning.
    """
    try:
        [int(value) for value in values]
        if len(values) != 5:
            raise ValueError(
                print(f"Warning! You have not entered five figures, you have entered {
                      len(values)}")
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please check and try again.\n")
        return False
    return True


def update_worksheet():
    """
    This function will update the worksheet with data input by the user
    """
    print("Worksheet update in progress...")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Worksheet updated.\n")


data = get_sales()
sales_data = [int(num) for num in data]
update_worksheet(sales_data)
