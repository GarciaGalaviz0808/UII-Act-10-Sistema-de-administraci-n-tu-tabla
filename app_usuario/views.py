# app_usuario/views.py (o el nombre de tu aplicación)
from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario # Cambiado de Producto a Usuario
from .forms import UsuarioForm # Cambiado de ProductoForm a UsuarioForm

# app_usuario/views.py

def index(request):
    usuarios = Usuario.objects.all()
    # Asegúrate de que 'app_usuario' aquí coincida con el nombre de tu aplicación
    return render(request, 'app_usuario/index.html', {'usuarios': usuarios})

def add_usuario(request): # Cambiado de add_producto a add_usuario
    success = False
    if request.method == 'POST':
        form = UsuarioForm(request.POST) # Cambiado de ProductoForm a UsuarioForm
        if form.is_valid():
            form.save()
            success = True
            # Puedes redirigir a la lista de usuarios después de agregar, como buena práctica
            # return redirect('index_usuarios') # Asumiendo un nombre de URL 'index_usuarios'
    else:
        form = UsuarioForm() # Cambiado de ProductoForm a UsuarioForm
    return render(request, 'app_usuario/add.html', {'form': form, 'success': success}) # Cambiado de app_producto/add.html a app_usuario/add.html

def edit_usuario(request, id_usuario): # Cambiado de edit_producto a edit_usuario y id_producto a id_usuario
    usuario = get_object_or_404(Usuario, id_usuario=id_usuario) # Cambiado de Producto a Usuario y id_producto a id_usuario
    success = False
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario) # Cambiado de ProductoForm a UsuarioForm
        if form.is_valid():
            form.save()
            success = True
            # Puedes redirigir a la lista de usuarios después de editar
            # return redirect('index_usuarios')
    else:
        form = UsuarioForm(instance=usuario) # Cambiado de ProductoForm a UsuarioForm
    return render(request, 'app_usuario/edit.html', {'form': form, 'success': success}) # Cambiado de app_producto/edit.html a app_usuario/edit.html

def delete_usuario(request, id_usuario): # Cambiado de delete_producto a delete_usuario y id_producto a id_usuario
    usuario = get_object_or_404(Usuario, id_usuario=id_usuario) # Cambiado de Producto a Usuario y id_producto a id_usuario
    if request.method == 'POST':
        usuario.delete() # Cambiado de producto.delete() a usuario.delete()
        return redirect('index_usuarios') # Asegúrate de que este nombre de URL sea el correcto para tu lista de usuarios
    return redirect('index_usuarios') # Asegúrate de que este nombre de URL sea el correcto para tu lista de usuarios