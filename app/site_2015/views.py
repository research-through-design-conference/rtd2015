from django.shortcuts import render, get_object_or_404
from site_2015.models import Page
from site_2015.models import Home

# Create your views here.


def home(request):
        pages = Page.objects.filter(top_level_nav=True).order_by('-pub_date')
        home = get_object_or_404(Home)
        # now return the rendered template
        return render(request, 'site_2015/home.html', {'page': pages, 'home': home})

def page(request, slug):
        # get the Page object
        pages = Page.objects.filter(top_level_nav=True).order_by('-pub_date')
        page = get_object_or_404(Page, slug=slug)
        # now return the rendered template
        return render(request, 'site_2015/page.html', {'page': pages, 'content' : page})
