from django.shortcuts import render,HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')
# for view all employees we create this function.
def all_emp(request):
    emp = Employee.objects.all()
    context = {
        'emps': emp
    }
    print(context)
    return render(request, 'view_all_emp.html',context)
# for adding an employee we create this function
def add_emp(request):
    # print("request method", request)
    # print("request method data", request.POST)
    # the below code is only execute if the request method is 'POST'
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = int(request.POST['dept'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = int(request.POST['role'])
        phone = int(request.POST['phone'])
        # print("#########",first_name)
        # print("1111",last_name)
        # print("!!!!!!",dept)
        # print("#########",salary)
        # print("#########",bonus)
        # print("#########",role)
        # print("#########",phone)
        # the below line is to insert data for the several fields and save
        new_emp = Employee(first_name = first_name, last_name = last_name, dept_id = dept, salary = salary,bonus = bonus, role_id = role, phone = phone,hire_date = datetime.now())
        new_emp.save()
        # print("#############################",new_emp)
        return HttpResponse('Employee Added Successfully')
        
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("An exceptional error occured")
# create this function to remove an employee
def remove_emp(request,emp_id = 0):
    #print("########################",request)
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id = emp_id)
            # print("------------->",emp_to_be_removed)
            # print("------------->",type(emp_to_be_removed))
            # print("------------->",emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please add a valid emp id")
            
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html',context)
# create this function to filter the employee
def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name = dept)
        if role:
            emps = emps.filter(role__name = role)

        context = {
            'emps': emps
        }
        return render(request,'view_all_emp.html',context)
    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse("An exceptional error occured")