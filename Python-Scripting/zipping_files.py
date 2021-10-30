#!/usr/bin/env python3

import os
import zipfile

# this function will back up an entire folder to a .zip file
def backup_zip(folder):
    folder = os.path.abspath(folder)    # use absolute path
    
    # determine filename to back up to
    ver = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(ver) + '.zip'
        if not os.path.exists(zip_filename):
            break
        ver += 1

    # create the zip file
    print("\narchiving %s..." % (zip_filename))
    backup_zip_file = zipfile.ZipFile(zip_filename, 'w')
    
    # walk the folder tree in it's entirety to compress all files in subfolders as well
    # during each iteration of the for loop os.walk returns the current folder name, 
    # subfolders in that folder, as well as all the filenames within that folder
    for foldername, subfolders, filenames in os.walk(folder):
        print("\nadding files in %s..." % (foldername))
        backup_zip_file.write(foldername)
        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue # we don't want to back up zip files
            backup_zip_file.write(os.path.join(foldername, filename))
    backup_zip_file.close()
    print("\narchiving complete. {} created successfully!".format(zip_filename))

    
backup_zip('c:\\it_osaiti\\139895')