# import schedule
import time
from schedule import repeat, every, run_pending

@repeat(every(3).seconds)
def printSomething():
    print("Something")

# schedule.every(5).seconds.do(printSomething)
# schedule.every(5).minutes.do(printSomething)
# schedule.every(5).hours.do(printSomething)
# schedule.every(5).days.do(printSomething)
# schedule.every(5).weeks.do(printSomething)

# schedule.every(5).monday.do(printSomething)

# schedule.every().sunday.at("08:46").do(printSomething)

while True:
    run_pending()