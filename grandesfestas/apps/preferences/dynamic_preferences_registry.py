from dynamic_preferences.types import BooleanPreference, StringPreference
from dynamic_preferences import user_preferences_registry, global_preferences_registry

from preferences.types import FloatPreference


@global_preferences_registry.register
class SiteTitle(StringPreference):
    section = 'general'
    name = 'title'
    default = 'Grandes festas do Sonhar Acordado'
    verbose_name = 'Título do site'


@global_preferences_registry.register
class SiteUrl(StringPreference):
    section = 'general'
    name = 'site_url'
    default = 'http://localhost:8000'
    verbose_name = 'URL base do site'


@global_preferences_registry.register
class PaypalReceiverEmail(StringPreference):
    section = 'payment'
    name = 'paypal_receiver_email'
    default = 'receiver@paypaltest.com'
    verbose_name = 'Email do recebedor no PayPal'


@global_preferences_registry.register
class PaypalTest(BooleanPreference):
    section = 'payment'
    name = 'paypal_test'
    default = True
    verbose_name = 'Transações fake no PayPal'


@global_preferences_registry.register
class PaypalCancelExplanation(StringPreference):
    section = 'payment'
    name = 'cancel_explanation_path'
    default = '/pagamento-cancelado'
    verbose_name = 'Informativo de pagamento cancelado'


@global_preferences_registry.register
class PaypalCustom(StringPreference):
    section = 'payment'
    name = 'campaign'
    default = 'Festa de Natal 2015'
    verbose_name = 'Objetivo da arrecadação'


@global_preferences_registry.register
class PaypalItemName(StringPreference):
    section = 'payment'
    name = 'item_name'
    default = 'Inscrição de {0}'
    help_text = '{0} vira o nome do voluntário'
    verbose_name = 'Nome do item'


@global_preferences_registry.register
class PaypalReturn(StringPreference):
    section = 'payment'
    name = 'return_after_payment'
    default = '/obrigado'
    verbose_name = 'Caminho de retorno'


@global_preferences_registry.register
class SubscriptionValue(FloatPreference):
    section = 'subscription'
    name = 'ticket_value'
    default = 40
    verbose_name = 'Valor da inscrição'


@global_preferences_registry.register
class SubscriptionOpen(BooleanPreference):
    section = 'subscription'
    name = 'ticket_open'
    default = True
    verbose_name = 'Aberto para inscrições'

#
#20150000332879
#
#1001629
#