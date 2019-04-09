from django.conf.urls import url
from rto_app import views

app_name = 'rto_app'


urlpatterns = [
    url(r'^$', views.user_login, name='user_login'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^latest_images/', views.latest_images, name='latest_images'),
    url(r'^apply_fine/', views.apply_fine, name='apply_fine'),
    url(r'^fine_applied/', views.fine_applied, name='fine_applied'),
]
