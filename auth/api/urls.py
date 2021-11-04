from auth.api.views import UserCreateViewSet
from rest_framework.routers import SimpleRouter

auth_router = SimpleRouter()
auth_router.register("profiles/create", UserCreateViewSet, basename="profile")
