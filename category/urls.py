from django.conf.urls import url , include
from rest_framework_nested import routers
from views import CategoryViewSet , SubCategoryViewSet


router = routers.SimpleRouter()
router.register(r'category',CategoryViewSet)
router.register(r'subcategory',SubCategoryViewSet)


urlpatterns = [

		url(r'^',include(router.urls)),
		
]