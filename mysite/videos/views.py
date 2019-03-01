from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'random_videos': ['Random example'],
        'all_videos': ['Normal example 1', 'Normal example 2'],
    }
    return render(request, 'videos/videos.html', context)


def edit_video(request):
    pass
