from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views


router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)
router.register(r'news', views.NewsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', obtain_auth_token, name='obtain-token')
]
