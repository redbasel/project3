# we need gspread in order to access the sheet.
# pprint is to better present the tables to the users
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint as pp
# the scope says which apis can be utilized
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
# pointing python to which sheet file we want to access.
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('p3clients')

# this functon fetches and manipulates the values from the selected client to be used with the tools i.e. our functions
def to_be_utilized():
    try:
        select_worksheet = input('write the name of the client record you wish to access:\n')
        terminal_chosen_worksheet = SHEET.worksheet(select_worksheet)
        chosen_ws_all_values = terminal_chosen_worksheet.get_all_values()
        header_row = chosen_ws_all_values[0]
        start_row = chosen_ws_all_values[1]
        last_row = chosen_ws_all_values[-1]
        start_weight_test = terminal_chosen_worksheet.cell(2, 1)
        weight_start_value = int(chosen_ws_all_values[1][0])
        weight_final_value = int(chosen_ws_all_values[-1][0])
        height_value = int(chosen_ws_all_values[-1][-2])
        start_bmi = (((weight_start_value) / ((height_value) * (height_value))) * 10000)
        final_bmi = (((weight_final_value) / ((height_value) * (height_value))) * 10000)
        percentage_change_test_bmi = int(((int(final_bmi)) - (int(start_bmi)))/(int(start_bmi)) * 100)
    except:
        print("There was a error fetching the data from the google sheet. Please check that the sheet is avaialble and the creds are correct.")
    return select_worksheet, terminal_chosen_worksheet, chosen_ws_all_values, header_row, start_row, last_row, start_weight_test, weight_final_value, height_value, start_bmi, final_bmi, percentage_change_test_bmi


#for loop that calculates the percentage change in the clients health data over time, comparing the first measurement with the last. 
def health_measurements():
    select_worksheet, terminal_chosen_worksheet, chosen_ws_all_values, header_row, start_row, last_row, start_weight_test, weight_final_value, height_value, start_bmi, final_bmi, percentage_change_test_bmi = to_be_utilized()
    for x in range(4):
        percentage_change_test = int(((int(last_row[x])) - (int(start_row[x])))/(int(start_row[x])) * 100)
        header_row_x = header_row[x]
        print(f"the percentage change in {header_row_x} is {percentage_change_test}%")

# nre funciton cehck einrval and make the variable equal something, then at the end of the function have the print statement within an f ""....
# this function calcualtes the bmi of the client. firstly their initial bmi value and secondly their final bmi vlaue. and it outputs to the client in which bmi range they were and which they are presently in.
def bmi_check():
    select_worksheet, terminal_chosen_worksheet, chosen_ws_all_values, header_row, start_row, last_row, start_weight_test, weight_final_value, height_value, start_bmi, final_bmi, percentage_change_test_bmi = to_be_utilized()
    if 18.5 > start_bmi:
        #print (f"{select_worksheet} were in the underweight range")
        bmi_interval_past = "underweight" 
        if 18.5 > final_bmi:
            #print (f"{select_worksheet} is now in the underweight range")
            bmi_interval_present = "underweight" 
        elif 18.5 <= final_bmi <= 24.9:
            #print(f"{select_worksheet} is now in the healthy weight range")
            bmi_interval_present = "healthy"
        elif 25 <= final_bmi <= 29.9:
            #print(f"{select_worksheet} is now in the overweight range")
            bmi_interval_present = "overweight"
        elif 30 <= final_bmi <= 39.9:
            #print(f"{select_worksheet} is now in the obese range")
            bmi_interval_present = "obese"
        else:
            #print(f"{select_worksheet} should see a physician")
            bmi_interval_present = "beyond obese"
    elif 18.5 <= start_bmi <= 24.9:
        #print(f"{select_worksheet} were in the healthy weight range")
        bmi_interval_past = "healthy" 
        if 18.5 > final_bmi:
            #print (f"{select_worksheet} is now in the underweight range")
            bmi_interval_present = "underweight"
        elif 18.5 <= final_bmi <= 24.9:
            #print(f"{select_worksheet} is now in the healthy weight range")
            bmi_interval_present = "healthy"
        elif 25 <= final_bmi <= 29.9:
            #print(f"{select_worksheet} is now in the overweight range")
            bmi_interval_present = "overweight"
        elif 30 <= final_bmi <= 39.9:
            #print(f"{select_worksheet} is now in the obese range")
            bmi_interval_present = "obese"
        else:
            #print(f"{select_worksheet} should see a physician")
            bmi_interval_present = "beyond obese"
    elif 25 <= start_bmi <= 29.9:
        #print(f"{select_worksheet} were in the overweight range")
        bmi_interval_past = "overweight"
        if 18.5 > final_bmi:
            #print (f"{select_worksheet} is now in the underweight range")
            bmi_interval_present = "underweight"
        elif 18.5 <= final_bmi <= 24.9:
            #print(f"{select_worksheet} is now in the healthy weight range")
            bmi_interval_present = "healthy"
        elif 25 <= final_bmi <= 29.9:
            #print(f"{select_worksheet} is now in the overweight range")
            bmi_interval_present = "overweight"
        elif 30 <= final_bmi <= 39.9:
            #print(f"{select_worksheet} is now in the obese range")
            bmi_interval_present = "obese"
        else:
            #print(f"{select_worksheet} should see a physician")
            bmi_interval_present = "beyond obese"
    elif 30 <= start_bmi <= 39.9:
        #print(f"{select_worksheet} were in the obese range")
        bmi_interval_past = "obese"
        if 18.5 > final_bmi:
            #print (f"{select_worksheet} is now in the underweight range")
            bmi_interval_present = "underweight"
        elif 18.5 <= final_bmi <= 24.9:
            #print(f"{select_worksheet} is now in the healthy weight range")
            bmi_interval_present = "healthy"
        elif 25 <= final_bmi <= 29.9:
            #print(f"{select_worksheet} is now in the overweight range")
            bmi_interval_present = "overweight"
        elif 30 <= final_bmi <= 39.9:
            #print(f"{select_worksheet} is now in the obese range")
            bmi_interval_present = "obese"
        else:
            #print(f"{select_worksheet} should see a physician")
            bmi_interval_present = "beyond obese"
    else:
        #print(f"{select_worksheet} should've seen a physician")
        bmi_interval_past = "beyond obese"
    print(f"{select_worksheet} was in the {bmi_interval_past} range, \nnow she is in the {bmi_interval_present} range")

# this function prints the table of the client which the first row filled with the titles 
def allDataClient():
    select_worksheet, terminal_chosen_worksheet, chosen_ws_all_values, header_row, start_row, last_row, start_weight_test, weight_final_value, height_value, start_bmi, final_bmi, percentage_change_test_bmi = to_be_utilized()
    pp(chosen_ws_all_values)

# this is the menu that the user will interact with initially and then return to again to continue using the other functions available. 
def toolMenu():
    print("\nWelcome to the tool menu, these tools are at your disposal")
    print("1: Analyze the clients percentage change of their body measurements")
    print("2: Analyze the clients past and present BMI data")
    print("3: Show all the data avaialable")
    print('available clients:')
    worksheet_list = SHEET.worksheets()
    ws_names = ','.join(str(v) for v in worksheet_list)
    try:
        for sheet in worksheet_list:
            print(sheet.title)
        selection = int(input("Please enter your selection, between 1-3:\n"))
        if selection==1:
            health_measurements()
            runAgain()
        elif selection==2:
            bmi_check()
            runAgain()
        elif selection==3:
            allDataClient()
            runAgain()
        else:
            print("invalid choice. enter between 1-3")
            toolMenu()
    except ValueError:
        print("You did not enter a valid number selection, make sure its an integer")
        runAgain()
# this function main task is once tooMenu finishes, ask if the user is finished or wish to utilize the menu once more
def runAgain():
    answer = input('Do you wish to continue using the program, type "yes" in that case otherwise "no"')
    if answer== 'yes':
        toolMenu()
    elif answer == 'no':
        print('Thank you for using the tool, hopefully it could assist you')
    else:
        print('Invalid input, please type again "yes" or "no"')
        runAgain()

def main():
    toolMenu()

main()