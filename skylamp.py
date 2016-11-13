import ephem

location = ephem.Observer()

location.long = ephem.degrees("-122.4194")
location.lat = ephem.degrees("37.7749")
location.date = "2016/11/12 17:00:300"

jupiter = ephem.Jupiter(location)
saturn = ephem.Saturn(location)
mercury = ephem.Mercury(location)
venus = ephem.Venus(location)
mars = ephem.Mars(location)

# Azimuth usually starts from North
print jupiter.alt, jupiter.az, jupiter.mag
print saturn.alt, saturn.az, saturn.mag
print mercury.alt, mercury.az, mercury.mag
print venus.alt, venus.az, venus.mag
print mars.alt, mars.az, mars.mag
