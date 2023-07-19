from django.shortcuts import render,get_object_or_404,redirect
from .models import Produto, Marca
from .forms import ProdutoForm

def produto_editar(request,id):
    produto = get_object_or_404(Produto,id=id)
   
    if request.method == 'POST':
        form = ProdutoForm(request.POST,instance=produto)

        if form.is_valid():
            form.save()
            return redirect('produto_listar')
    else:
        form = ProdutoForm(instance=produto)

    return render(request,'produto/form.html',{'form':form})


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
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProdutoForm()
    else:
        form = ProdutoForm()

    context = {
        'form': form
    }

    return render(request, "produto/form.html", context)


def produto_listar(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, "produto/produtos.html", context)


def index(request):
    total_produtos = Produto.objects.count()
    total_marcas = Marca.objects.count()
    context = {
        'total_produtos': total_produtos,
        'total_marcas': total_marcas,
    }
    return render(request, "produto/index.html", context)
