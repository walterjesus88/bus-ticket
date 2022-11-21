#Django
from django.urls import include, path

#Django rest framework
from rest_framework.routers import DefaultRouter

#Views 
from vehicles import views

router = DefaultRouter()
router.register(r'vehicles',views.VehicleViewSet, basename='vehicles')


urlpatterns = [
    path('',include(router.urls))
]