from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import persona
from .forms import SimpleForm,personaForm
from django.http import HttpResponseRedirect


def lista_personas(request):
        lista = persona.objects.all()
        ctx = {'lista':lista}
        return render_to_response('lista.html',ctx,
                        context_instance=RequestContext(request))

def formulario(request):
        if request.method == "POST":
            form = personaForm(request.POST,request.FILES)
            if form.is_valid():
                p = form.save()
                p.save()

                return HttpResponseRedirect('/')
            else:
                form = personaForm(request.POST,request.FILES['foto'])
                ctx = {'form':form}
                return render_to_response('form.html',ctx,
                            context_instance=RequestContext(request))

        else:
            form = personaForm()
            ctx = {'form':form}
            return render_to_response('form.html',ctx,
                        context_instance=RequestContext(request))
