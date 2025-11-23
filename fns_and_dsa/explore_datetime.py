import datetime
def display_current_datetime():
    current_date = datetime.date.today()
    current_time = datetime.datetime.now().time()
    print(f"Current Date and Time: {current_date} {current_time}")  
    timedelta = int(input("Enter number of days to add to the current date: "))
    future_date = current_date + datetime.timedelta(days=timedelta)
    print(f"Future Date: {future_date}")