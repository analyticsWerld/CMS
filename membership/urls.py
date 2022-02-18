from django.urls import path
from . import views
urlpatterns = [
    path("show_member/<int:id>",views.show_member, name = "show_member"),
    path("show_members",views.show_members, name = "show_members"),
    path("edit/<int:id>",views.edit_member, name = "edit"),
    path("remove/<int:id>",views.delete_member, name = "delete"),
    path("create",views.create_member, name = "create"),
    path("search/",views.search,name="search_results")
]