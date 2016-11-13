from math import pi
import ephem

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
    'mercury': (1, mer.alt, mer.az, mer.mag),
    'venus': (2, ven.alt, ven.az, ven.mag),
    'mars': (3, mar.alt, mar.az, mar.mag),
    'jupiter': (4, jup.alt, jup.az, jup.mag),
    'saturn': (5, sat.alt, sat.az, sat.mag),
}

# < 135 East light -- 135 to 225 Center Light -- > 225 West light
for p, i in planets.items():
    planet_no, alt, az, mag = i

    if 180 * alt / pi < 5:
        continue # planet is below the horizon

    az_degrees = 180 * az / pi
    if az_degrees <= 135:
        # planet is in the East
        print "Look East for %s" % p

    if az_degrees > 135 and az_degrees < 225:
        # planet is in the South
        print "%s is up high in the South" % p

    if az_degrees >= 135:
        # planet is in the West
        print "Look West for %s" % p
