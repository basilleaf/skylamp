import ephem

kpno = ephem.Observer()

kpno.long = ephem.degrees("122.4194")
kpno.lat = ephem.degrees("37.7749")
kpno.date = "2016/11/12 19:50:300"

jupiter = ephem.Jupiter(kpno)
saturn = ephem.Saturn(kpno)
mercury = ephem.Mercury(kpno)
venus = ephem.Venus(kpno)
mars = ephem.Mars(kpno)

print jupiter.alt, jupiter.az
print saturn.alt, saturn.az
print mercury.alt, mercury.az
print venus.alt, venus.az
print mars.alt, mars.az
