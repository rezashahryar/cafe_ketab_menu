from django.shortcuts import get_object_or_404
from django.views import generic

from products.models import Category
# Create your views here.

class HomePageView(generic.TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()

        return context
    

class CategoryObjects(generic.ListView):
    template_name = 'pages/category_objects.html'
    context_object_name = 'products'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        cat_obj = get_object_or_404(Category, slug=slug)

        return cat_obj.products.all()
    
    def get_context_data(self, **kwargs):
        slug = self.kwargs.get('slug')
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, slug=slug)

        return context
