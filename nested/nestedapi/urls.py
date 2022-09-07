from django.urls import path, include
from rest_framework.routers import DefaultRouter
from nestedapi import views

router = DefaultRouter()
router.register('school', views.SchoolView, basename='school')
router.register('class', views.ClassView, basename='class')
router.register('student', views.StudentView, basename='student')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.RegisterView.as_view()),
    path('auth/', include('rest_framework.urls')),
]
