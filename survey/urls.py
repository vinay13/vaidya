from django.conf.urls import patterns, url
from survey import views


urlpatterns = [
    url(r'^surveys/$',views.SurveyView.as_view()),
    url(r'^surveys/(?P<pk>[0-9]+)/$',views.SurveyDetail.as_view()),
    url(r'^questions/$',views.QuestionView.as_view()),
    url(r'^questions/(?P<pk>[0-9]+)$',views.QuestionDetail.as_view()),
   # url(r'^choices/$',views.GetChoices.as_view()),
]

