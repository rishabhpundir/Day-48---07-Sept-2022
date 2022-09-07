from django.urls import path, include
from apiapp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('api', views.PersonView, basename='api')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.RegisterView.as_view()),
    path('login/', include('rest_framework.urls'))
]
