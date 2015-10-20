# -*- coding: utf-8 -*-
from rest_framework import viewsets

from trainings.models import Training
from volunteers.models import Volunteer
from subscriptions.models import Subscription

from apiv1.serializers import (SubscriptionSerializer,
                               TrainingSerializer,
                               VolunteerSerializer, )


class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.select_related('local').all().order_by('date')
    serializer_class = TrainingSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
