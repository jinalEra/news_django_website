from django.shortcuts import render
from api.models import Product
import requests
# Create your views here.
# fetch data for user
API_KEY = '1cad6972504848f38785e5cddceb7d0e'


def showAllPro(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'backend/home.html', context)

def news(request):

    country = request.GET.get('country')
    category = request.GET.get('category')

    if country:
        news_url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url=news_url)
        data = response.json()
    elif category:
        news_url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url=news_url)
        data = response.json()
    else:
        news_url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
        response = requests.get(url=news_url)
        data = response.json()
    # print(data)

    article = data['articles']

    context = {
        'article': article
    }
    return render(request, 'backend/news.html', context)
