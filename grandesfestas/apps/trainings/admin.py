from django.contrib import admin
from trainings.models import Training, TrainingLocal


@admin.register(TrainingLocal)
class TrainingLocalAdmin(admin.ModelAdmin):
    list_display = ('name', 'cep', 'address', 'complement', 'state', 'city', 'lat', 'lon',)
    search_fields = ('name', 'cep', 'address', 'complement', 'state', 'city',)


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ('local', 'date',)
