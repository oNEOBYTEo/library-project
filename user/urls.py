from rest_framework.routers import DefaultRouter

from .views import UserViewSet

router = DefaultRouter()
router.register("users-info", UserViewSet)
urlpatterns = router.urls
