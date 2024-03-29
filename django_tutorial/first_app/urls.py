# all first app related urls mapped/define here

from django.urls import path
from .views import home_view
from .views import aboutus_view
from .views import contactus_view
from .views import get_dept_details
from .views import get_dept_list
from .views import create_dept
from .views import render_with_django_form
from .views import inventory_view

from .views import (indexView, postFriend, checkNickName)

urlpatterns = [
    path('home', home_view),
    path("aboutus", aboutus_view),
    path("contactus", contactus_view),
    path("departments/<int:dept_id>/", get_dept_details),
    path("departments/dept_list", get_dept_list, name='dept_list'),
    path("departments/create", create_dept, name='create_dept'),
    path("testforms", render_with_django_form, name='test_forms'),
    path("inventory", inventory_view, name="create_inventory"),
    path('index', indexView),
    path('post/ajax/friend', postFriend, name="post_friend"),
    path('get/ajax/validate/nickname', checkNickName, name="validate_nick_name"),

]