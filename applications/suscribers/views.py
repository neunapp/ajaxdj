#
from django.shortcuts import render
from django.http import JsonResponse

from django.views.generic import CreateView

from .models import Suscriptor


class SuscriptorCreateView(CreateView):
    template_name = "add.html"
    model = Suscriptor
    fields = ('__all__')
    success_url = '.'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["suscripciones"] = Suscriptor.objects.all()
        print('**************')
        return context
    

    def render_to_response(self, context, **response_kwargs):
        """  """
        if self.request.is_ajax():
            print('Es un peticon ajax*********')
            data = list(context["suscripciones"].values())
            return JsonResponse({'suscriptores': data})
        else:
            response_kwargs.setdefault('content_type', self.content_type)
            return self.response_class(
                request=self.request,
                template=self.get_template_names(),
                context=context,
                using=self.template_engine,
                **response_kwargs
            )
    

# cuando este proceso de la respuesta es repetitiva durante el proyecto
# podemos usar una de las mejores herramientas que ofrece Vistas basadas en clases
# que son los mixin, lo que nos ayuda a resumir aun mas las lineas de codigo
# ejemplo aqui abajo utilizano la misma vista


class AjaxaResponseMixin(object): 

    def render_to_response(self, context, **response_kwargs):
        """  """
        if self.request.is_ajax():
            data = list(context['suscripciones'].values())
            return JsonResponse({'suscriptores': data})
        else:
            response_kwargs.setdefault('content_type', self.content_type)
            return self.response_class(
                request=self.request,
                template=self.get_template_names(),
                context=context,
                using=self.template_engine,
                **response_kwargs
            )


class SuscriptorCreateView2(AjaxaResponseMixin, CreateView):
    template_name = "add.html"
    model = Suscriptor
    fields = ('__all__')
    success_url = '.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["suscripciones"] = Suscriptor.objects.all() 
        return context