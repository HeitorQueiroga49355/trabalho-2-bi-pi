from django.shortcuts import render, get_object_or_404, redirect
from produto.models import Marca
from .forms import MarcaForm


def marca_editar(request, id):
    marca = get_object_or_404(Marca, id=id)

    if request.method == 'POST':
        form = MarcaForm(request.POST, request.FILES, instance=marca)

        if form.is_valid():
            form.save()
            return redirect('adm_marca_listar')
    else:
        form = MarcaForm(instance=marca)

    return render(request, 'marca/formAdm.html', {'form': form, 'active': 'marcas'})


def marca_remover(request, id):
    marca = get_object_or_404(Marca, id=id)
    marca.delete()
    return redirect('adm_marca_listar')


def marca_criar(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = MarcaForm()
            return redirect('adm_marca_listar')
    else:
        form = MarcaForm()

    return render(request, "marca/formAdm.html", {'form': form, 'active': 'marcas'})


def adm_marca_listar(request):
    marcas = Marca.objects.all()
    context = {
        'marcas': marcas, 'active': 'marcas',
    }
    return render(request, "marca/marcasAdm.html", context)
