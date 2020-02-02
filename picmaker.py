import math
import random

def dist(x1,y1,x2,y2):
    return math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))

img = open("pic.ppm","w")
img.write("P3\n 500 500\n 255\n")
arr = [[[111,196,246] for i in range(500)] for i in range(500)]


for bubbles in range(75):
    centerX = random.randint(0,500)
    centerY = random.randint(0,500)
    radius = random.randint(5,25)
    r = random.randint(140,255);
    g = random.randint(200,255);
    b = 255

    for y in range(500):
        for x in range(500):
            if (dist(x,y, centerX, centerY) < radius):
                arr[y][x][0] = r
                arr[y][x][1] = g
                arr[y][x][2] = b

for y in range(500):
    for x in range(500):
        img.write(str(arr[y][x][0]) + " " + str(arr[y][x][1]) + " " + str(arr[y][x][2]) + "\n")

img.close()
