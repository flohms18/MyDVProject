from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import DataRole, Article, GlossaryTerm
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
    obj = Article.objects.all().order_by('-is_featured', '-published_date')    
    paginator = Paginator(obj, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "dataverse/index.html", {
        'obj': obj,
        'page_obj' : page_obj,
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
