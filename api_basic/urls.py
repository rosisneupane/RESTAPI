from django.contrib import admin
from django.urls import path
from .views import article_list,article_detail,ArticleAPIView,ArticleDetails
urlpatterns = [
    # path('articles/',article_list),
    path('articles/',ArticleAPIView.as_view()),
    path('article/<int:id>/',ArticleDetails.as_view())
]
