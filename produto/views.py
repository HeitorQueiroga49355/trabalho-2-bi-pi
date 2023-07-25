from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Marca
from .forms import ProdutoForm


def produto_editar(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)

        if form.is_valid():
            form.save()
            return redirect('produto_listar')
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'produto/formAdm.html', {'form': form, 'active': 'produtos', })


def produto_remover(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('produto_listar')


def produto_detalhe(request, id):
    produto = get_object_or_404(Produto, id=id)
    context = {
        'produto': produto
    }
    return render(request, "produto/detalhe.html", context)


def produto_criar(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('produto_listar')
        else:
            print(form.errors)
    else:
        form = ProdutoForm()

    context = {
        'form': form,
        'active': 'produtos',
    }

    return render(request, "produto/formAdm.html", context)


def produto_listar(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos,
        'active': 'produtos',
    }
    return render(request, "produto/produtosAdm.html", context)


def index(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos,
    }
    return render(request, "produto/index.html", context)


def crud(request):
    produtos = Produto.objects.count()
    marcas = Marca.objects.count()
    context = {
        'produtos_total': produtos,
        'marcas_total': marcas,
        'active': 'dashboard'
    }
    return render(request, "produto/crud.html", context)
