from pages.models import Page

def get_pages(request):

    pages = Page.objects.filter(visible=True).order_by('order').values_list('id', 'title', 'slug')
    # pages = Page.objects.all()

    return {
        'pages': pages
    }