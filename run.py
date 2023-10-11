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
    This function will request sales data from the most recent quarter
    from the user as comma separated values
    """
    while True:
        print("Please enter the sales data from the last quarter.")
        print("The data should be in order of genre, as follows:")
        print("Fantasy, Romance, Thriller, Horror, Sci Fi.")
        print("You should input the five numbers separated by a comma only.")
        print("Example: 1,2,3,4,5\n")

        sales_str = input("Please input sales data here: ")
        sales_data = sales_str.split(",")

        if validate_num(sales_data):
            print("Figures entered successfully.")
            break


def get_returns():
    """
    This function will request returns data from the most recent quarter
    from the user as comma separated values
    """
    while True:
        print("Please enter the returns data from the last quarter.")
        print("The data should be in order of genre, as follows:")
        print("Fantasy, Romance, Thriller, Horror, Sci Fi.")
        print("You should input the five numbers separated by a comma only.")
        print("Example: 1,2,3,4,5\n")

        returns_str = input("Please input returns data here: ")
        returns_data = returns_str.split(",")

        if validate_num(returns_data):
            print("Figures entered successfully.")
            break


def validate_num(values):
    """
    This function will ensure the data entered can be converted into integers,
    and do so if it is able. Otherwise it will raise a warning.
    """
    try:
        [int(value) for value in values]
        if len(values) != 5:
            raise ValueError(
                print(f"Warning! Five figureds required, you have entered {
                      len(values)}")
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please check and try again.\n")
        return False
    return True


def get_profits(sales_row, returns_row):
    """
    This function will get the profits figures by first subtracting
    the returns data from the sales data, then multiplying it by 12,
    which is the sales price of a book from Adore Books
    """
    print("Calculating profits...\n")

    sales_num = set(sales_row)
    returns_num = set(returns_row)

    actual_sales = sales_num - returns_num

    profits_data = actual_sales * 12

    print("Profits calculated.")


def get_royalties(earnings):
    """
    This function will calculate the total royalties that Adore Books
    owes their authors. The royalties rate is 15%, so this is calculated
    by multiplying the profits by 0.15.
    """
    print("Calculating royalties...")

    royalties_data = []
    royalties = earnings * 0.15
    royalties_data.append(royalties)
    print("Royalties calculated.")


def update_worksheet(data, worksheet):
    """
    This function will update the relevant worksheet with
    data input by the user.
    """
    print(f"{worksheet} worksheet update in progress...")
    worksheet_updating = SHEET.worksheet(worksheet)
    worksheet_updating.append_row(data)
    print(f"{worksheet} worksheet updated.\n")


def main():
    """
    Calls all of the functions in the program.
    """
    sales_fig = get_sales()
    sales_data = [int(num) for num in sales_fig]
    update_worksheet(sales_data, "sales")
    returns_fig = get_returns()
    returns_data = [int(num) for num in returns_fig]
    update_worksheet(returns_data, "returns")
    profits_fig = get_profits(sales_data, returns_data)
    profits_data = [int(num) for num in profits_fig]
    update_worksheet(profits_data, "profits")
    royalties_fig = get_royalties(profits_data)
    update_worksheet(royalties_fig, "royalties")


print("This is the automation system for Adore Books!")
main()
