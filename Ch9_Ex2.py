#Name: Bryan Huebner
#Date: 04 November 2014
#Description: Challenge Exercise-2 from chapter 9.
#Script to copy all the rasters in a workspace to a new file geodatabase:
#(using the rasters from Chapter 9 exercises)


#import modules
import arcpy
from arcpy import env

env.workspace = "E:/Python/Data/Exercise09"  #set environmental workspace
env = env.workspace  #create variable for workspace

raster_list = arcpy.ListRasters()  #list available rasters
arcpy.CreatePersonalGDB_management(env + "/Results", "new_rasters.gdb")  #create new geodatbase for rasters

for raster in raster_list:  #set perameters and iterate through raster list
    desc = arcpy.Describe(raster)  #set variable for raster describe function 
    raster_name = desc.baseName  #describe raster properties
    output_raster = env + "/Results/new_rasters.gdb/" + raster_name  #set path for the 'new' output rasters
    arcpy.CopyRaster_management(raster, output_raster)  #copy rasters into new geodatbase
