# -*- coding -*- utf-8
from django.db.models import Q
from import_export import resources
from volunteers.models import Volunteer


class VolunteerResource(resources.ModelResource):
    class Meta:
        model = Volunteer
        fields = ('name', 'email', 'rg', 'birthdate', 'phone', 'occupation', 'organization', 'cep', 'address', 'complement', 'state', 'city', 'project',)
        export_order = ('name', 'email', 'rg', 'birthdate', 'phone', 'occupation', 'organization', 'cep', 'address', 'complement', 'state', 'city', 'project',)

    def dehydrate_volunteer(self, volunteer):
        return str(volunteer.volunteer)

    def dehydrate_training(self, volunteer):
        return str(volunteer.training)

    def get_or_init_instance(self, loader, row):
        instance = loader.get_queryset()\
                         .filter(email=row.get('email'))\
                         .first()
        if instance:
            return instance, False
        return self.init_instance(row), True
