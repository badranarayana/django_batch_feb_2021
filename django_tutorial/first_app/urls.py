# all first app related urls mapped/define here

from django.urls import path
from .views import home_view
from .views import aboutus_view
from .views import contactus_view
from .views import get_dept_details

urlpatterns = [
    path('home', home_view),
    path("aboutus", aboutus_view),
    path("contactus", contactus_view),
    path("departments/<int:dept_id>/", get_dept_details),
]