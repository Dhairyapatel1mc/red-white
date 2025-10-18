import datetime
import time

def current_datetime():
    """Display current date and time"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def date_difference(date1, date2):
    """Calculate difference between two dates (YYYY-MM-DD)"""
    d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def custom_format():
    """Format current date into custom formats"""
    now = datetime.datetime.now()
    return now.strftime("%A, %d %B %Y")

def stopwatch():
    """Simple stopwatch"""
    input("Press Enter to start the stopwatch...")
    start = time.time()
    input("Press Enter to stop...")
    end = time.time()
    return round(end - start, 2)

def countdown(seconds):
    """Countdown timer"""
    for i in range(seconds, 0, -1):
        print(i, end=" ", flush=True)
        time.sleep(1)
    print("\nTime's up!")
