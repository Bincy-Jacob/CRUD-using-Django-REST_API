from django.urls import path
from . import views

urlpatterns = [
    path('',views.Apioverview,name='home'),
    path('emplist/',views.Emplist,name='emplist'),
    path('empcreate/',views.Empcreate,name='empcreate'),
    path('empupdate/<int:pk>/',views.Empupdate,name='empupdate'),
    path('empdelete/<int:pk>/',views.Empdelete,name='empupdate'),
    path('emplistid/<int:pk>/',views.Emplistid,name='emplistid'),
]