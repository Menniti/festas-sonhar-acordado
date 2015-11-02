# -*- coding -*- utf-8
from import_export import resources
from subscriptions.models import Subscription


class SubscriptionResource(resources.ModelResource):
    class Meta:
        model = Subscription
        fields = ('volunteer', 'training', 'present', 'paid', 'payment', 'valid', 'extra', )
        export_order = ('volunteer', 'training', 'present', 'paid', 'payment', 'valid', 'extra', )

    def dehydrate_volunteer(self, subscription):
        return str(subscription.volunteer)

    def dehydrate_training(self, subscription):
        return str(subscription.training)
