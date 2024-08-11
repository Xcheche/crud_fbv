from django.urls import path

from . import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),  # fbv_crud/ => fbv_crud/index.html
    path("create_students/", views.create_students, name="create_students"),
    path("/delete/<int:pk>", views.delete, name="delete"),
    path("update/<int:pk>", views.update, name="update"),
]
