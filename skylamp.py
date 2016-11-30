from __future__ import print_function
from math import pi
from time import sleep
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

current_date_time = "2016/11/30 02:55:00"

# setup pyephem Observer location
location = ephem.Observer()
location.lat = ephem.degrees('37.7749')
location.long = ephem.degrees('-122.4194')
location.date = ephem.Date(current_date_time)

mer = ephem.Mercury(location)
ven = ephem.Venus(location)
mar = ephem.Mars(location)
jup = ephem.Jupiter(location)
sat = ephem.Saturn(location)

mar.compute(location)
print(mar.alt, mar.az, mar.mag)

# Azimuth in pyephome starts from North and runs clockwise
planets = {
    'mercury': (mer.alt, mer.az, mer.mag),
    'venus': (ven.alt, ven.az, ven.mag),
    'mars': (mar.alt, mar.az, mar.mag),
    'jupiter': (jup.alt, jup.az, jup.mag),
    'saturn': (sat.alt, sat.az, sat.mag),
}

# < 135 East light -- 135 to 225 Center Light -- > 225 West light
for p, i in planets.items():

    alt, az, mag = i

    alt_deg = 180 * alt / pi
    if alt_deg < 5:
        continue # planet is below the horizon

    az_deg = 180 * az / pi
    if az_deg <= 135:
        # planet is in the East
        direction = "E"

    if az_deg > 135 and az_deg < 225:
        # planet is in the South
        direction = "S"

    if az_deg >= 135:
        # planet is in the West
        direction = "W"

    # if direction:
    pin = pin_codes[(p, direction)]
    msg = (p, direction, pin)
    if debug:
        print(msg)
        print('alt: %s, az: %s, mag: %s' % (str(alt_deg), str(az_deg), str(mag)))
        print()
    if not debug:
        ser.write(str(msg) + ';')

    del msg
    del direction
