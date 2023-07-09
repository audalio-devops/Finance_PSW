import json
from django.http import JsonResponse
from django.shortcuts import render
from perfil.models import Categoria
from django.views.decorators.csrf import csrf_exempt

def definir_planejamento(request):
    categorias = Categoria.objects.all()
    return render(request, 'definir_planejamento.html', {'categorias': categorias})

@csrf_exempt
def update_valor_categoria(request, id):
    novo_valor = json.load(request)['novo_valor']
    print(f'Id : {id} - Novo valor: {novo_valor}')
    categoria = Categoria.objects.get(id=id)
    print (categoria)
    categoria.valor_planejamento = novo_valor
    categoria.save()

    return JsonResponse({'status': 'Sucesso'})

def ver_planejamento(request):
    categorias = Categoria.objects.all()
    #TODO: Realizar barra com total
    return render(request, 'ver_planejamento.html', {'categorias': categorias})
