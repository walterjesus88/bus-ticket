#Django
from django.urls import include, path

#Django rest framework
from rest_framework.routers import DefaultRouter

#Views 
from users import views

router = DefaultRouter()
router.register(r'users',views.UserViewSet, basename='users')


urlpatterns = [
    path('',include(router.urls))
]