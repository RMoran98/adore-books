# Adore Books
This is a python program which enables the user to enter data and update a google spreadsheet for a fictional publishing house. It enters the data and performs calculations for the user.

## How to Use
- On running the program, the user will be prompted to enter the sales data, consisting of five numbers in order of the book genre. These numbers should be separated by a comma only, with no blank spaces.
- Next the user will be asked to enter the returns data, in the same format as before.
- Both of these operations will check if the data is valid and transform the data from a string into an integer so it can be used in mathematical operations.
- The information will be logged to the spreadsheet before the calculations occur.
- First the program will find the profit for each genre by sorting the two inputted lists into sets, and subtracting the returns values from the sales values. Since the sales and returns figures are the number of books total, the resulting figure is multiplied by 12, which is the cost of a book in euros. This data will then be logged in the spreadsheet.
- Lastly the program will calculate how much is owed in author's royalties, by multiplying the profits figure by 0.15 to get 15% of the total profit. This set of numbers will also be recorded on the spreadsheet.
