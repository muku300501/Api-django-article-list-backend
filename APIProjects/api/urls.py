from django.urls import path, include
# from .views import article_list, article_details(Function based api url imports)
# from .views import ArticleList, ArticleDetails(Class based api url imports)
from .views import ArticleViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
router.register('users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    # CLASS-BASED API URL PATTERNS
    #path('articles/', ArticleList.as_view()),
    #path('articles/<int:id>/', ArticleDetails.as_view()),

    # FUNCTION-BASED API URL PATTERNS
    # path('articles/', article_list),
    # path('articles/<int:pk>/', article_details),
]
