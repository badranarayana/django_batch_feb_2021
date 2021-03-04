from django.shortcuts import render, HttpResponse

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









