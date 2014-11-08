#Name: Bryan Huebner
#Date: 04 November 2014
#Description: Challenge Exercise-1 from chapter 10.
#Using ArcPy mapping module - script that adds the 'parks' layer (from Challenge Exercise 10 dat file)
#from the 'Parks' data frame in 'Austin_TX.mxd' to the other 2 existing data frames
#in the same map document


#import modules
import arcpy
from arcpy import env

env.workspace = "E:/Python/Data/Exercise10"  #set environmental workspace

Austin_mxd = arcpy.mapping.MapDocument("E:/Python/Data/Exercise10/Austin_TX.mxd")  #open the map document
data_frame = arcpy.mapping.ListDataFrames(Austin_mxd, "Parks")[0]  #list of dataframes in the map document with index of '0'
layer = arcpy.mapping.ListLayers(Austin_mxd, "parks", data_frame)[0]  #access the layers in dataframe with index of '0'

data_frame_list = arcpy.mapping.ListDataFrames(Austin_mxd)  #list dataframe
for d_frame in data_frame_list:  #iterate dataframe list
    if d_frame.name == "Parks":  #identify 'Parks' in dataframe
        arcpy.mapping.AddLayer(d_frame, layer)  #if 'Parks' is there then add layer

Austin_mxd.save()  #save map document

