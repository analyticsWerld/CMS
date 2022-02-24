from django.urls import path
from . import views

urlpatterns = [
    #path("show",views.show_attendance, name = "show_attendance"),
    #path("edit/<int:id>",views.edit_attendance, name = "edit_attendance"),
    #path("remove/<int:id>",views.delete_attendance, name = "delete_attendance"),
    path("take_attendance",views.attendance, name = "attendance"),
    path("try",views.atten, name = "try"),    
]