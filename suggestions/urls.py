from django.conf.urls import patterns, url
from suggestions import views


urlpatterns = [
    url(r'^suggestions/$',views.suggestion_list),
  #  url(r'^suggestions(?P<pk>[0-9]+)/$',views.suggestion_detail),

]