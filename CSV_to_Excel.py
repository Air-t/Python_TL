#!D:\Tools\Python37\python.exe

# shebang (line above) shows the exe file for python 3 on your computer

'''
Created on 15 paz 2018

@author: ADP
'''

import glob, csv, os
from openpyxl import Workbook

# fill working directory (use double backslash "\\" to separate directories)
input_path = "C:\\Users\\ADP\\Desktop\\csv"
output_path = "C:\\Users\\ADP\\Desktop\\csv\\1"

#fill desired file extension
extension = "csv"


# returns list of csv files in a given directory
def map_dir(path, extension):
    csv_names =[]  
    file_names = os.listdir(path)
    for name in file_names:
        if name.endswith(extension):
            csv_names.append(name.rstrip("."+extension))
        else:
            pass
    return csv_names 

# converts single csv to xlsx file and saves it in desired directory       
def csv_to_xlsx(file_name, file_path, extension):
    
    # set up new line and standard csv delimiter
    with open((file_name + "." + extension), newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
           
        # create new spreadsheet with active first sheet
        wb = Workbook()
        ws = wb.active
        
        for line in csv_reader:
            ws.append(line)
        
        # create output path directory, file name and format
        path = "{}\\{}.xlsx".format(file_path, file_name)
        
        wb.save(path)


#-------------------------------------------------------------


# change directory to input path
os.chdir(input_path)

# get csv file list
csv_file_list = map_dir(input_path, extension)

print(csv_file_list)

for file in csv_file_list:
    csv_to_xlsx(file, output_path, extension)






















