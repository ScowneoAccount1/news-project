from django.urls import path
# Импортируем созданные нами представления
from .views import NewsList, NewsShow

urlpatterns = [
   path('', NewsList.as_view(), name='news_list'),
   path('<int:pk>', NewsShow.as_view(), name='news_show'),
]