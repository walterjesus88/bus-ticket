from django.urls import include, path
from rest_framework.routers import DefaultRouter
from routes import views

router = DefaultRouter()
router.register(r'route', views.RouteViewSet, basename='route')
router.register(r'city', views.CityViewSet, basename='city')

urlpatterns = [
  path('', include(router.urls))
]
