import cv2
import numpy as np
import pandas as pd
import openpyxl as opxl
import matplotlib.pyplot as plt
import matplotlib as mpl

# read an excel file with the coords of a sample polygon
xlsx_file_dataframe = pd.read_excel("coords_test_polygon.xlsx")
list_polygon_x_coords = np.array(xlsx_file_dataframe["x"].to_list())
list_polygon_y_coords = np.array(xlsx_file_dataframe["y"].to_list())

# normalize them by subtracting the minimal coordinates i.e. translating them close to
# the origin of the coordinate system (i.e. make the coordinates relative)
norm_list_polygon_x_coords = list_polygon_x_coords - np.min(list_polygon_x_coords)
norm_list_polygon_y_coords = list_polygon_y_coords - np.min(list_polygon_y_coords)

# combine them to x-y pairs
x_y_pairs_polygon = [(x, y) for (x, y) in zip(norm_list_polygon_x_coords, norm_list_polygon_y_coords)]

print(x_y_pairs_polygon)


def round_to_nearest_half_int(num):
    return round(num * 2) / 2

height = 7.2

height_rounded = round_to_nearest_half_int(height)

df_distances = pd.read_excel("luminaires_grid_distances.xlsx")

flag_high_room = height_rounded >= 6

if flag_high_room:
    wall_distance = df_distances["dist_w_l"].loc[df_distances["height_l"] == height_rounded].to_list()[0]
    grid_distance = df_distances["dist_g_l"].loc[df_distances["height_l"] == height_rounded].to_list()[0]
else:
    wall_distance = df_distances["dist_wall"].loc[df_distances["height"] == height_rounded].to_list()[0]
    grid_distance = df_distances["dist_grid"].loc[df_distances["height"] == height_rounded].to_list()[0]

# get the bounding box of a room by finding max x and y coords of room polygon
xmax = max(norm_list_polygon_x_coords)
ymax = max(norm_list_polygon_y_coords)





