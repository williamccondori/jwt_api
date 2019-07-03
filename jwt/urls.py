from django.conf.urls import url, include
from rest_framework_jwt.views import verify_jwt_token, obtain_jwt_token

from rest_framework import routers

app_name = 'jwt'

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^api-token-auth/', obtain_jwt_token),
]
