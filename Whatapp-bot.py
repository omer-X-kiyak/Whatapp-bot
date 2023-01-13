import datetime
import pywhatkit

# Read the data from the file
with open("contacts.txt", "r") as f:
    lines = f.readlines()

# Parse the data
contacts = []
for line in lines:
    name, number, dob = line.strip().split(",")
    dob = datetime.datetime.strptime(dob, "%d/%m/%Y").date()
    contacts.append((name, number, dob))

# Check if it's someone's birthday today
today = datetime.date.today()
for name, number, dob in contacts:
    if dob == today:
        # Send a birthday message
        pywhatkit.sendwhatmsg(number, 0, 0, f"Happy birthday, {name}!")
