from django.shortcuts import render, get_object_or_404
from . models import Album



def index(request):
    all_albums = Album.objects.all()

    context = {'all_albums': all_albums, }
    return render(request, 'classroom/index.html', context)
def calculate(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums, }
    for album in all_albums:
        if album.marks<50 & album.marks>30:
            album.marks = album.marks+10
            album.save()
    return render(request, 'classroom/index.html', context)





