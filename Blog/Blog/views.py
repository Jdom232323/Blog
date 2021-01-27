from django.http import HttpResponse

def home(request):#primera vista
    return HttpResponse("Pagina principal")

def entradas(request):#primera vista
    return HttpResponse("aqui iran unas entradas a mis proyectos")