from unicodedata import name
from django.urls import path, include
from backendapi.views import ArticleViewSet
#from .views import article_list, article_details
#from .views import ArticleList, ArticleDetails

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')

urlpatterns = [
    #path('articles/', article_list, name='articles'),
    #path('articles/<slug:slug>/', article_details, name='article-details'),
    # path('articles/', ArticleList.as_view()),
    # path('articles/<slug:slug>/', ArticleDetails.as_view()),

    path('', include(router.urls))
]