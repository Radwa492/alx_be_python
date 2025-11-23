import datetime

def display_current_datetime():
    # Part 1: Display current date and time
    current_date = datetime.datetime.now()   # stores both date & time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date):
    # Part 2: Calculate future date
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + datetime.timedelta(days=days_to_add)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")
    return future_date
# Run program
current_date = display_current_datetime()
calculate_future_date(current_date)