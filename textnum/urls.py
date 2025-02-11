from django.urls import path,include
from . import views
urlpatterns = [
    path('number_text',views.number_text)
]
