# --------------------
# File      : .py
# Created   : 22-10-2021 {TIME}
# Author    : Sreejith
# Version   : v1.0.0.
# Licensing : (C) 2021  Sreejith , LYIT
#             Available under  GNU Public License (GPL)
# Description :
# --------------------


import os


def file_processing3(file_name):

    file_obj = open(file_name,"r+")
    # 1
    # file_obj.seek(0) # rewind the file - start at position 0

    # 2
    # file_obj.seek(10, 0) # Move 10 bytes forward from the start (0) of file0=SEEK_SET

    # 3
    file_obj.seek(1, os.SEEK_SET) # move 1 byte forward from the beginning

    # 4
    # file_obj.seek(0, os.SEEK_CUR) # seek the current position, offset must be 0

    # 5
    # file_obj.seek(0, os.SEEK_END) # Reset the current position (SEEK_END) of file
    all_file_contents = file_obj.read() # read the files from the set position
    print(all_file_contents) # print the contents to demo where the start point was
    file_obj.close()

if __name__ == '__main__':
 '''
 Main method of application
 Demo seek
 Parameters:
 none
 Returns:
 none
 '''
file_processing3("sample.txt")