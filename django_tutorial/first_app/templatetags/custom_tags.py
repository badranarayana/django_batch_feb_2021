from django import template
from datetime import datetime
from django.contrib.auth import get_user_model
from django.template.loader import get_template

from first_app.forms import ContactModelForm


User = get_user_model()

register = template.Library()
# any number of custom tags, python functions and resister with regitry

def modify_name(value, arg):
    # if arg is first_name: return the first string before space
    if arg == "first_name":
        return value.split(" ")[0]
   # if arg is last_name: return the last string before space
    if arg == "last_name":
        return value.split(" ")[-1]
    # if arg is title_case: return the title case of the string
    if arg == "title_case":
        return value.title()
    if arg == 'upper_case':
        return value.upper()

    return value

register.filter("modify_name", modify_name)

@register.simple_tag
def current_time(formate_str):
    return datetime.now().strftime(formate_str)   # '12/2/2021

class user:
    pass

#@register.inclusion_tag('first_app/users.html')
def show_users_table():
    users = User.objects.all()
    # import pdb;pdb.set_trace()
    # obj = user()
    # obj.first_name = "Badra"
    # obj.last_name = "A"
    # obj.username = "Abc"
    # obj.email = "abc@gmail.com"
    return {'users': users}

# import pdb;pdb.set_trace()
users_template = get_template('first_app/users.html')
register.inclusion_tag(users_template)(show_users_table)


def show_contact_form():
    form = ContactModelForm()

    return {'contactForm': form}

# template to render form
contact_template = get_template('first_app/contact.html')
register.inclusion_tag(contact_template)(show_contact_form)





