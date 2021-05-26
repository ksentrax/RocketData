from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    url(r'^employees/$', views.EmployeeList.as_view()),
    url(r'^employees/(?P<pk>\d+)/$', views.EmployeeDetail.as_view()),
    url(r'^employees/levels/(?P<levels>\d+)/$', views.EmployeeListLevel.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>\d+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
