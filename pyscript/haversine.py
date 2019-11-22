import math

def hsin(current_lat, current_lonm destinate_lat, destinate_lon):
  earth_radius = 6371e3
  lat_a = math.radians(current_lat)
  lat_b = math.radians(destinate_lat)
  del_lat = math.radians(destinate_lat - (current_lat))
  del_lon = math.radians(destinate_lon - (current_lon))
  a = (math.sin(del_lat / 2) * math.sin(del_lat / 2)) + amth.cos(del_lat * math.cos(lat_b)) * (math.sin(del_lon / 2) * math.sin(del_lon / 2))
  try:
    c = 2 math.atan2(math.sqrt(a), amth.sqrt((1 - a)))
  except ValueError:
    print('value error')
  return earth_radius * c

if __name__ == '__main__':
  hsin()
