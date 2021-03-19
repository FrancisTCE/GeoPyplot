import gmplot
import os
from dataclasses import dataclass


@dataclass
class GeoStat:
    sea_level: float
    lat: str
    long: str


geoStatsArr = []

markers = []

APIKEY = ''

distance12_flat = 0
distance23_flat = 0
distance123_flat = 0

distance12_direct = 0
distance23_direct = 0
distance123_direct = 0


def getScreenWidthPadded(root, pad):
    if (root.winfo_screenwidth() * pad) > 1920:
        return str(int((root.winfo_screenwidth() * pad) / 2))
    return str(int(root.winfo_screenwidth() * pad))


def getScreenHeightPadded(root, pad):
    if (root.winfo_screenheight() * pad) > 1080:
        return str(int((root.winfo_screenheight() * pad) / 2))
    return str(int(root.winfo_screenheight() * pad))


def setAPIKEY():
    global APIKEY
    with open(format(os.getcwd()) + '/APIKEY.GKEY') as f:
        APIKEY = f.readline()


def markGPS_coordinates():
    global geoStatsArr
    geoStatsArr.append(GeoStat(0.0, 'lat1', 'long1'))


def run(p1, p2, p3):
    global APIKEY
    global geoStatsArr
    markers.append(p1)
    markers.append(p2)
    markers.append(p3)
    print('\nWorking with the following coordinates:')
    for x in markers:
        print('\n' + x)
    setAPIKEY()
    print(APIKEY)
    markGPS_coordinates()

    # calculate_distances(p1, p2, p3)
    # calculate_sea_level(p1, p2, p3)
    # directLines_distances(p1, p2, p3)
