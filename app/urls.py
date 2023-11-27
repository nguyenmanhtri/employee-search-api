from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from search.views import views
from search.views.employees import EmployeeViewSet

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"employees", EmployeeViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
