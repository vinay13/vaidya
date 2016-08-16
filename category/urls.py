from django.conf.urls import patterns, url , include
from rest_framework_nested import routers
from views import CategoryViewSet 


router = routers.SimpleRouter()
router.register(r'category',CategoryViewSet)


urlpatterns = [

		url(r'^',include(router.urls)),
		
]