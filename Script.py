#Create an application to load student data from a CSV file into a database. Each row should contain student details such as name, age, class, address_street, address_city, address_state, address_zipcode, hobby1, hobby2, and hobby3. Please ensure to create three tables for storing the user’s basic information, address, and hobby; they should be appropriately connected with foreign keys. The data should be listed, and it should be editable as well.

import numpy as np
import pandas as pd
import os
import csv
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "assign.settings")
import django
django.setup()
# from models import Student, address, hobby
from assign.models import Student, address, Hobby

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
print(script_dir)
print(os.path.exists(script_dir))
common_parent_dir = os.path.abspath(os.path.join(script_dir, '..'))
true_folder = os.path.abspath(os.path.join(common_parent_dir, '..'))
output_folder_path = os.path.join(script_dir, 'media', 'uploads')
print(output_folder_path)
host_audio_path = os.path.join(output_folder_path, 'Untitled spreadsheet - Sheet1 (1).csv')
print(host_audio_path)

def read_data_csv():
    
    with open(host_audio_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader :
            student = Student.objects.create(name = row['name'], age = row['age'], class_name = row['class'])
            address.objects.create(student = student, address_street = row['address_street'], address_city = row['address_city'], address_state = row['address_state'], address_zipcode = row['address_zipcode'])
            Hobby.objects.create(student = student, hobby1 = row['hobby1'], hobby2 = row['hobby2'], hobby3 = row['hobby3'])

if __name__ == '__main__':
    read_data_csv()
