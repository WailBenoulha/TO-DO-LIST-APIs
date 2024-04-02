from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from accounts import views

router = DefaultRouter()
router.register('users',views.UserViewSet)

urlpatterns = [
    path('profiles/',include(router.urls)),
    path('login/',views.UserLoginApiView.as_view()),
]