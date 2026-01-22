from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, UserProjectsView

router = DefaultRouter()
router.register(r'clients', ClientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('projects/', UserProjectsView.as_view()),
]