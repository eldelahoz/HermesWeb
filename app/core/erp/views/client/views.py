from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from core.erp.forms import ClientForm
from core.erp.models import Client


class ClientListView(TemplateView):
    model = Client
    template_name = 'client/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        a = request
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                # print(Client.objects.all())
                for i in Client.objects.all():
                    data.append(i.toJSON())
            if action == 'add':
                cli = Client()
                cli.nombres = request.POST['nombres']
                cli.apellidos = request.POST['apellidos']
                cli.dni = request.POST['dni']
                cli.fecha_nac = request.POST['fecha_nac']
                cli.direccion = request.POST['direccion']
                cli.sexo = request.POST['sexo']
                cli.save()
            if action == 'edit':
                cli = Client.objects.get(pk=request.POST['id'])
                cli.nombres = request.POST['nombres']
                cli.apellidos = request.POST['apellidos']
                cli.dni = request.POST['dni']
                cli.fecha_nac = request.POST['fecha_nac']
                cli.direccion = request.POST['direccion']
                cli.sexo = request.POST['sexo']
                cli.save()
            if action == 'delete':
                cli = Client.objects.get(pk=request.POST['id'])
                cli.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado Clientes'
        context['entity'] = 'Clientes'
        context['list_url'] = reverse_lazy('erp:client_list')
        context['tablaName'] = 'tablaClient'
        context['form'] = ClientForm
        return context
