from django.conf.urls import url, patterns, include

from rest_framework import routers

from api.views import TransactionViewSet, AccountViewSet

router = routers.DefaultRouter()
router.register(r'account', AccountViewSet)
router.register(r'transaction', TransactionViewSet)


urlpatterns = patterns(
    '',
    url('', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
)
