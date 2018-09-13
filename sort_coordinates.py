import math
import json

with open('coordinates.json') as json_data:
    points = json.load(json_data)

def calculateDistance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist

def func():
    try:
        x_origin = int(raw_input("Enter x coordinate of origin : "))
        y_origin = int(raw_input("Enter y coordinate of origin : "))

        dist  = {}

        for point in points:
            dist.update({point["value"] : calculateDistance(x_origin,y_origin,int((point["value"]).split(",")[0]),int((point["value"]).split(",")[1]))})

        for key, value in sorted(dist.iteritems(), key=lambda (k,v): (v,k)):
             print "("+ key + ")"
    except:
        print "Wrong input"
        func()

if __name__ == '__main__':
    func()