from django.urls import path;
from . import views;
urlpatterns=[
    path('',views.notes,name="notes"),
    path('add',views.addNote,name="addNote"),
    path('delete',views.deleteNote,name="deleteNote"),

]