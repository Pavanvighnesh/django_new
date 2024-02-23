from django.conf import urls
from . import views
from django.urls import path


app_name='my_app'
urlpatterns=[
    path('first',views.first,name='first'),
    path('second',views.second,name='second'),
    path('user',views.users,name='user'),
    path('register',views.register,name="register")

]