from rest_framework.routers import DefaultRouter
from .views import BookViewset, BookItemViewSet

router = DefaultRouter()
router.register("catalog", BookViewset)
router.register("book-items", BookItemViewSet)
urlpatterns = router.urls
