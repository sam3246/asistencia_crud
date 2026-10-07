from django.shortcuts import render
from .models import asistencia

def crear(request):
    if request.method == 'POST':
        Asistencia = asistencia(
            tipo_documento = request.POST["tipo_documento"],
            documento = request.POST["documento"],
            nombres = request.POST["nombres"],
            apellidos = request.POST["apellidos"],
            whatsapp = request.POST["whatsapp"],
            fecha = request.POST["fecha"],
            asistencia = request.POST["asistencia"]
        )
        Asistencia.save()
    return render(request, "formulario.html")

def listar(request):
    #Select * from asistencias
    asistencias = asistencia.objects.all()
    return render(
        request,
        "lista.html",
        {"asistencias":asistencias}
    )

#Consultar la información de un registro
def detalle(request,id):
    Asistencia = asistencia.objects.get(id=id) #SELECT * FROM asistencias WHERE id=7
    return render(
        request, 
        "detalle.html",
        {"Asistencia": Asistencia})

def editar(request, id):
    Asistencia = asistencia.objects.get(id=id)#SELECT * FROM asistencias WHERE id=7
    
    if request.method=="POST":#Si se van a guardar los cambios
        Asistencia.tipo_documento = request.POST["tipo_documento"] #Cambiar el tipo de documento
        Asistencia.documento = request.POST["documento"] #Cambiar el documento
        Asistencia.nombres = request.POST["nombres"] #Cambiar los nombres
        Asistencia.apellidos = request.POST["apellidos"] #Cambiar los apellidos
        Asistencia.whatsapp = request.POST["whatsapp"] #Cambiar el número de whatsapp
        Asistencia.fecha = request.POST["fecha"] #Cambiar la fecha
        Asistencia.asistencia = request.POST["asistencia"] #Cambiar el estado de asistencia

        Asistencia.save() #Guardar los cambios

        return render(
            request,
            "detalle.html",
            {"Asistencia":Asistencia}
        )
    return render(
        request,
        "formulario.html",
        {"Asistencia": Asistencia}
    )

def eliminar(request,id):
    Asistencia = asistencia.objects.get(id=id)#SELECT * FROM asistencias WHERE id=7
    Asistencia.delete() #DELETE * FROM asistencias WHERE id= 7
    return render(
            request,
            "lista.html",
            {"Asistencia":Asistencia}
        )