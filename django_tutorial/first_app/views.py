from django.shortcuts import render, HttpResponse, redirect
from .forms import EmployeeForm

# Simplae views to understad the django concepts, in realtime we may to write some complex views
# Create your views here.
def home_view(request):
    # QUERY DATABASE
    # Design template
    # give HTML resposne
    return render(request, template_name="first_app/home.html", context={})

def aboutus_view(request):
    # QUERY DATABASE
    # Design template
    # give HTML resposne
    return render(request, template_name="first_app/aboutus.html", context={})

def contactus_view(request):
    # QUERY DATABASE
    # Design template
    # give HTML resposne
    return render(request, template_name="first_app/contactus.html", context={})

from .models import Department
def get_dept_details(request, dept_id):
    print(" ID IS", dept_id)
    # select * from department where id = dept_id
    try:
        dept_details = Department.objects.get(pk=dept_id)
    except Exception as e:
        dept_details = None
    dept = {}
    if dept_details:
        dept['name'] = dept_details.name
        dept['description'] = dept_details.description
    else:
        dept['exception'] = f"NO Details found for id {dept_id}"
    return render(request, template_name="first_app/dept_details.html", context=dept)

def get_dept_list(request):
    """
    get all depts form db and display in html
    :param request:
    :return:
    """

    departments = Department.objects.all()
    context = {}
    context['departments'] = departments
    context['userName'] = 'Badra'

    return render(request, template_name="first_app/dept_list.html", context=context)


def create_dept(request):
    """
    This view is responsible to give template and handl posting of data
    :param request:
    :return:
    """
    # 'get' and 'post'
    if request.method == 'POST':
        #import pdb;pdb.set_trace()
        # l - show the few lines of code
        # n - go to next line
        # c - continue
        """
        <QueryDict: {'csrfmiddlewaretoken': ['wiMalhPw2pclV1mFIK4u9XwWZJmUKJ2kL7VgJtN4iTZA6XjI3Y7zUsRNnkU4xwyt'], 
        'deptName': ['my nde dept 1'], 'deptDescription': ['new dept description'], 'deptLocation': ['mumbai'], 'deptPinCode': ['566622']}>
        """
        dept_name = request.POST.get('deptName')
        dept_description = request.POST.get('deptDescription')
        dept_location = request.POST.get('deptLocation')
        dept_pin_code = request.POST.get('deptPinCode')
        # ORM class(model)
        dept = Department(name=dept_name, description=dept_description, location=dept_location, pin_code=dept_pin_code)
        dept.save()
        return redirect(to="dept_list")


    if request.method == 'GET':
        return render(request, template_name="first_app/create_dept.html", context={})


def render_with_django_form(request):
    context = {}

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        context['employeeForm'] = form
        if form.is_valid():
            # model required to save data

            return HttpResponse("Form submitted.")

    else:  # get request
        form = EmployeeForm()
        context['employeeForm'] = form

    return render(request, template_name='first_app/testforms.html', context=context)


"""
--> Form generate HTML inputs/Elements(with all html features)
--> Form validate data once data is submitted(only when we call form.is_valid()(True if valid)



"""







