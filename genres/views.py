from django.http import JsonResponse
from genres.models import Genres
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404


"""
@csrf_exempt é usado no Django para desabilitar a 
proteção contra  CSRF (Cross-Site Request Forgery) em uma
view específica. Quando aplicado, ele impede que o Django 
verifique o CSRF token nas requisições feitas a essa view.
"""

@csrf_exempt
def genre_list_creat(request):
    
    if request.method == "GET":
        search = Genres.objects.all()
        list_genre = [{'id' : genre.id, 'name' : genre.name} for genre in search]
        return JsonResponse(
            {'message': 'Todos os gêneros', 
             'genres': list_genre
            },
             safe=False)
    
    elif request.method == "POST":
        
        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genres(name = data ['name'])
        new_genre.save()
        return JsonResponse(
            {
                'message':'Gênero cadastrado com sucesso',
                'id' : new_genre.id, 
                'name': new_genre.name
            }, 
            status= 201)

@csrf_exempt
def genre_update_delete(request, pk):
    search = get_object_or_404(Genres, pk=pk) #pesquisa filtrada por pk (primary key)
    print(search)
    
    if request.method == 'GET':
        data = {'id':search.id, 'name': search.name}
        return JsonResponse(data)
    
    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8')) #carrega informações que o usuário disponibilizou
        search.name = data['name']
        search.save()
        return JsonResponse(
            {'message':'Gênero atualizado com sucesso',
             'id':search.id, 
             'name': search.name
            },
            status=202)
    
    elif request.method == 'DELETE':
        search.delete()
        return JsonResponse(
            {'message':'Gênero de filme deletado com sucesso'},
            status=202)
        
    
    
    