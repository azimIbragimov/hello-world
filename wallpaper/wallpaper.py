import ctypes, random, os, time


while True: 
    images = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    for (dirpath, dirnames, filenames) in os.walk(dir_path):
        images.append(filenames)

    images = images[1]
    random_picture = random.choice(images)

    absolute_path_of_picture = dir_path + '\\Images\\' + random_picture
    print(absolute_path_of_picture)


    SPI_SETDESKWALLPAPER = 20 
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 1, os.path.normpath(absolute_path_of_picture), 2)
    print(f"Photo has been changed. Image: {random_picture}")
    time.sleep(600)
