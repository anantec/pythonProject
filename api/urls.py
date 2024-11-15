from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccessViewSet, UsersViewSet, login_view, RecordViewSet

router = DefaultRouter()
router.register(r'access', AccessViewSet)
router.register(r'users', UsersViewSet)
router.register(r'records', RecordViewSet)  # New endpoint for Record

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_view, name='login'),
]
