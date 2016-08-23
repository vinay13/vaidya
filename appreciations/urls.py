from django.conf.urls import patterns, url
from appreciations import views


urlpatterns = [
    url(r'^appreciations/$',views.AppreciationList.as_view()),
    ]