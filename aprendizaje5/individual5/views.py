from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import FormularioRegistroUsuario, FormularioRegistroProveedor

def index(request):
    "Vista para renderizar la página inicial"
    return render(request, 'index.html')

def lista_usuarios(request):
    "Vista para renderizar la página donde se mostrarán los datos de usuarios"
    usuarios = User.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

def registro_usuario(request):
    if request.method == 'POST':
        form = FormularioRegistroUsuario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form = FormularioRegistroUsuario()
    return render(request, 'registro_usuario.html', {'form':form})

def registrar_proveedor(request):
    if request.method == 'POST':
        form = FormularioRegistroProveedor(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'proveedor.html', {'form': FormularioRegistroProveedor(), 'message': 'Proveedor guardado en la base de datos'})
    else:
        form = FormularioRegistroProveedor()
    return render(request, 'proveedor.html', {'form': form})