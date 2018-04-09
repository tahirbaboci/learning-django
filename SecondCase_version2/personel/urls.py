from django.conf.urls import url
from . import views

urlpatterns = [
    # /personel/
    url(r'^$', views.index, name='index'),
    # /personel/list/71/
    url(r'^list/(?P<Employee_id>[0-9]+)/$', views.detail, name='detail'),
    # /personel/list/
    url(r'list/', views.listData, name='listData'),
    # /personel/add/
    url(r'add/', views.add, name='add'),
    # /personel/add_me/
    url(r'^add_me/', views.add_me, name='add_me'),
    url(r'^add/validate_email', views.validate_email, name="validate_email"),
]

