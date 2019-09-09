from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Clientes
from .forms import ClienteForm



# Create your views here.
@login_required
def clientes_list(request):
    clientes = Clientes.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

@login_required
def clientes_new(request):
    form = ClienteForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('cliente_list')
    return render(request, 'clientes_form.html', {'form': form})

@login_required
def cliente_update(request, id):
    cliente = get_object_or_404(Clientes, pk=id)
    form = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('cliente_list')
    return render(request, 'clientes_form.html', {'form': form})


@login_required
def cliente_delete(request, id):
    cliente = get_object_or_404(Clientes, pk=id)
    form = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)

    if request.method == "POST":
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'cliente_delete_confirm.html', {'form': form})





