from django.shortcuts import render
from .models import Employee
def home(request):
    return render(request,"home.html")

def profile(request):
    return render(request,"profile.html")

def profile(request):
    if request.method == 'POST':
        email = request.POST['email']
        gender = request.POST['gender']
        phone = request.POST['phone']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        city = request.POST['city']
        address_pincode = request.POST['zip']
        state = request.POST['state']
        department = request.POST['department']
        employee = Employee( last_name=last_name,first_name=first_name, email=email, department=department,city=city, gender=gender, address_pincode=address_pincode,state=state)
        employee.save()
        print('user created')
    return render(request, 'profile.html')


def loginpage(request):
    return render(request, 'loginpage.html')

def register(request):
    return render(request, 'register.html')
