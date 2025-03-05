from rest_framework.routers import SimpleRouter

from .views import UserViewSet, PostViewSet

router = SimpleRouter()
router.register("users", UserViewSet, basename="users")  # /api/v1/users/
router.register("", PostViewSet, basename="posts")  # /api/v1/

urlpatterns = router.urls
