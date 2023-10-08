from django.shortcuts import render
from django.http import HttpResponse
from .models import internship
import re

def home_page(request):

    if request.method == "POST":
        name = request.POST['Name_']
        college = request.POST['college_']
        email = request.POST['Email_']
        phone = request.POST['phone_']
        experience = request.POST['experience_']
        Subject = request.POST['Subject_']
        
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if !re.match(pattern, email):
            return Httpresponse('Add Valid Mail')

        pattern2 = r'^\d{10}$'
        if !re.match(pattern, phone):
            return Httpresponse(' Add Valid Phone Number ')        
  
        student = internship()
        student.name = name
        student.college = college
        student.Email = email
        student.phone = phone
        student.experience = experience
        student.Subject = Subject
        student.save()
        return render(request , 'shop\index2.html')
    return render(request , 'shop\index.html')









# print(" Your name Is : ",name)
        # print(" Your college Is : ",college)
        # print(" Your email Is : ",email)
        # print(" Your phone Is : ",phone)
        # print(" Your experience Is : ",experience)
        # print("Your Subject Is : ",Subject)
