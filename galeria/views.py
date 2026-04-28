from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Foto
from .forms import FotoForm

@login_required
def index(request):
    if request.method == 'POST':
        # Sacamos el archivo directamente del request
        imagen = request.FILES.get('imagen')
        if imagen:
            # Creamos la foto usando el nombre del archivo como título automático
            Foto.objects.create(
                usuario=request.user,
                titulo=imagen.name, 
                imagen=imagen
            )
            return redirect('index')
    
    fotos = Foto.objects.filter(usuario=request.user)
    return render(request, 'galeria/index.html', {'fotos': fotos})

@login_required
def eliminar_foto(request, foto_id):
    # DELETE: Borrar foto
    foto = get_object_or_404(Foto, id=foto_id, usuario=request.user)
    foto.delete()
    return redirect('index')