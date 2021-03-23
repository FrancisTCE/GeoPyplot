import urllib.request
# pip install json
import json
import math
import matplotlib.pyplot as plt
import sys
# pip install xlsxwriter
import xlsxwriter
import os
import time
import threading

workbook = NotImplemented
filename = NotImplemented
samples = NotImplemented
excel_filename = NotImplemented
save_excel = NotImplemented
done = False
rerun = False
finished = False
dir_path = NotImplemented
default_path = NotImplemented
working = NotImplemented


def query():
    global default_path
    global filename
    global samples
    global excel_filename
    global save_excel
    global done
    global rerun
    global finished
    global dir_path
    done = False
    rerun = False
    finished = False
    default_path = os.getcwd()
    printBanner()
    filename = selectFile()
    samples = input('Number of samples between towers: ')
    # save_excel = input('Export data to an excel?[yes][no] ')
    save_excel = 'yes'
    if save_excel == 'yes' or save_excel == 'y':
        folderName()

    geep(0, 1)


def printBanner():
    print('\n============================================================')
    print("   _____               _____                _         _   ")
    print("  / ____|             |  __ \              | |       | |  ")
    print(" | |  __   ___   ___  | |__) |_   _  _ __  | |  ___  | |_ ")
    print(" | | |_ | / _ \ / _ \ |  ___/| | | || '_ \ | | / _ \ | __|")
    print(" | |__| ||  __/| (_) || |    | |_| || |_) || || (_) || |_ ")
    print("  \_____| \___| \___/ |_|     \__, || .__/ |_| \___/  \__|")
    print("                               __/ || |                   ")
    print("                              |___/ |_|                   ")
    print('                       An Geo Elevation Mapping Python Tool')
    print('                      Developed by Francisco Ferreira ISCTE')
    print('============================================================'
          '\n API: Open Elevation \n GeoDose Method: SRTM DEM'
          '\n============================================================\n')


def selectFile():
    print('\nAvailable gps files:')
    arr = os.listdir(os.getcwd())
    for x in arr:
        if x.__contains__('.gps'):
            print('\n   ' + str(x))
    filename_ = input('\nName of file with Towers coordinates: ')
    return filename_


def checkRerun():
    global dir_path
    print('\nDone')
    redo = input('\nRun again?[yes]{no]: ')
    if redo == 'yes' or redo == 'y':
        os.chdir('..')
        query()
    else:
        exit()


def workingBar():
    global working
    # Initial call to print 0% progress
    printProgressBar(0, 100, prefix='Progress:', suffix='', length=50)
    i = 0
    while working:
        # Do stuff...
        time.sleep(0.5)
        # Update Progress Bar
        i = i + 1
        if i == 100:
            i = 0
        printProgressBar(i + 1, 100, prefix='Progress:', suffix='', length=50)


# Print iterations progress
def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


def folderName():
    global default_path
    global dir_path
    global excel_filename
    excel_filename = input('Folder name to save data: ')
    dir_path = os.path.dirname(os.path.realpath(__file__))
    default_path = dir_path
    try:
        os.mkdir(dir_path + '/' + excel_filename)
        os.chdir(dir_path + '/' + excel_filename)
    except FileExistsError:
        print('\nFolder already exists select another name to avoid overwrite.')
        folderName()


def geep(n1, n2):
    global filename
    global done
    global save_excel
    global excel_filename
    global workbook
    global rerun
    global finished
    global working

    with open(os.path.join(default_path, filename)) as f:
        towers = f.readline()
    tower_list = towers.split(':')
    if n1 == 0 and not rerun:
        print('\nFound ' + str(len(tower_list)) + ' towers.')

    s = int(samples)

    points_list = [tower_list[n1].split(', '), tower_list[n2].split(', ')]

    # START-END POINT
    p1 = points_list[0]
    p2 = points_list[1]
    p2[1] = p2[1].rstrip('\n')

    print('\nChecking: ' + '\nTower ' + str(n1 + 1) + ' ' + str(p1)
          + '\nTower ' + str(n2 + 1) + ' ' + str(p2) + '\nAt ' + str(s) + ' samples')

    # NUMBER OF POINTS
    interval_lat = (float(p2[0]) - float(p1[0])) / s  # interval for latitude
    interval_lon = (float(p2[1]) - float(p1[1])) / s  # interval for longitude

    # SET A NEW VARIABLE FOR START POINT
    lat0 = float(p1[0])
    lon0 = float(p1[1])

    # LATITUDE AND LONGITUDE LIST
    lat_list = [lat0]
    lon_list = [lon0]

    # GENERATING POINTS
    for i in range(s):
        lat_step = lat0 + interval_lat
        lon_step = lon0 + interval_lon
        lon0 = lon_step
        lat0 = lat_step
        lat_list.append(lat_step)
        lon_list.append(lon_step)

    # HAVERSINE FUNCTION
    def haversine(lat1, lon1, lat2, lon2):
        lat1_rad = math.radians(lat1)
        lat2_rad = math.radians(lat2)
        lon1_rad = math.radians(lon1)
        lon2_rad = math.radians(lon2)
        delta_lat = lat2_rad - lat1_rad
        delta_lon = lon2_rad - lon1_rad
        a = math.sqrt(
            (math.sin(delta_lat / 2)) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * (math.sin(delta_lon / 2)) ** 2)
        d = 2 * 6371000 * math.asin(a)
        return d

    # DISTANCE CALCULATION
    d_list = []
    for j in range(len(lat_list)):
        lat_p = lat_list[j]
        lon_p = lon_list[j]
        dp = haversine(lat0, lon0, lat_p, lon_p) / 1000  # km
        d_list.append(dp)
    d_list_rev = d_list[::-1]  # reverse list

    # CONSTRUCT JSON
    d_ar = [{}] * len(lat_list)
    for i in range(len(lat_list)):
        d_ar[i] = {"latitude": lat_list[i], "longitude": lon_list[i]}
    location = {"locations": d_ar}
    json_data = json.dumps(location, skipkeys=int).encode('utf8')

    # SEND REQUEST
    print('\nRequesting data from https://api.open-elevation.com/api/v1/lookup')
    try:
        url = "https://api.open-elevation.com/api/v1/lookup"
        response = urllib.request.Request(url, json_data, headers={'Content-Type': 'application/json'})
        fp = urllib.request.urlopen(response)
    except KeyboardInterrupt:
        sys.exit(0)
    except SystemExit:
        sys.exit(0)
    except:
        print('\nRequest timed out. Trying again. Free service tho.')
        rerun = True
        geep(n1, n2)

    print('\nReceived Data')

    # RESPONSE PROCESSING
    res_byte = fp.read()
    res_str = res_byte.decode("utf8")
    js_str = json.loads(res_str)
    fp.close()

    # GETTING ELEVATION
    response_len = len(js_str['results'])
    elev_list = []
    for j in range(response_len):
        elev_list.append(js_str['results'][j]['elevation'])

    distance = d_list_rev[-1]

    print('\nPlotting elevation')

    # PLOT ELEVATION PROFILE
    base_reg = 0
    plt.figure(figsize=(10, 4), num='Towers: ' + str(n1+1) + ' - ' + str(n2+1))
    t1_p = [0, d_list_rev[-1]]
    t2_p = [elev_list[0], elev_list[-1]]
    deltaX = t2_p[1] - t2_p[0]
    deltaY = t1_p[1] - t1_p[0]
    angle = math.atan2(deltaY, deltaX) * 180 / math.pi
    plt.title('Distance: ' + str(distance) + ' km' + '\n Angle between towers LTR ref is horizon: '
              + str("%.2f" % round(angle, 2)) + 'º')
    plt.ylim(min(elev_list) - 20, max(elev_list) + 20)
    plt.plot(d_list_rev, elev_list)
    plt.plot([0, distance], [elev_list[0], elev_list[0]], '--g',
             label='Tower ' + str(n1) + ': ' + str(elev_list[0]) + ' m')
    plt.plot([0, distance], [elev_list[-1], elev_list[-1]], '--r',
             label='Tower ' + str(n2) + ': ' + str(elev_list[-1]) + ' m')
    plt.plot(t1_p, t2_p, label='LOS')

    plt.fill_between(d_list_rev, elev_list, base_reg, alpha=0.1)
    plt.text(d_list_rev[0], elev_list[0], 'Tower ' + str(n1 + 1))
    plt.text(d_list_rev[-1], elev_list[-1], 'Tower ' + str(n2 + 1))
    plt.plot(d_list_rev[0], elev_list[0], 'bo')
    plt.plot(d_list_rev[-1], elev_list[-1], 'bo')
    plt.xlabel("Distance(km)")
    plt.ylabel("Elevation(m)")
    plt.grid()
    plt.legend(fontsize='small')
    # print('\nClose graph to save data or exit program.')
    plt.ion()
    plt.show()
    plt.pause(0.001)
    # input("Press [enter] to continue.")

    print('\nSaving ' + dir_path + '/' + excel_filename + '_t' + str(n1 + 1) + '_t' + str(n2 + 1) + '.png')
    pic_path = str(os.path.join(dir_path, str(excel_filename), excel_filename))
    plt.savefig(
        pic_path + '_t' + str(n1 + 1) + '_t' + str(n2 + 1) + '.svg',
        format='svg', dpi=1200)
    plt.savefig(
        pic_path + '_t' + str(n1 + 1) + '_t' + str(n2 + 1) + '.png',
        format='png', dpi=1200)
    os.path.join("a",'b','c')
    if save_excel == 'yes' or save_excel == 'y':
        print('\nSaving to ' + str(excel_filename) + '.xlsx')
        elevations = []
        distances = []
        for x in elev_list:
            elevations.append(str(x))
        for x in d_list_rev:
            distances.append(str("%.3f" % round(x, 3)))
        if n1 == 0:
            workbook = xlsxwriter.Workbook(pic_path + '.xlsx')
            worksheet = workbook.add_worksheet()
            worksheet.write(0, 0, 'Distance (km)')
            worksheet.write(0, 1, 'Elevation (m)')
            worksheet.write(1, 2, 'Tower ' + str(n1 + 1))
            worksheet.write(len(elevations), 2, 'Tower ' + str(n2 + 1))
            for row_num, data in enumerate(distances):
                worksheet.write(row_num + 1, n1, data)
            for row_num, data in enumerate(elevations):
                worksheet.write(row_num + 1, n2, data)
            if len(tower_list) == 2:
                workbook.close()
                checkRerun()
        else:
            worksheet = workbook.get_worksheet_by_name('Sheet1')
            worksheet.write(0, 4, 'Distance (km)')
            worksheet.write(0, 5, 'Elevation (m)')
            worksheet.write(1, 6, 'Tower ' + str(n1 + 1))
            worksheet.write(len(elevations), 6, 'Tower ' + str(n2 + 1))
            for row_num, data in enumerate(distances):
                worksheet.write(row_num + 1, n1 + 3, data)
            for row_num, data in enumerate(elevations):
                worksheet.write(row_num + 1, n2 + 3, data)
            workbook.close()
            checkRerun()
        if len(tower_list) == 3 and not done:
            done = True
            print('\nRunning for tower 2 and 3')
            geep(1, 2)

    else:
        print('\nExiting...')
        sys.exit(0)


query()
