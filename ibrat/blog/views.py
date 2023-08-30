from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    news = News.objects.all()
    first_element = news[len(news)-1]
    second_element = news[len(news)-2]
    third_element = news[len(news)-3]

    context = {
        'first_element': first_element,
        'second_element': second_element,
        'third_element': third_element
        }
    return render(request, 'index.html', context)

def news_detail(request, pk):
    new = News.objects.get(pk=pk)
    print(new)
    return render(request, 'news_detail.html', {'new': new})