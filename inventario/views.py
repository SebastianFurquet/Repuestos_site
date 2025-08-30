from django.shortcuts import render, redirect, get_list_or_404
from django.db.models import Q
from .models import Estructura
from .forms import EstructuraForm, BusquedaForm

def index(request):
    return render(request, 'inventario/index.html')


def estructura_list(request):
    form = BusquedaForm(request.GET or None)
    qs = Estructura.objects.select_related(
        "modelo", "modelo__marca", "modelo__clase", "parte", "elemento"
    )
    if form.is_valid():
        q = form.cleaned_data.get("q")
        if q:
            qs = qs.filter(
                Q(nro_pieza__icontains=q) |
                Q(modelo__cod_modelo__icontains=q) |
                Q(elemento__cod_elemento__icontains=q) |
                Q(elemento__nombre__icontains=q)
            )
    qs = qs.order_by("modelo__marca__nombre", "modelo__descripcion", "parte__nombre", "elemento__nombre")
    return render(request, "inventario/estructura_list.html", {'form': form, 'objetos': qs})


def estructura_create(request):
    if request.method == "POST":
        form = EstructuraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estructura_list')
    else:
        form = EstructuraForm()
    
    return render(request, 'inventario/estructura_form.html', {'form': form})