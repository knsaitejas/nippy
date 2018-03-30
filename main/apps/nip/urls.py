from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new_user/?$', views.new_user),      
    url(r'^login/?$', views.login),
    url(r'^strengths/?$', views.strength),
    url(r'^socials/?$', views.socials),
    url(r'^socials_process/?$', views.socials_process), 
    url(r'^process/?$', views.process), 
    url(r'^home/?$', views.home), 
    
]