#Name: Bryan Huebner
#Date: 04 November 2014
#Description: Challenge Exercise-1 from chapter 9.
#Script for determining area that meets certain conditions:
#Moderate slope--between 5 and 20 degrees
#Southerly aspect--between 150 and 270 degrees
#Forested--land cover types of 41, 42, 0r 43


#import modules
import arcpy
from arcpy import env
from arcpy.sa import *  #use 'wilcard' to import "ALL" of the spatial analyst module

env.workspace = "E:/Python/Data/Exercise09" #set environmental workspace
env = env.workspace  #create variable for workspace

if arcpy.CheckExtension("Spatial") == "Available":  #verify license is available
    arcpy.CheckOutExtension("Spatial")  #obtain license
    elevation = arcpy.Raster("elevation")  #set variable for raster
    land_cover = arcpy.Raster("landcover.tif")
    slope = Slope(elevation)  #set slope and aspect to the elevation
    aspect = Aspect(elevation)
    goodslope = ((slope > 5) & (slope < 20))  #convert slope values
    goodaspect = ((aspect > 150) & (aspect < 270))  #convert aspect values
    goodland = ((lc == 41) | (lc == 42) | (lc ==43))  #convert goodland values
    outraster = (goodslope & goodaspect & goodland)  #set the output raster variable
    outraster.save("E:/Python/Data/Exercise09/Results/final")  #save the raster to make it permanent
    arcpy.CheckInExtension("Spatial")  #return licences to manager
