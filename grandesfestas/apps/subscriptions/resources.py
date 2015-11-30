# -*- coding -*- utf-8
from import_export import resources
from subscriptions.models import Subscription


class SubscriptionResource(resources.ModelResource):
    class Meta:
        model = Subscription
        fields = ('volunteer', 'volunteer__project', 'training', 'present', 'paid', 'party', 'payment', 'valid', 'extra', )
        export_order = ('volunteer', 'volunteer__project', 'training', 'present', 'party', 'paid', 'payment', 'valid', 'extra', )

    def dehydrate_volunteer(self, subscription):
        return str(subscription.volunteer)

    def dehydrate_training(self, subscription):
        return str(subscription.training)
