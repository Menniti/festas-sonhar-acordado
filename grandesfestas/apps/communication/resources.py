# -*- coding -*- utf-8
from import_export import resources
from communication.models import ContactEmail


class ContactEmailResource(resources.ModelResource):
    class Meta:
        skip_unchanged = True
        model = ContactEmail
