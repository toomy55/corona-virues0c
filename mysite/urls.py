from django.contrib import admin
from django.urls import path

from mysite.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('AR', views.homeAR, name='homeAR'),

    path('population-chart/', views.population_chart, name='population-chart'),
    path('pie-chart/', views.pie_chart, name='pie-chart'),
    path('daily_chart/', views.daily_chart, name='daily_chart'),
    path('avreg_chart/', views.avreg_chart, name='avreg_chart'),
    path('manths_chart/', views.manths_chart, name='manths_chart'),
    path('week_chart/', views.week_chart, name='week_chart'),




    path('admin/', admin.site.urls),
]
