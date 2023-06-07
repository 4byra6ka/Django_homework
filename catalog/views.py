from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from catalog.models import Product, Category
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage


class ProductListView(generic.ListView):
    paginate_by = 3
    model = Product
    extra_context = {
        'title': 'Главное меню "Каталог"'
    }
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        all_product = Product.objects.all()
        context['all_product_list'] = all_product
        return context

# def catalog(request):
#     products_list = Product.objects.all().order_by('id')
#     paginator = Paginator(products_list, 3)
#
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {
#         'object_list': products_list,
#         'page_object': page_obj,
#         'title': 'Главное меню "Каталог"'
#     }
#     return render(request, 'catalog/product_list.html', context)


class ProductDetailView(generic.DetailView):
    model = Product
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        all_product = Product.objects.all()
        context['all_product_list'] = all_product
        context['title'] = context['object']
        return context
# def product(request, pk):
#     products_list = Product.objects.all()
#     product_item = Product.objects.get(pk=pk)
#     context = {
#         'object_list': products_list,
#         'product': product_item,
#         'title': f'Товар {product_item.name}'
#     }
#     return render(request, 'catalog/product_detail.html', context=context)


class ProductCreateView(generic.CreateView):
    model = Product
    extra_context = {
        'title': 'Добавить товар'
    }
    fields = ('name', 'description', 'image', 'category', 'price')
    # success_url = reverse_lazy('catalog:index')
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        all_product = Product.objects.all()
        context['all_product_list'] = all_product
        category_list = Category.objects.all()
        context['category_list'] = category_list
        return context
# def add_product(request):
#     products_list = Product.objects.all()
#     category_list = Category.objects.all()
#     context = {
#         'object_list': products_list,
#         'category_list': category_list,
#         'add_items': None,
#         'title': f'Добавить товар',
#     }
#     if request.method == 'POST':
#         product_item = Product(
#             name=request.POST.get('name'),
#             description=request.POST.get('description'),
#             category=Category.objects.get(name=request.POST.get('category')),
#             price=request.POST.get('price'))
#         if request.POST.get('image') != '':
#             image = request.FILES['image']
#             fs = FileSystemStorage()
#             filename = fs.save(f'products/{image.name}', image)
#             uploaded_file_url = fs.url(filename)
#             product_item.image = filename
#         product_item.save()
#         context['add_items'] = True
#     return render(request, 'catalog/add_product.html', context=context)

def contact(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
        'title': 'Контакты'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    return render(request, 'catalog/contact.html', context)






