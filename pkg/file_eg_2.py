# --------------------
# File      : .py
# Created   : 22-10-2021 {TIME}
# Author    : Sreejith
# Version   : v1.0.0.
# Licensing : (C) 2021  Sreejith , LYIT
#             Available under  GNU Public License (GPL)
# Description :
# --------------------

def file_processing2(file_name):
    #open a file with the list of students and print their details...

    file_obj = open(file_name,"r+")
    #Lines.sort()  # this method can be used to sort a file

    for line in file_obj:
        print(line.rstrip())  #remove or strip whitespace at the end of the line while printing

    file_obj.write("\nThe Stopper, L0054321, BSc in Computing")
    file_obj.seek(0)

    print("\nAfter the student has been added: ")
    all_file_contents = file_obj.read()
    print(all_file_contents)
    file_obj.close()

if __name__ == '__main__':
    file_processing2("sample.txt")