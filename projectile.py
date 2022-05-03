from math import pi, tan, cos
#square the acceleration
acceleration = float(9.81)

barrel_height = 1

horizontal_distance_travelled = 0.5

elevation = 80
elevation_converted = elevation * (pi / 180)
print(elevation_converted)

initial_velocity = 44

answer = barrel_height + (horizontal_distance_travelled * tan(elevation_converted)) - ((acceleration * horizontal_distance_travelled) / 2 * (initial_velocity * cos(elevation_converted)))
print(answer)