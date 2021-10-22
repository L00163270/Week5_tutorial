# --------------------
# File      : .py
# Created   : 18-10-2021 {TIME}
# Author    : Sreejith
# Version   : v1.0.0.
# Licensing : (C) 2021  Sreejith , LYIT
#             Available under  GNU Public License (GPL)
# Description :
# --------------------


def file_processing(file_name):
        """Open a file with a list of students and print their details...."""
        lines = open(file_name).readlines()
        # lines.sort() #this method can be used to sort a file

        for line in lines:
            student, l_num, course = line.split(",")
            print("Student Name:{0} \nLNumber: \t{1} \nCourse\t\t{2}\n".format(student, l_num, course) )

if __name__ == '__main_':
    file_processing("sample.txt")




