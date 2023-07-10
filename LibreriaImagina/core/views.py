from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Libro, Cliente

import cx_Oracle
from django.http import HttpResponse

def iniciosesion(request):
    if request.method == 'POST':
        usuario_cli = request.POST.get('usuario_cli')
        contrasenia_cli = request.POST.get('contrasenia_cli')

        # Buscar el cliente en la base de datos
        try:
            cliente = Cliente.objects.get(usuario_cli=usuario_cli, contrasenia_cli=contrasenia_cli)
            # Inicio de sesión exitoso
            # Almacena el nombre del cliente en una cookie
            response = redirect('home')
            response.set_cookie('cliente_nombre', cliente.nombre_cli)
            return response
        except Cliente.DoesNotExist:
            # Usuario o contraseña incorrectos
            messages.error(request, 'Credenciales inválidas')

    return render(request, 'registration/iniciosesion.html')


def cerrarsesion(request):
    response = redirect('iniciosesion')
    response.delete_cookie('cliente_nombre')
    return response


# def iniciosesion(request):
#     if request.method == 'POST':
#         usuario_cli = request.POST.get('usuario_cli')
#         contrasenia_cli = request.POST.get('contrasenia_cli')

#         # Conexión a la base de datos Oracle
#         conn = cx_Oracle.connect('bdLibreria/bdLibreria@127.0.0.1:1521/xe')

#         # Cursor para ejecutar consultas
#         cursor = conn.cursor()

#         # Consulta para obtener los datos del cliente con el usuario proporcionado
#         query = "SELECT usuario_cli, contrasenia_cli FROM cliente WHERE usuario_cli = :usuario"
#         cursor.execute(query, usuario=usuario_cli)
#         result = cursor.fetchone()

#         if result is not None:
#             # Verificar la contraseña
#             if contrasenia_cli == result[1]:
#                 # Inicio de sesión exitoso
#                 # Redirigir a una página de inicio de sesión exitoso
#                 return render(request, 'core/home.html')
        
#         # Inicio de sesión fallido
#         # Redirigir a una página de inicio de sesión fallido
#         return render(request, 'registration/iniciosesion.html')

#     return render(request, 'registration/iniciosesion.html')


def home(request):
    return render(request,'core/home.html')

def catalogo(request):
    libros = Libro.objects.all()
    data = {
        'libros' : libros
    }
    return render(request,'core/catalogo.html',data)

def servicios(request):
    return render(request,'core/servicios.html')

def quienessomos(request):
    return render(request,'core/quienessomos.html')

def home(request):
    return render(request,'core/home.html')

def seguimiento(request):
    return render(request,'core/seguimiento.html')

def registrouser(request):
    return render(request,'registration/registrouser.html')
