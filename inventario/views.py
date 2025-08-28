from django.shortcuts import render

# Create your views here.
def estructura_list(request):
    return render(request, 'inventario/estructura_list.html', {})