from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app import views

router=DefaultRouter()
router.register('tasks',views.TasksViewSets)

urlpatterns = [
    path('',include(router.urls))
]
