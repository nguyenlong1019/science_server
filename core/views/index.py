from django.shortcuts import render 


def index_view(request):
    return render(request, 'core/index.html', status=200)


def topic_detail_view(request, slug):
    pass 


def document_detail_view(request, slug):
    pass 
