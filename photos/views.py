#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from photos.models import Photo, PUBLIC


def home(request):
    photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
    context = {
        'photos_list': photos[:4]
    }
    return render(request, 'photos/home.html', context)

def detail(request, pk):
    """
    Carga la página de detalle de una foto
    :param request: HttpRequest
    :param pk: id de la foto
    :return: HttpResponse
    """
    # try:
    #     photo: Photo.objects.get(pk=pk)
    # except Photo.doesNotExist:
    #     phoyo = None
    # except Photo.MultipleObjects:
    #     photo = None
    possible_photos = Photo.objects.filter(pk=pk)
    # photo = (possible_photos.lenght == 1) ? possible_photos[0] : null
    photo = possible_photos[0] if len(possible_photos) == 1 else None
    if photo is not None:
        # cargar la plantilla de detalle
        context ={
            'photo' : photo
        }
        return render(request, 'photos/detail.html', context)
    else:
        return HttpResponseNotFound('No existe esa foto !!!')

