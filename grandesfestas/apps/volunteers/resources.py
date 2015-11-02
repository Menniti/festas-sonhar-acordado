# -*- coding -*- utf-8
from import_export import resources
from volunteers.models import Volunteer


class VolunteerResource(resources.ModelResource):
    class Meta:
        model = Volunteer
        fields = ('name', 'email', 'created_date', 'rg', 'birthdate', 'phone', 'occupation', 'organization', 'cep', 'address', 'complement', 'state', 'city', 'project',)
        export_order = ('name', 'email', 'created_date', 'rg', 'birthdate', 'phone', 'occupation', 'organization', 'cep', 'address', 'complement', 'state', 'city', 'project',)

    def dehydrate_volunteer(self, volunteer):
        return str(volunteer.volunteer)

    def dehydrate_training(self, volunteer):
        return str(volunteer.training)
