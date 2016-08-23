from django.conf.urls import patterns, url
from complaints import views


urlpatterns = [
    url(r'^complaints/$',views.ComplaintList.as_view()),
    url(r'^complaints/(?P<pk>[0-9]+)/$',views.ComplaintDetail.as_view()),
    ]