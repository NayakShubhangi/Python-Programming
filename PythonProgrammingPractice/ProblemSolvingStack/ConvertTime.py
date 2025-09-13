# Write a Python program to convert time from 12 hour to 24 hour format.
# Solution:-  Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# Note : Midnight is 12:00:00 AM on a 12-hour clock and 00:00:00 on a 24-hour clock.
# Noon is 12:00:00 PM on 12-hour clock and 12:00:00 on 24-hour clock.
# Examples :
# Input : 11:21:30 PM
# Output : 23:21:30

# Input : 12:12:20 AM
# Output : 00:12:20

twelve_hour_time = input("Please enter a time in 12 hour format (hh:mm:ss AM/PM): ").split(":")
am_pm = twelve_hour_time[2][-2:]
twelve_hour = twelve_hour_time[0]
twentyFour_hour = "00"
if twelve_hour == "12" and am_pm == "AM":
    twentyFour_hour = "00"
elif twelve_hour == "12" and am_pm == "PM":
    twentyFour_hour = "12"
else:
    twentyFour_hour = str(int(twelve_hour) + 12)
twentyFour_hour_time = twentyFour_hour+":"+twelve_hour_time[1]+":"+twelve_hour_time[2][:2]
print(twentyFour_hour_time)