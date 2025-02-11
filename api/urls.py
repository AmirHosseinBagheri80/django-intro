from django.urls import path,include
from .import views
urlpatterns = [
    path('generate-password',views.generate_password),
]
