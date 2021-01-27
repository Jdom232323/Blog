from django.http import HttpResponse,render

def home(request):#primera vista
    return HttpResponse("Pagina principal")

def perfil_personal(request):#primera vista
    return HttpResponse("Servicios")
    
def blog(request):#primera vista
    return HttpResponse("blog")

def contacto(request):#primera vista
    return HttpResponse("contacto")

