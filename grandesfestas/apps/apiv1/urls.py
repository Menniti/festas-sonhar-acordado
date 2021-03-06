from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken import views as token_views

from apiv1 import views

router = routers.DefaultRouter()
router.register(r'trainings', views.TrainingViewSet)
router.register(r'subscriptions', views.SubscriptionViewSet)
router.register(r'volunteers', views.VolunteerViewSet)
router.register(r'contactemails', views.ContactEmailViewSet)

urlpatterns = [
    url(r'^', include(router.urls, namespace="api")),
    url(r'^paymentform/(bcash/)?(?P<subscription_id>[1-9]\d*)/?$', views.BcashFormAPIView.as_view(), name='bcash_form'),
    url(r'^paymentform/paypal/(?P<subscription_id>[1-9]\d*)/?$', views.PaypalFormAPIView.as_view(), name='paypal_form'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^token-auth/', token_views.obtain_auth_token)
]
