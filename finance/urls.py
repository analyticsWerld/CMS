from django.urls import path
from . import views
urlpatterns = [
    path("show",views.show_Finance, name = "show_finance"),
    path("edit/<int:id>",views.editFinance, name = "edit_finance"),
    path("remove/<int:id>",views.delete_Finance, name = "delete_finance"),
    path("create",views.createFinance, name = "create"),
]