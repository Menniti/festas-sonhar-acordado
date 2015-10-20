# -*- coding: utf-8 -*-
from rest_framework import viewsets
from trainings.models import Training

from apiv1.serializers import TrainingSerializer


class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.select_related('local').all().order_by('date')
    serializer_class = TrainingSerializer
