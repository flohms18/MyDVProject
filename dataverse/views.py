from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import DataRole, Article, GlossaryTerm, Category
# Create your views here.

def datarole(request):
    queryset = DataRole.objects.all()  
    return render(request, "dataverse/datarole.html",{'queryset': queryset})

def about(request):
    return render(request,'dataverse/about.html')

def glossary(request):
    glossary_dict = {}
    terms = GlossaryTerm.objects.all().order_by("term")
    for term in terms:
        FirstLetter = term.term[0].upper()
        if FirstLetter not in glossary_dict:
            glossary_dict[FirstLetter] = []
        glossary_dict[FirstLetter].append(term)

    return render(request, 'dataverse/glossary.html', {
        'glossary_dict': glossary_dict})

def index(request):
    featured_articles = Article.objects.filter(is_featured=True).order_by('-published_date')
    recent_articles = Article.objects.filter(is_featured=False).order_by('-published_date')

    paginator = Paginator(recent_articles, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()

    return render(request, "dataverse/index.html", {
        'featured_articles': featured_articles,
        'page_obj': page_obj,
        'categories': categories,
    })


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles_list = Article.objects.filter(category=category).order_by('-published_date')
    
    paginator = Paginator(articles_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, "dataverse/category_detail.html", {
        'category': category,
        'page_obj': page_obj,
    })


def governance(request):
    return render(request,'dataverse/governance.html')

def datarole_detail(request, slug):
    dr = get_object_or_404(DataRole, slug=slug)    
    obj = DataRole.objects.all()
    return render(request, "dataverse/datarole_detail.html", {
        'dr': dr
})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)    
    return render(request, "dataverse/article_detail.html", {
        'article': article
})

def data_mindset(request):
    obj = Article.objects.filter(insight__name="Data Mindset").order_by('-published_date')    
    paginator = Paginator(obj, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "dataverse/data_mindset.html", {
        'obj': obj,
        'page_obj' : page_obj
    })

def analytic_edge(request):
    obj = Article.objects.filter(insight__name="Analytic Edge").order_by('-published_date')
    paginator = Paginator(obj, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "dataverse/analytic_edge.html", {
        'obj': obj,
        'page_obj' : page_obj,
    })
