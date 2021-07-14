from django.conf.urls import url

from app import views

app_name = 'app'

urlpatterns = {
    url('^$', views.index, name='index'),
    url('^checkservice$', views.check_service, name='check_service'),
}
