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

current_date_time = "2016/11/30 01:50:00"

# setup pyephem Observer location
location = ephem.Observer()
location.lat = ephem.degrees(37.7749)
location.long = ephem.degrees(-122.4194)

mer = ephem.Mercury(location)
ven = ephem.Venus(location)
mar = ephem.Mars(location)
jup = ephem.Jupiter(location)
sat = ephem.Saturn(location)
location.date = current_date_time

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

    if 180 * alt / pi < 5:
        continue # planet is below the horizon

    az_degrees = 180 * az / pi
    if az_degrees <= 135:
        # planet is in the East
        direction = "E"

    if az_degrees > 135 and az_degrees < 225:
        # planet is in the South
        direction = "S"

    if az_degrees >= 135:
        # planet is in the West
        direction = "W"

    # if direction:
    msg = pin_codes[(p, direction)]
    print(p, direction, msg)

    msg = str(msg) + ';'
    print(msg)
    if not debug:
        ser.write(str(msg) + ';')

    del msg
    del direction
