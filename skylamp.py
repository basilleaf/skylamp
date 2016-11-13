from math import pi
import ephem
import serial

# setup serial port where arduino is
ser = serial.Serial('/dev/cu.usbmodem1421', 9600)

# setup pyephem Observer location and date/time
location = ephem.Observer()
location.lat = ephem.degrees("37.7749")
location.long = ephem.degrees("-122.4194")
location.date = "2016/12/11 03:40:300"  # must be GMT

mer = ephem.Mercury(location)
ven = ephem.Venus(location)
mar = ephem.Mars(location)
jup = ephem.Jupiter(location)
sat = ephem.Saturn(location)

# Azimuth usually starts from North
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

    msg = "%s %s" % (p, direction )
    ser.write(msg)
