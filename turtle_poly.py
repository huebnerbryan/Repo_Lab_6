#Name: Bryan Huebner
#Date: 03 November 2014
#Description: Script using "turtle" to draw a polygon for Arc
#report the points of the polygon and create a new feature class in ArcMap
#Save the polygon as "turtle_poly.shp"
#Use "WGS1984" as the spatial reference


#import modules
import arcpy
import fileinput
import string
#import Turtle Graphics - use wildcard
from turtle import *

arcpy.env.workspace = 'G:/GIS_501/Labs/Lab_6/Python_Scripts'
env = arcpy.env.workspace
arcpy.env.overwriteOutput = True

#set projection, feature class, and spatial reference
out_path = "G:/GIS_501/Labs/Lab_6/Python_Scripts/results"
fc = "turtle_poly.shp"
prj_file = "G:/GIS_501/Labs/Lab_6/Data/WGS_1984.prj"
spatial_ref = arcpy.SpatialReference('prj_file')


#statement telling the 'user' what to expect
print ("This program draws equal-sided polygons based on the number you select.")        

#prompt 'user' to select an integer
sides = int(raw_input("Select the number of sides for the polygon you wish to draw: "))

#prompt 'user' to choose the length of the polygon sides
length = int(raw_input("How long do you wish the sides of your polygon to be?: "))

turtle = Pen()                                  #identify pen
turtle.shape('turtle')                          #select the drawing symbol (turtle shape)
turtle.speed('slow')                            #set turtle speed
turtle.screen.bgcolor('#160912')                #set screen background color
turtle.color('#00D143')                         #set turtle/pen color

xy = []                                         #point coordinate list

for i in range(sides):                          #generate polygon based on integer selected
    x = turtle.xcor()
    y = turtle.ycor()
    xy.append(str(i)+ ',' + str(x)+','+str(y))
    turtle.forward(length)
    turtle.left(360/sides)

arcpy.management.CreateFeatureClass('out_path', 'fc', "POLYGON", '', '', '', 'spatial_ref')

#set cursor, array, and point
cursor = arcpy.da.InsertCursor(fc, ["SHAPES@"])
array = arcpy.Array()
point = arcpy.Point()

for cord in xy:                                  #return polygon vertices as point coordinates
    print cord
    point.ID, point.X, point.Y = cord.split(',')
    array.add(point)
polygon = arcpy.Polygon(array)
cursor.insertRow([polygon])
del cursor






