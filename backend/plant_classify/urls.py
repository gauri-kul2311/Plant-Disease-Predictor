from rest_framework import urlpatterns
from .views import PlantViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'plants',PlantViewSet)
urlpatterns = router.urls