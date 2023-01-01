from django.views.generic import ListView, DetailView
from .models import Product
from .filters import ProductFilter
from .models import Product, News
from datetime import datetime


from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from .filters import *
from .forms import ProductForm
from .models import Product


class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'


class ProductCreate(CreateView):
    form_class = ProductForm
    model = Product
    template_name = 'product_edit.html'


class ProductUpdate(UpdateView):
    form_class = ProductForm
    model = Product
    template_name = 'product_edit.html'

# Представление удаляющее товар.
class ProductDelete(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')

class ProductDelete(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')




class NewsList(ListView):
    model = News
    ordering = 'date'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsShow(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = News
    # Используем другой шаблон — product.html
    template_name = 'article.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'news'


class NewsDetail(DetailView):
    model = News
    template_name = 'news.html'
    context_object_name = 'product'


class NewsCreate(CreateView):
    form_claNews = ProductForm
    model = Product
    template_name = 'news_edit.html'


class NewsUpdate(UpdateView):
    form_claNews = ProductForm
    model = Product
    template_name = 'news_edit.html'

# Представление удаляющее товар.
class NewsDelete(DeleteView):
    model = News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')

# from django.shortcuts import render, reverse, redirect
# from django.views import View
# from django.core.mail import send_mail
# from datetime import datetime
 
# from .models import User
 
 
# class AppointmentView(View):
#     def post(self, request, *args, **kwargs):
#         message = User(
#             date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
#             client_name=request.POST['client_name'],
#             message=request.POST['message'],
#         )
#         message.save()

#         send_mail( 
#             subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%M-%d")}',  # имя клиента и дата записи будут в теме для удобства
#             message=appointment.message,  # сообщение с кратким описанием проблемы
#             from_email='peterbadson@yandex.ru', # здесь указываете почту, с которой будете отправлять (об этом попозже)
#             recipient_list=[]  # здесь список получателей. Например, секретарь, сам врач и т. д.
#         )
 
#         return redirect('appointments:make_appointment')

# вот мой проэкт [ссылка на гитхаб]. Я добавил уже catetory и все нужные связи (как мне кажется). Но, я ну думаю что я вообще понимаю как что делать дальше. Тем более в курсе были достаточно конкретные примеры, я не совсем понмиаю как это применить ко мне. Нужно ли мне в views.py выхывать чтото типо News.category.subscribs[i]? каким образом я аддресую это всё. Плюс я сделал регестрацию и пользывателей совершенно в другом проэкте (который уже утерян), и теперь я незнаю как и что тут должно работать чтобы отправлялись нужные сообщения.
# я подозревая мне нужно создать определённый view котоырый будет идти по списку подписчиком категорий, и отправлять сообщения. Но что и как будет активирывать функцию отправки я незнаю, как сделать так чтобы это работало автоматически при добавлении новой новости определённой категории я незнаю. В оригинальной статьъе (d9.2.) пользыватели отправляли appointment-ы, но тут уже другая структура данных и я не знаю как обращатся, и к чему обращатся - тут нет такой одной модели особо.
# В общем, я не совсем понимаю как выполнить задание