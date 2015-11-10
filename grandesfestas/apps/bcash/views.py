import json
import urllib

from hashlib import md5
from collections import OrderedDict

from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import classonlymethod
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from bcash.models import Transaction


class BCashUpdateView(View):

    def post(self, request):
        try:
            if 'id_pedido' in request.POST:
                order = int(request.POST.get('id_pedido'))
            elif 'pedido' in request.POST:
                order = int(request.POST.get('pedido'))

            if 'transacao_id' in request.POST:
                transaction = int(request.POST.get('transacao_id'))
            elif 'id_transacao' in request.POST:
                transaction = int(request.POST.get('id_transacao'))

            status = request.POST.get('status', '')
            status_code = int(request.POST.get('cod_status', 0))
            raw_data = json.dumps(request.POST.dict())

            t = Transaction.objects.filter(order_id=order, transaction_id=transaction).first()

            if not t:
                t = Transaction(order_id=order, transaction_id=transaction)

            t.status = status
            t.status_code = status_code
            t.raw_data = raw_data
            t.save()

            msg = "Transaction(id={0})".format(t.id)
            return HttpResponse(content=msg)
        except Exception as e:
            full_request = {'GET': request.GET.dict(), 'POST': request.POST.dict(), 'error': e.message}
            return HttpResponse(content=json.dumps(full_request))

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(BCashUpdateView, self).dispatch(request, *args, **kwargs)

#
#class BCashForwardView(View):
#
#    def get(self, request, **kwargs):
#        subscription = Subscription.objects.get(**kwargs)
#        title = _('Subscription of %(volunteer)s for %(event)s %(year)s') % {
#            'volunteer': subscription.volunteer.user.get_full_name(),
#            'event': subscription.event.name,
#            'year': subscription.event.year,
#        }
#        campanha = "%s %s" % (subscription.event.name, subscription.event.year,)
#        parts = OrderedDict()
#        parts['campanha'] = campanha
#        parts['email_loja'] = ''
#        parts['meio_pagamento'] = '10'
#        parts['parcela_maxima'] = '1'
#        parts['produto_codigo_1'] = "Subscription(%d)" % subscription.id
#        parts['produto_descricao_1'] = title
#        parts['produto_qtde_1'] = 1
#        parts['produto_valor_1'] = subscription.event.subscription_value + subscription.extra_value
#        parts['redirect'] = 'true'
#        parts['redirect_time'] = '10'
#        parts['url_retorno'] = request.build_absolute_uri(reverse('bcash_update'))
#
#        try:
#            url = urllib.urlencode(parts)
#        except UnicodeEncodeError:
#            parts['produto_descricao_1'] = title.encode('utf-8')
#            parts['campanha'] = campanha.encode('utf-8')
#
#            url = urllib.urlencode(parts)
#
#            parts['produto_descricao_1'] = title
#            parts['campanha'] = campanha
#
#        secret = 'chave_secreta'
#        parts['hash'] = md5(url + secret).hexdigest()
#
#        title = 'Indo para o BCash'
#        action = 'https://www.bcash.com.br/checkout/pay/'
#        inputs = ''.join(['<input type="hidden" name="%s" value="%s"/>' % (k, v,) for k, v in parts.items()])
#        script = '<script type="text/javascript">window.onload=function(){document.forms[0].submit();}</script>'
#        html = '<html><head>%s</head><body><form action="%s" method="POST">%s</form></body></html>' % (
#            script, action, inputs
#        )
#        return HttpResponse(html)
