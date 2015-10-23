from django.conf.urls import url, include
from rest_framework import routers
from apiv1 import views

router = routers.DefaultRouter()
router.register(r'trainings', views.TrainingViewSet)
router.register(r'subscriptions', views.SubscriptionViewSet)
router.register(r'volunteers', views.VolunteerViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^paymentform/(?P<subscription_id>[1-9]\d*)/?$', views.PaymentFormAPIView.as_view(), name='payment_form'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
