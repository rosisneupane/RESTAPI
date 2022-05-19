from django.contrib import admin
from django.urls import path
from .views import article_list,article_detail,ArticleAPIView
urlpatterns = [
    # path('articles/',article_list),
    path('articles/',ArticleAPIView.as_view()),
    path('article/<int:pk>/',article_detail)
]
