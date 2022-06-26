# This app give take a birth date and return all age details 

# import date model
from datetime import date, timedelta
def cal_age(birth_date):
    today = date.today()
    year = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day)) 
    months = 'Unsolved'
    days = 'Unsolved'
    return year, months, days

my_birth_date = date(1995, 12, 31)
today = date.today()

# print(cal_age(my_birth_date))

welcome_msg = '''
        WELCOME TO AGE CALCULATOR
    Please enter your birth date in this formate
                "dd-mm-yyyy"
'''

print(welcome_msg)
while True:
    user_date = input('Birth date (dd-mm-yyyy): ')
    try:
        user_date.strip()
        bod_day, bod_month, bod_year = map(int, user_date.split('-'))
        bod = date(bod_year, bod_month, bod_day)
    except:
        print('\n\nInlaid Date', 'Please Try Again!', sep='\n')
        print('\n')
        continue
    years, months, days = cal_age(bod)
    print(f'Your age is: {years} years, {months} months and {days} day')
    print('\n\n\nThank You for using our app!\n\n\n')
    user_input = input('Press "t" to start with another date\n or press any key to exit')
    if user_input == 't':
        continue
    break
