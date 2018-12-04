from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.login, name='login'),
    path('log/', views.log, name='log'),
    path('ListCS/', views.ListCS, name='ListCS')

]
