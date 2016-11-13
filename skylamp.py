from math import pi
from time import sleep
import ephem
import serial

# setup serial port where arduino is
ser = serial.Serial('/dev/cu.usbmodem1411', 9600)

# Azimuth usually starts from North
planets = {
    'mercury': (mer.alt, mer.az, mer.mag),
    'venus': (ven.alt, ven.az, ven.mag),
    'mars': (mar.alt, mar.az, mar.mag),
    'jupiter': (jup.alt, jup.az, jup.mag),
    'saturn': (sat.alt, sat.az, sat.mag),
}

# nastyh hacker
pin_code = {
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

demo_dates = ["2016/12/11 03:40:300", "2016/01/01 04:00:000", "2016/01/21 04:00:000", "2016/19/8 11:00:000"]  # must be GMT
while True:
    for d in demo_dates:

        # setup pyephem Observer location
        location = ephem.Observer()
        location.lat = ephem.degrees(37.7749)
        location.long = ephem.degrees(-122.4194)

        mer = ephem.Mercury(location)
        ven = ephem.Venus(location)
        mar = ephem.Mars(location)
        jup = ephem.Jupiter(location)
        sat = ephem.Saturn(location)
        location.date = d[0]

        print "checking date: %s" % d

        # < 135 East light -- 135 to 225 Center Light -- > 225 West light
        for p, i in planets.items():

            alt, az, mag = i

            print p, 180 * az / pi

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

            msg = pin_code[p, direction]
            print p, direction, msg
            ser.write(str(msg) + ';')

        sleep(5)
