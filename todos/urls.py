from django.conf.urls import include, url
from django.contrib import admin
from todos import views #gets all our view functions

urlpatterns = [
    # url(r'^$', views.Index.as_view(), name='index'),
    url(r'^register$', views.RegisterUser.as_view(), name='register'),
    # url(r'^login$', views.LoginUser.as_view(), name='login'),
    # url(r'^add$', views.AddTodo.as_view(), name='add'),
    # url(r'^search$', views.SearchTodo.as_view(), name='search'),
]
