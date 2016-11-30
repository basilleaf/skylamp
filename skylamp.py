from __future__ import print_function
from math import pi
from time import sleep
from datetime import datetime
import ephem
import serial

# setup serial port where arduino is
debug = False
try:
    ser = serial.Serial('/dev/cu.usbmodem1411', 9600)
except serial.SerialException:
    print("\nNo USB connection, continuing in debug mode... \n")
    debug = True

# match the arduino pin to a planet and direction in sky
pin_codes = {
    ('mercury','E'): 1,
    ('mercury','C'): 2,
    ('mercury','W'): 3,
    ('venus','E'): 4,
    ('venus','C'): 5,
    ('venus','W'): 6,
    ('mars','E'): 7,
    ('mars','C'): 8,
    ('mars','W'): 9,
    ('jupiter','E'): 10,
    ('jupiter','C'): 11,
    ('jupiter','W'): 12,
    ('saturn','E'): 13,
    ('saturn','C'): 14,
    ('saturn','W'): 15
}

d = datetime.utcnow()
current_date_time = d.strftime('%Y/%m/%d %H:%M:00')

# setup pyephem Observer location
location = ephem.Observer()
location.lat = ephem.degrees('37.7749')
location.long = ephem.degrees('-122.4194')
location.date = ephem.Date(current_date_time)

# the 5 naked-eye planets
mer = ephem.Mercury(location)
ven = ephem.Venus(location)
mar = ephem.Mars(location)
jup = ephem.Jupiter(location)
sat = ephem.Saturn(location)

# collect the alt, az, mag of our 5 planets
planets = {
    'mercury': (mer.alt, mer.az, mer.mag),
    'venus': (ven.alt, ven.az, ven.mag),
    'mars': (mar.alt, mar.az, mar.mag),
    'jupiter': (jup.alt, jup.az, jup.mag),
    'saturn': (sat.alt, sat.az, sat.mag),
}

# look for each planet in the sky
for p, i in planets.items():

    alt, az, mag = i

    alt_deg = 180 * alt / pi
    if alt_deg < 5:
        continue  # planet is below the horizon

    az_deg = 180 * az / pi
    if az_deg <= 135:
        # planet is in the East
        direction = "E"

    if az_deg > 135 and az_deg < 225:
        # planet is due South
        direction = "S"

    if az_deg >= 135:
        # planet is in the West
        direction = "W"

    pin = pin_codes[(p, direction)]
    msg = (p, direction, pin)

    if not debug:
        ser.write(str(msg) + ';')  # tell the Arduino which pin to light
    else:
        print(msg)
        print('alt: %s, az: %s, mag: %s' % (str(alt_deg), str(az_deg), str(mag)))
        print()

    del msg
    del direction
