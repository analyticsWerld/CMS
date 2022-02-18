from django.urls import path
from . import views

urlpatterns = [
    path("show",views.show_Announcement, name = "show_announcement"),
    path("edit/<int:id>",views.editAnnouncement, name = "edit_announcement"),
    path("remove/<int:id>",views.delete_Announcement, name = "delete_announcement"),
    path("create",views.createAnnouncement, name = "create_announcement"),
]