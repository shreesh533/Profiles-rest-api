from django.urls import path
from profiles_api import views

urlpatterns = [
    path("hello-view", views.HelloApiView.as_view(), name="HelloApiView"),
    path("hello-world", views.hello_world, name="HelloApiView")
]
