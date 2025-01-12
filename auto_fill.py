from os import times
import keyboard
import time

attendees_filename = "verified_attendees.txt"
attendees = set(line.strip() for line in open(attendees_filename))

# five second delay than autotype
time.sleep(5)

for attendee in attendees:
    keyboard.write(attendee)
    keyboard.press_and_release('enter')

    time.sleep(1)

keyboard.write('klar.')