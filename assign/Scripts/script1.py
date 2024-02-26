#Create an application to load student data from a CSV file into a database. Each row should contain student details such as name, age, class, address_street, address_city, address_state, address_zipcode, hobby1, hobby2, and hobby3. Please ensure to create three tables for storing the user’s basic information, address, and hobby; they should be appropriately connected with foreign keys. The data should be listed, and it should be editable as well.

import numpy as np
import pandas as pd
import os
import csv
# from models import Student, address, hobby
from assign.models import Student, address, hobby
def read_data_csv():
    with open('data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
    for row in reader :
        student = Student.objects.create(name = row['name'], age = row['age'], class_name = row['class'])
        address.objects.create(student = student, address_street = row['address_street'], address_city = row['address_city'], address_state = row['address_state'], address_zipcode = row['address_zipcode'])
    for x in [row['hobby1'], row['hobby2'], row['hobby3']]:
        if x:
            hobby.objects.create(student=student, hobby = hobby)

if __name__ == '__main__':
    read_data_csv()
