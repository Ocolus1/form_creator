from django.urls import path

from . import views


urlpatterns = [
	#Leave as empty string for base url
	path('', views.index, name="index"),
	path('home/', views.home, name="home"),
	path('create/', views.create_form, name="create"),
	path('preview/', views.preview, name="preview"),
	path('delete_field/<id>/', views.del_field, name="delete_field"),
	path('tm/<short_url>/', views.floor_temp, name="floor_temp"),
]