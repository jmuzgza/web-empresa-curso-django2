from django.shortcuts import render, HttpResponse

# Create your views here.
"""Añade una app Core con una vista para cada página de la cafetería, deberás añadir las respectivas URL y lograr que todo funcione. Por ahora puedes devolver un HttpResponse simple con el nombre de las página:

    Inicio home/

    Historia about/

    Servicios services/

    Visítanos store/

    Contacto contact/

    Blog blog/

    Sample sample/ (esta es para páginas de prueba)
    """

def home(request):
    # return HttpResponse("Inicio")
    return render(request, "core/home.html")
def about(request):
    return render(request, "core/about.html")

def store(request):
    return render(request, "core/store.html")
    




   
     
    

