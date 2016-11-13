import ephem

kpno = ephem.Observer()

kpno.long = ephem.degrees("-7.44111")
kpno.lat = ephem.degrees("31.9533")
kpno.elevation = 1925.0 + 700.0
kpno.date = "2010/1/1"

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
