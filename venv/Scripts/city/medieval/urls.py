from django.urls import path
 
from . import views
app_name = 'medieval'
 
urlpatterns = [
	path('', views.index, name='index'),
	
]
