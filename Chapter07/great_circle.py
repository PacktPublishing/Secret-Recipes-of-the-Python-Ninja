from math import cos, sin, atan2, fabs, sqrt, pow, radians

r = 6371 # Earth's radius at equator in kilometers

# Alamo
lat1 = 29.42569
lat1_rads = radians(lat1)
long1 = -98.48503
long1_rads = radians(long1)

# Tokyo Tower
lat2 = 35.65857
lat2_rads = radians(lat2)
long2 = 139.745484
long2_rads = radians(long2)

delta = fabs(long1_rads - long2_rads)

def great_circle(lat1_rads, lat2_rads, delta):
    x = (sin(lat1_rads) * sin(lat2_rads)) + (cos(lat1_rads) * cos(lat2_rads) * cos(delta))
    y = sqrt(pow((cos(lat2_rads) * sin(delta)), 2)
         + pow((cos(lat1_rads) * sin(lat2_rads)) - (sin(lat1_rads) * cos(lat2_rads) * cos(delta)), 2))

    angle = atan2(y, x)

    dist = r * angle

    return dist

num = 100000000
for i in range(num):
    great_circle(lat1_rads, lat2_rads, delta)
