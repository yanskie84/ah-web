from django.urls import path

from.import views

app_name = 'modul'

urlpatterns = [
    path('python/', views.python, name='modul1'),
    path('gui/', views.gui, name='modul2'),
    path('statis/', views.statis, name='modul3'),
    path('dinamis/', views.dinamis, name='modul4'),
]