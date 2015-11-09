# -*- coding: utf-8 -*-
from dynamic_preferences.types import BooleanPreference, StringPreference, IntegerPreference
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
class PaymentReceiverEmail(StringPreference):
    section = 'payment'
    name = 'receiver_email'
    default = 'receiver@payment.com'
    verbose_name = 'Email do recebedor do pagamento'


@global_preferences_registry.register
class PaypalReceiverEmail(StringPreference):
    section = 'payment'
    name = 'paypal_receiver_email'
    default = 'receiver@payment.com'
    verbose_name = 'Email do recebedor do paypal'


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
class BCashSecret(StringPreference):
    section = 'payment'
    name = 'bcash_secret'
    default = ''
    verbose_name = 'Chave secreta do BCash'


@global_preferences_registry.register
class BCashCodloja(StringPreference):
    section = 'payment'
    name = 'bcash_cod_loja'
    default = ''
    verbose_name = 'Código da loja do BCash'


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


@global_preferences_registry.register
class TrainingNotificationOpen(IntegerPreference):
    section = 'training'
    name = 'notification_before'
    default = 2
    verbose_name = 'Notificar treinamento x dias antes'


@global_preferences_registry.register
class MandrillApiKey(StringPreference):
    section = 'mail'
    name = 'mandrill_api_key'
    default = ''
    verbose_name = 'Chave do mandrill'


@global_preferences_registry.register
class DefaultFromEmail(StringPreference):
    section = 'mail'
    name = 'default_from_email'
    default = 'voluntarios@sonharacodado.com.br'
    verbose_name = 'Remetente padrão'


@global_preferences_registry.register
class DefaultToEmail(StringPreference):
    section = 'mail'
    name = 'default_to_email'
    default = 'voluntarios@sonharacodado.com.br'
    verbose_name = 'Destinatário padrão'
