# GeoPyplot

GeoPyplot is a python geo elevation tool using open elevation api. This tool maps the elevation between points and saves this data to an excel file and 2 graphs per pair of points one in .png and another in .svg at 1200 dpi

# requires python 3.8

pip install matplotlib xlsxwriter

# cmd to run: python3 GeoPyplot.py

# Instructions:
the file with gps coordenates can take up to 3 gps points
Terminal to folder

1) You will be prompted for the file name with the gps coord, these "file.gps" needs to be in the same folder as GeoPyplot.py
2) Enter number of samples of data you need between the points
3) Enter a new folder name to save the excel.xlsx file with data and elevation graphs.png /.svg
4) press enter 

# File type:
# "example.gps" 
contains format: "lat1, long1:lat2, long2" such as "39.014095, -9.322054:38.947374, -9.304201"
