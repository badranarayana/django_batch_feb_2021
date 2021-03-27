from django import template

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
