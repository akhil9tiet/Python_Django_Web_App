from django.http import HttpResponse, Http404
from django.template import loader
from .models import Album,Song
from django.shortcuts import render, get_object_or_404

# Create your views here.

def index(request):
    all_album= Album.objects.all()
    #template=loader.get_template('music/index.html')
    context={'all_album': all_album}
    #return HttpResponse(template.render(context, request))
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    '''try:
        album= Album.objects.get(pk=album_id)
        context={'album': album}
    except (Album.DoesNotExist):
        raise Http404("Album Does Not Exist")'''
    album=get_object_or_404(Album, pk=album_id)
    context={
        'album':album
    }
    #return HttpResponse("<h1>Details for album ID: "+ str(album_id) +" </h1>")
    return render(request,'music/detail.html', context)
