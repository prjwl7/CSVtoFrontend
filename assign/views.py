from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from .models import Student, address, Hobby
from assign.forms import CSVUploadForm
from Script import read_data_csv



def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        print("Uploaded")
        if form.is_valid():
            print("Valid")
            csv_file = request.FILES['csv_file']
            fs = FileSystemStorage(location='media/uploads/')  # Set the location where original files will be stored
            carrier_filename = fs.save(csv_file.name, csv_file)
            print(carrier_filename)
            read_data_csv()
            print(request.FILES['csv_file'])
            return redirect(screen_database)
    else :
        form = CSVUploadForm()

    return render(request, 'home.html', {'form' : form})


def home_view(request, *args, **kwargs):
    return render(request, 'home.html')

# def get_csv(request, *args, **kwargs):
#     csv_file = request.FILES['csvUpload']
#     fs = FileSystemStorage(location='media/uploads/') 
#     csv_file_name = fs.save(csv_file.name, csv_file)
#     print(csv_file_name)
#     redirect(screen_database)
#     return render(request, 'home.html')    

def screen_database(request, *args, **kwargs):
    students = Student.objects.all()
    return render(request, 'home2.html', {'students' : students})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk = pk)
    return render(request, 'student_edit.html', {'student' : student})

def student_update(request, pk):
    student = get_object_or_404(Student, pk = pk)
    student.name = request.POST['name']
    student.age = request.POST['age']
    student.class_name = request.POST['class']
    student.address.address_street = request.POST['street']
    student.address.address_city = request.POST['city']
    student.address.address_city = request.POST['state']
    student.address.address_city = request.POST['zipcode']
    # print(student.address.address_city)
    student.hobby.hobby1 = request.POST['hobby1']
    student.hobby.hobby2 = request.POST['hobby2']
    student.hobby.hobby3 = request.POST['hobby3']
    student.save()
    student.address.save()
    student.hobby.save()
    return redirect(screen_database)

def screen_database1(request, *args, **kwargs):
    students = Student.objects.all()
    return render(request, 'home3.html', {'students' : students})