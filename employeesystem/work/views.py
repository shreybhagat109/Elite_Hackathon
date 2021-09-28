from django.shortcuts import render
from .models import Employee
from math import ceil
def home(request):
    emp=Employee.objects.all()
    n=len(emp)
    slides=n//4 +ceil((n/4)-(n//4))
    allprods=[]
    cats=Employee.objects.values('city','id')
    cat={item['city'] for item in cats}
    for cat in cat:
        pro = Employee.objects.filter(city=cat)
        print(pro)
        n = len(pro)
        slides = n // 4 + ceil((n / 4) - (n // 4))

        allprods.append([pro,range(0,slides),slides])
    context={'allprods':allprods}
    return render(request,'home.html',context)

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
        pincode = request.POST['zip']
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

def paid_time_off(request):

    return render(request, 'paid_time_off.html')
