import math as math

angle = 0
while angle < 360:
    rad = angle * math.pi / 180
    print('angle: ' + str(angle) + ' sin: ' + str(round(math.sin(rad), 4)) + ' cos: ' + str(round(math.cos(rad), 4)))
    angle += 15
