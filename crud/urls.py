from django.urls import path
from .views import delete, home,create, update

urlpatterns = [
    path("", home, name="home-page"),
    path("create/", create, name="create-page"),
    path("update/<int:id>", update, name="update-page"),
    path("delet/<int:id>", delete, name="delete-page"),
]
